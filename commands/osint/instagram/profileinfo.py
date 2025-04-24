import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def osint_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = uc.Chrome(options=options)

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "meta"))
        )
        metas = driver.find_elements(By.TAG_NAME, "meta")

        title = None
        desc = None
        image = None

        for meta in metas:
            name = meta.get_attribute("property")
            if name == "og:title":
                title = meta.get_attribute("content")
            elif name == "og:description":
                desc = meta.get_attribute("content")
            elif name == "og:image":
                image = meta.get_attribute("content")

        if not title or not desc or not image:
            console.print("[bold red]No se pudo extraer la información del perfil.[/bold red]")
            return

        parts = title.split("(@")
        name = parts[0].strip() if len(parts) > 1 else ""
        user = parts[1].rstrip(")") if len(parts) > 1 else username

        stats = desc.split(" • ")
        posts = stats[0].split(" ")[0]
        followers = stats[1].split(" ")[0]
        following = stats[2].split(" ")[0]

        console.print(Panel.fit(f"[bold cyan]Perfil OSINT de Instagram: @{user}[/bold cyan]", border_style="bright_blue"))
        if name:
            console.print(f"[bold]Nombre:[/bold] {name}")
        console.print(f"[bold]Seguidores:[/bold] {followers}")
        console.print(f"[bold]Siguiendo:[/bold] {following}")
        console.print(f"[bold]Publicaciones:[/bold] {posts}")
        console.print(f"[bold]Foto de perfil:[/bold] {image}")

    finally:
        driver.quit()

if __name__ == "__main__":
    username = Prompt.ask("[bold green]Ingresa el nombre de usuario[/bold green]")
    osint_instagram(username)