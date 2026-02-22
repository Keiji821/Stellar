from rich.console import Console
import yaml
import os
 
console = Console()
 
def translate(category=None, type=None):
    try:
        os.chdir(os.path.expanduser("~/Stellar/configs"))
        with open('selected_lang.txt', 'r', encoding='utf-8') as archive:
            selected_lang = yaml.safe_load(archive)
        os.chdir(os.path.expanduser("~/Stellar/langs"))
        with open(f'{selected_lang}.yml', 'r', encoding='utf-8') as archive:
            lang = yaml.safe_load(archive)
        return lang[f"{category}"][f"{type}"]
    
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {lang["user-config"]["error_message"]} > {e}")
        return