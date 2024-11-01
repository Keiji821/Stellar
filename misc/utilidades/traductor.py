from googletrans import Translator
from rich import print
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def traducir(texto, idioma_destino):
    try:
        traductor = Translator()
        resultado = traductor.translate(texto, dest=idioma_destino)
        return resultado.text
    except Exception as e:
        return f"Error al traducir: {e}"

if __name__ == "__main__":
    console.print("Bienvenido al Traductor en Termix", style="bold green")
    texto = input("Introduce el texto que deseas traducir: ")
    idioma_destino = input("Introduce el código del idioma de destino (ej. 'en' para inglés, 'es' para español): ")

    traduccion = traducir(texto, idioma_destino)
    console.print(f"Traducción: {traduccion}", style="bold blue")