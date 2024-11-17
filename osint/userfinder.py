import requests
from bs4 import BeautifulSoup
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, SpinnerColumn
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "DNT": "1",  
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Pragma": "no-cache",
    "TE": "trailers"
}
MAX_WORKERS = 8
console = Console()

def get_soup(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        console.print(f"[bold red]Error fetching {url}[/]: {e}")
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
        ("Twitter", search_twitter)
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
    console.print(Panel("[bold blue]Buscador de Información sobre usuarios.[/bold blue]", border_style="green"))
    name = input("Ingresa el nombre o término a buscar: ")
    console.print(f"[bold green]Buscando información para:[/bold] {name}")
    results = search_person(name)
    display_results(results)

if __name__ == "__main__":
    main()