import requests
from bs4 import BeautifulSoup

def search_facebook(name):
    url = f"https://www.facebook.com/search/top/?q={name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for result in soup.find_all('div', {'class': '_5d-5'}):
        results.append({'name': result.find('h2').text.strip(), 'url': result.find('a')['href']})
    return results

def search_linkedin(name):
    url = f"https://www.linkedin.com/search/results/content/?keywords={name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for result in soup.find_all('li', {'class': 'result-card job-result-card result-card--with-hover-state'}):
        results.append({'name': result.find('h3', {'class': 'result-card__title'}).text.strip(),
                        'title': result.find('p', {'class': 'result-card__subtitle'}).text.strip(),
                        'company': result.find('p', {'class': 'result-card__meta'}).text.strip()})
    return results

def search_twitter(name):
    url = f"https://twitter.com/search?q={name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for result in soup.find_all('li', {'class': 'js-stream-item stream-item stream-item'}):
        results.append({'name': result.find('strong', {'class': 'fullname'}).text.strip(),
                        'username': result.find('span', {'class': 'username'}).text.strip()})
    return results

def search_instagram(name):
    url = f"https://www.instagram.com/web/search/topsearch/?query={name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for result in soup.find_all('div', {'class': '_7UhW9 vy6Bbq PIoX7 Mp0Rd fDxYl'}):
        results.append({'name': result.find('h2').text.strip(),
                        'username': result.find('span', {'class': '_7UhW9'}).text.strip()})
return results

def search_youtube(name):
    url = f"https://www.youtube.com/results?search_query={name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for result in soup.find_all('div', {'class': 'yt-lockup-dismissable'}):
        results.append({'title': result.find('a', {'class': 'yt-uix-tile-link'}).text.strip(),
                        'url': result.find('a', {'class': 'yt-uix-tile-link'})['href']})
    return results

def search_pinterest(name):
    url = f"https://www.pinterest.com/search/?q={name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for result in soup.find_all('div', {'class': 'hCL kmc'}):
        results.append({'title': result.find('a', {'class': 'htub2'}).text.strip(),
                        'url': result.find('a', {'class': 'htub2'})['href']})
    return results

def search_github(name):
    url = f"https://www.github.com/search?q={name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for result in soup.find_all('li', {'class': 'repo-list-item'}):
        results.append({'title': result.find('a', {'class': 'repo'}).text.strip(),
                        'url': result.find('a', {'class': 'repo'})['href']})
    return results

def search_person(name):
    results = []
    results.extend(search_facebook(name))
    results.extend(search_linkedin(name))
    results.extend(search_twitter(name))
    results.extend(search_instagram(name))
    results.extend(search_youtube(name))
    results.extend(search_pinterest(name))
    results.extend(search_github(name))
    return results

name = input("Ingresa el nombre de la persona a buscar: ")
results = search_person(name)
print(results)