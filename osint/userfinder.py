import requests
from bs4 import BeautifulSoup

def search_person(name):
    urls = [
        f"https://www.facebook.com/search/top/?q={name}",
        f"https://www.linkedin.com/search/results/content/?keywords={name}",
        f"https://twitter.com/search?q={name}",
        f"https://www.instagram.com/web/search/topsearch/?query={name}",
        f"https://www.pinterest.com/search/?q={name}",
        f"https://www.github.com/search?q={name}",
        f"https://www.youtube.com/results?search_query={name}",
        f"https://www.flickr.com/search/?q={name}",
        f"https://www.reddit.com/search?q={name}",
    ]
    results = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for result in soup.find_all('div', {'class': '_5d-5'}):
            results.append({'name': result.find('h2').text.strip(), 'url': result.find('a')['href']})
    return results

name = input("Ingresa el nombre de la persona a buscar: ")
results = search_person(name)
print(results)