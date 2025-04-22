from rich.console import Console
import termios

console = Console()

fd = termios.stdin.fileno()

entrada = termios.read(fd, 10)

print(entrada)
