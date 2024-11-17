import requests
from bs4 import BeautifulSoup
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, SpinnerColumn
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from concurrent.futures import ThreadPoolExecutor, as_completed
import random

HEADERS_LIST = [
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    },
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Accept-Language": "fr-FR,fr;q=0.5",
        "Cache-Control": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "TE": "trailers",
    },
    {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Accept-Language": "en-GB,en;q=0.9",
        "DNT": "1",
    },
]
MAX_WORKERS = 12
console = Console()

def get_soup(url):
    headers = random.choice(HEADERS_LIST)
    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        console.print(f"[bold red]Error al obtener {url}[/]: {e}")
        return None

def search_youtube(name):
    url = f"https://www.youtube.com/results?search_query={name}"
    soup = get_soup(url)
    results = []
    if not soup:
        return results
    for result in soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-video-renderer'}):
        title = result.text.strip()
        video_url = f"https://www.youtube.com{result['href']}"
        results.append({'platform': 'YouTube', 'title': title, 'url': video_url})
    return results

def search_github(name):
    url = f"https://github.com/search?q={name}"
    soup = get_soup(url)
    results = []
    if not soup:
        return results
    for result in soup.find_all('div', {'class': 'f4 text-normal'}):
        title = result.find('a').text.strip()
        repo_url = f"https://github.com{result.find('a')['href']}"
        results.append({'platform': 'GitHub', 'title': title, 'url': repo_url})
    return results

def search_stackoverflow(name):
    url = f"https://stackoverflow.com/search?q={name}"
    soup = get_soup(url)
    results = []
    if not soup:
        return results
    for result in soup.find_all('div', {'class': 'question-summary'}):
        title = result.find('a', {'class': 'question-hyperlink'}).text.strip()
        question_url = f"https://stackoverflow.com{result.find('a', {'class': 'question-hyperlink'})['href']}"
        votes = result.find('span', {'class': 'vote-count-post'}).text.strip()
        results.append({'platform': 'StackOverflow', 'title': title, 'url': question_url, 'votes': votes})
    return results

def search_reddit(name):
    url = f"https://www.reddit.com/search/?q={name}"
    soup = get_soup(url)
    results = []
    if not soup:
        return results
    for result in soup.find_all('div', {'class': 'Post'}):
        title_elem = result.find('h3')
        if title_elem:
            title = title_elem.text.strip()
            post_url = result.find('a', {'data-click-id': 'body'})['href']
            results.append({'platform': 'Reddit', 'title': title, 'url': f"https://www.reddit.com{post_url}"})
    return results

def search_wikipedia(name):
    url = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
    soup = get_soup(url)
    if not soup:
        return []
    results = []
    summary = soup.find('p')
    if summary:
        results.append({'platform': 'Wikipedia', 'title': 'Wikipedia Summary', 'content': summary.text.strip(), 'url': url})
    return results

def search_twitter(name):
    url = f"https://twitter.com/search?q={name}&src=typed_query"
    soup = get_soup(url)
    results = []
    if not soup:
        return results
    for result in soup.find_all('div', {'data-testid': 'tweet'}):
        user = result.find('span', {'class': 'username'})
        tweet_text = result.find('div', {'class': 'css-901oao'})
        if user and tweet_text:
            results.append({'platform': 'Twitter', 'title': user.text.strip(), 'content': tweet_text.text.strip()})
    return results

def search_person(name):
    searches = [
        ("YouTube", search_youtube),
        ("GitHub", search_github),
        ("StackOverflow", search_stackoverflow),
        ("Reddit", search_reddit),
        ("Wikipedia", search_wikipedia),
        ("Twitter", search_twitter),
        ("Instagram", search_instagram),
        ("LinkedIn", search_linkedin),
        ("Facebook", search_facebook),
        ("TikTok", search_tiktok)
    ]
    results = []
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Realizando búsquedas...[/cyan]", total=len(searches))
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(search_func, name): platform for platform, search_func in searches}
            for future in as_completed(futures):
                platform_results = future.result()
                results.extend(platform_results)
                progress.update(task, advance=1)
    return results

def search_instagram(name):
    url = f"https://www.instagram.com/explore/tags/{name}/"
    soup = get_soup(url)
    results = []
    if not soup:
        return results
    for result in soup.find_all('a', {'class': 'v1Nh3 kIKUG  _bz0w'}):
        title = result.find('img')['alt']
        post_url = f"https://www.instagram.com{result['href']}"
        results.append({'platform': 'Instagram', 'title': title, 'url': post_url})
    return results

def search_linkedin(name):
    url = f"https://www.linkedin.com/search/results/people/?keywords={name}"
    soup = get_soup(url)
    results = []
    if not soup:
        return results
    for result in soup.find_all('div', {'class': 'search-result__info'}):
        title = result.find('span', {'class': 'name'}).text.strip()
        profile_url = f"https://www.linkedin.com{result.find('a')['href']}"
        results.append({'platform': 'LinkedIn', 'title': title, 'url': profile_url})
    return results

def search_facebook(name):
    url = f"https://www.facebook.com/public/{name}"
    soup = get_soup(url)
    results = []
    if not soup:
        return results
    for result in soup.find_all('div', {'class': 'fsl fwb fcb'}):
        title = result.find('a').text.strip()
        profile_url = f"https://www.facebook.com{result.find('a')['href']}"
        results.append({'platform': 'Facebook', 'title': title, 'url': profile_url})
    return results

def search_tiktok(name):
    url = f"https://www.tiktok.com/search?q={name}"
    soup = get_soup(url)
    results = []
    if not soup:
        return results
    for result in soup.find_all('div', {'class': 'tiktok-1hvpfc4-DivItem'}):
        title = result.find('a', {'class': 'tiktok-1d7z6g9-AntA'}).text.strip()
        video_url = f"https://www.tiktok.com{result.find('a')['href']}"
        results.append({'platform': 'TikTok', 'title': title, 'url': video_url})
    return results

def display_results(results):
    if not results:
        console.print("[bold red]No se encontraron resultados.[/bold red]")
        return

    table = Table(title="Resultados de la Búsqueda", box=box.DOUBLE)
    table.add_column("Plataforma", style="cyan", no_wrap=True)
    table.add_column("Título", style="magenta")
    table.add_column("Enlace", style="green")
    table.add_column("Detalles", style="yellow", justify="center", overflow="fold")

    for result in results:
        title = result.get('title', 'Sin título')
        url = result.get('url', 'N/A')
        details = result.get('content', result.get('votes', 'N/A'))
        table.add_row(result.get('platform', 'Desconocido'), title, f"[link={url}]{url}[/link]" if url != 'N/A' else "N/A", str(details))

    console.print(Panel("Resultados de la Búsqueda Completada", border_style="blue"))
    console.print(table)

def main():
    console.print(Panel("[bold blue]Buscador de Información de usuarios.[/bold blue]", border_style="green"))
    name = input("Ingresa el nombre o término a buscar: ")
    console.print(f"[bold green]Buscando información para:[/bold green] {name}")
    results = search_person(name)
    display_results(results)

if __name__ == "__main__":
    main()