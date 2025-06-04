import packages.aragon as aragon
import packages.dimayuga as dimayuga
import packages.lim as lim
import packages.lopez as lopez
import packages.romero as romero
from rich.console import Console
from rich.panel import Panel 
from rich.align import Align
from rich import box
import os

# Initialize Console
console = Console()

# Function to clear terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print centered title panel
def print_title(text):
    panel = Panel(
        Align.center(text, vertical="middle"),  # Center text inside the panel
        border_style="magenta",
        width=60,
        box=box.ROUNDED
    )
    console.print(Align.center(panel))  # Center the panel on the screen

# Main menu
def main_menu():
    while True:
        clear_screen()
        title = "[bold magenta]Welcome to Gtech![/bold magenta]"
        print_title(title)

        menu_text = "\n".join([
            "[bold cyan]Choose a module to explore:[/bold cyan]",
            "1 - Aragon",
            "2 - Dimayuga",
            "3 - Lim",
            "4 - Lopez",
            "5 - Romero",
            "6 - Exit"
        ])

        # Create and center the menu panel
        menu_panel = Panel(
            Align.center(menu_text, vertical="middle"),
            border_style="cyan",
            width=60,
            box=box.DOUBLE_EDGE
        )
        console.print(Align.center(menu_panel)) 

        choice = console.input("\n[bold yellow]Enter your " \
                                    "choice:[/bold yellow] ").strip()

        clear_screen()

        if choice == "1":
            print_title("[bold magenta]You selected: " \
                            "Aragon Module[/bold magenta]")
            aragon.aragon_menu()
        elif choice == "2":
            print_title("[bold magenta]You selected: " \
                            "Dimayuga Module[/bold magenta]")
            dimayuga.display_menu()
        elif choice == "3":
            print_title("[bold magenta]You selected: " \
                            "Lim Module[/bold magenta]")
            lim.display_lim_menu()
        elif choice == "4":
            print_title("[bold magenta]You selected: " \
                            "Lopez Module[/bold magenta]")
            lopez.lopez_menu()
        elif choice == "5":
            print_title("[bold magenta]You selected: " \
                            "Romero Module[/bold magenta]")
            romero.romero_menu()
        elif choice == "6":
            console.print("\n[bold green]Thank you! Goodbye![/bold green]")
            break
        else:
            console.print("[red]Invalid choice. " \
                            "Please select a number from 1 to 6.[/red]")

main_menu()