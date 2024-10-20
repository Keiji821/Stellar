import socket
import socks
import threading
from colorama import Fore, Style, init
from tabulate import tabulate

# Inicializa colorama
init(autoreset=True)

class Chat:
    def __init__(self, username, host='0.0.0.0', port=5555):
        self.username = username
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = None
        self.client_socket = None

        # Intentar iniciar como servidor
        try:
            self.setup_server()
            print(f"{Fore.GREEN}{Style.BRIGHT}Servidor iniciado en {self.host}:{self.port}. Esperando conexiones...{Style.RESET_ALL}")
        except OSError:
            print(f"{Fore.YELLOW}{Style.BRIGHT}No se pudo iniciar el servidor. Conectando como cliente...{Style.RESET_ALL}")
            self.setup_client()

    def setup_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        threading.Thread(target=self.accept_connections).start()

    def accept_connections(self):
        while True:
            client_socket, address = self.server_socket.accept()
            self.clients.append(client_socket)
            print(f"{Fore.CYAN}{Style.BRIGHT}Cliente conectado desde {address}{Style.RESET_ALL}")
            self.show_active_connections()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"{Fore.CYAN}{Style.BRIGHT}{message}{Style.RESET_ALL}")
                    self.broadcast(message)
            except Exception as e:
                print(f"{Fore.RED}{Style.BRIGHT}Error: {e}{Style.RESET_ALL}")
                client_socket.close()
                break

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"{Fore.RED}{Style.BRIGHT}Error al enviar el mensaje: {e}{Style.RESET_ALL}")
                client.close()
                self.clients.remove(client)

    def show_active_connections(self):
        table_data = [[i + 1, client.getpeername()[0], client.getpeername()[1]] for i, client in enumerate(self.clients)]
        print(tabulate(table_data, headers=["#", "IP", "Puerto"], tablefmt="fancy_grid"))

    def setup_client(self):
        # Intenta conectarse al servidor Tor local
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # Conectar al servidor local
            self.client_socket.connect((self.host, self.port))
            print(f"{Fore.GREEN}{Style.BRIGHT}Conectado al servidor {self.host}:{self.port}{Style.RESET_ALL}")
        except OSError as e:
            print(f"{Fore.RED}{Style.BRIGHT}[ERROR] No se pudo conectar al servidor: {e}{Style.RESET_ALL}")
            return

        # Iniciar el hilo para recibir mensajes
        threading.Thread(target=self.receive_message).start()

        # Enviar mensajes
        while True:
            message = input(f"{Fore.YELLOW}{Style.BRIGHT}{self.username}: {Style.RESET_ALL}")
            if message.lower() == 'salir':
                print(f"{Fore.BLUE}{Style.BRIGHT}Desconectando del servidor...{Style.RESET_ALL}")
                self.client_socket.close()
                break
            self.send_message(f"{self.username}: {message}")

    def send_message(self, message):
        try:
            self.client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"{Fore.RED}{Style.BRIGHT}Error al enviar el mensaje: {e}{Style.RESET_ALL}")

    def receive_message(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"{Fore.CYAN}{Style.BRIGHT}{message}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}{Style.BRIGHT}Conexión cerrada por el servidor.{Style.RESET_ALL}")
                    self.client_socket.close()
                    break
            except Exception as e:
                print(f"{Fore.RED}{Style.BRIGHT}Error en la conexión con el servidor: {e}{Style.RESET_ALL}")
                self.client_socket.close()
                break

if __name__ == '__main__':
    print(f"{Fore.MAGENTA}{Style.BRIGHT}Chat 1 a 1 Anónimo con Tor{Style.RESET_ALL}")

    # Pedimos solo el nombre de usuario
    username = input(f"{Fore.YELLOW}{Style.BRIGHT}Introduce tu nombre de usuario: {Style.RESET_ALL}")

    # Creamos el chat automáticamente como servidor o cliente
    chat = Chat(username=username)
