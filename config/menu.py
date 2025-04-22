from rich.console import Console
import termios
import sys

console = Console()

fd = sys.stdin.fileno()
attr = termios.tcgetattr(fd)
termios.tcsetattr(fd, termios.TCSANOW, attr)

while True:
    char = sys.stdin.read(1)
    if char == "w":
        print("Has presionado la tecla w")
    elif char == "s":
        print("Has presionado la tecla s")
    elif char == "":
        break

termios.tcsetattr(fd, termios.TCSANOW, attr)