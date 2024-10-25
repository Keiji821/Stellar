import torch
import tiktoken
from tokenizers import Tokenizer

# Inicializamos el tokenizer
tokenizer = Tokenizer.from_file("tiktoken-bert-base.json")

# Definimos un diccionario de respuestas
responses = {
    "hola": "Hola! ¿En qué puedo ayudarte?",
    "adiós": "Adiós! Espero verte pronto.",
    "¿qué hora es?": "Lo siento, no tengo acceso a la hora actual.",
    # Agrega más preguntas y respuestas aquí
}

# Definimos una función para procesar el texto ingresado por el usuario
def process_text(text):
    # Tokenizamos el texto
    tokens = tokenizer.encode(text)
    # Procesamos los tokens
    tokenized_text = []
    for token in tokens:
        tokenized_text.append(token.text)
    response = " ".join(tokenized_text)
    return response

# Definimos una función para obtener la respuesta correspondiente
def get_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return responses[user_input]
    else:
        return "Lo siento, no entiendo lo que estás diciendo."

# Definimos la función principal del chatbot
def stellar_chatbot():
    print("Stellar Chatbot iniciado. ¿En qué puedo ayudarte?")
    while True:
        # Leemos la entrada del usuario
        user_input = input(">>> ")
        # Procesamos la entrada del usuario
        response = get_response(user_input)
        # Imprimimos la respuesta
        print(response)

# Iniciamos el chatbot
stellar_chatbot()
