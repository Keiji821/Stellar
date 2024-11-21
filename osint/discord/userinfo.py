import httpx
from bs4 import BeautifulSoup

def lookup_discord_user(user_id):
    url = f"https://discordlookup.com/user/{user_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        with httpx.Client(headers=headers, follow_redirects=True) as client:
            response = client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            return soup
    except httpx.RequestError as e:
        print(f"Error al realizar la solicitud: {e}")
        return None
    except httpx.HTTPStatusError as e:
        print(f"Error de estado HTTP: {e}")
        return None

def print_user_info(soup):
    user_info = {}
    user_info['username'] = soup.find('div', {'class': 'username'}).text.strip()
    user_info['discriminator'] = soup.find('div', {'class': 'discriminator'}).text.strip()
    user_info['avatar'] = soup.find('img', {'class': 'avatar'})['src']
    user_info['status'] = soup.find('div', {'class': 'status'}).text.strip()
    user_info['joined_at'] = soup.find('div', {'class': 'joined-at'}).text.strip()

    print("Username:", user_info['username'])
    print("Discriminator:", user_info['discriminator'])
    print("Avatar:", user_info['avatar'])
    print("Status:", user_info['status'])
    print("Joined at:", user_info['joined_at'])

user_id = input("Ingrese el ID: ")
html_data = lookup_discord_user(user_id)
if html_data:
    print_user_info(html_data)