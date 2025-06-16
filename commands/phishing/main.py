import os
import logging
from flask import Flask, request, render_template
from datetime import datetime
from rich.console import Console
import socket

console = Console()
logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

def get_client_info():
    headers = request.headers
    return {
        'ip': headers.get('X-Forwarded-For', request.remote_addr).split(',')[0],
        'ua': headers.get('User-Agent', 'Desconocido'),
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'host': socket.gethostname(),
        'method': request.method,
        'path': request.path
    }

@app.route('/')
def track():
    client = get_client_info()
    log_entry = (
        f"\n[ FECHA  ] {client['time']}\n"
        f"[ IP     ] {client['ip']}\n"
        f"[ AGENTE ] {client['ua']}\n"
        f"[ HOST   ] {client['host']}\n"
        f"[ METODO ] {client['method']}\n"
        "─" * 50
    )
    
    with open("visitas.log", "a") as f:
        f.write(log_entry)
    
    console.print(Panel.fit(
        f"[bold green]{log_entry}[/bold green]",
        title="Nueva Visita",
        border_style="cyan"
    ))
    
    return render_template("basic.html")

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000, threads=4)