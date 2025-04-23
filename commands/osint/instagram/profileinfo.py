import json
from bs4 import BeautifulSoup
import requests
import time
import random

def scrape_instagram(username):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept-Language': 'es-ES,es;q=0.9'
    }
    
    try:
        response = requests.get(f"https://www.instagram.com/{username}/", headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('script', string=lambda t: t and t.startswith('{"config"'))
        
        if not script:
            print("No se encontraron datos del perfil")
            return
            
        data = json.loads(script.string.split('window._sharedData = ')[1][:-1])
        user_data = data['entry_data']['ProfilePage'][0]['graphql']['user']
        
        print(f"Usuario: @{username}")
        print(f"Nombre: {user_data['full_name']}")
        print(f"Seguidores: {user_data['edge_followed_by']['count']:,}")
        print(f"Seguidos: {user_data['edge_follow']['count']:,}")
        print(f"Publicaciones: {user_data['edge_owner_to_timeline_media']['count']:,}")
        print(f"Biografía: {user_data['biography']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {str(e)}")
    except Exception as e:
        print(f"Error al procesar los datos: {str(e)}")

if __name__ == "__main__":
    username = input("Ingrese el usuario de Instagram: ").strip()
    scrape_instagram(username)
    time.sleep(random.uniform(3, 7))