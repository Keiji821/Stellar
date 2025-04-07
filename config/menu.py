from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.box import DOUBLE
from rich.style import Style

console = Console()

console.print(
    Panel.fit(
        Text("TERMINAL COMMANDER", justify="center", style="bold steel_blue1"),
        border_style="dim white",
        padding=(1, 4),
        style="on black",
        subtitle="v3.1.0"
    )
)

command_data = {
    "SYSTEM": {
        "color": "steel_blue1",
        "commands": {
            "reload": "Reload Stellar configuration",
            "clear": "Clear terminal screen",
            "bash": "Restart terminal session",
            "ui": "Customize interface themes"
        }
    },
    "UTILITIES": {
        "color": "dark_sea_green4",
        "commands": {
            "ia": "AI assistant service",
            "ia-image": "AI image generation",
            "traductor": "Multi-language translator",
            "myip": "IP address analyzer"
        }
    },
    "OSINT": {
        "color": "light_goldenrod3",
        "commands": {
            "ipinfo": "Advanced IP analysis",
            "phoneinfo": "Phone number lookup",
            "urlinfo": "URL/Domain scanner",
            "metadatainfo": "Metadata extraction",
            "emailsearch": "Email search tool",
            "userfinder": "Username tracker"
        }
    },
    "DISCORD": {
        "color": "medium_purple4",
        "commands": {
            "userinfo": "Discord user lookup"
        }
    }
}

for category, data in command_data.items():
    table = Table(
        show_header=False,
        box=DOUBLE,
        border_style=data["color"],
        padding=(0, 2),
        expand=True
    )
    table.add_column(width=20)
    table.add_column(width=50)
    
    table.add_row(
        f"[bold {data['color']}]{category}[/]",
        ""
    )
    
    for cmd, desc in data["commands"].items():
        table.add_row(
            f"[bold bright_white]{cmd}[/]",
            f"[bright_black]{desc}[/]"
        )
    
    console.print(table)
    console.print()

hotkeys_table = Table(
    box=DOUBLE,
    border_style="bright_white",
    show_header=False,
    padding=(0, 2),
    width=50
)
hotkeys_table.add_column(width=15)
hotkeys_table.add_column(width=35)
hotkeys_table.add_row("[bold bright_white]CTRL+Z[/]", "[bright_black]Safe process termination[/]")
hotkeys_table.add_row("[bold bright_white]CTRL+C[/]", "[bright_black]Force process termination[/]")

console.print(
    Panel.fit(
        hotkeys_table,
        title="KEYBINDS",
        border_style="dim white",
        style="on black"
    )
)