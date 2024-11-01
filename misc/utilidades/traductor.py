from googletrans import Translator

def traducir(texto, idioma_destino):
    traductor = Translator()
    try:
        resultado = traductor.translate(texto, dest=idioma_destino)
        return resultado.text
    except Exception as e:
        return f"Error al traducir: {e}"

if __name__ == "__main__":
    print("Bienvenido al Traductor en Termux")
    texto = input("Introduce el texto que deseas traducir: ")
    idioma_destino = input("Introduce el código del idioma de destino (ej. 'en' para inglés, 'es' para español): ")

    traduccion = traducir(texto, idioma_destino)
    print(f"Traducción: {traduccion}") 
