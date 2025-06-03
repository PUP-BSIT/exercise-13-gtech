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


        console.print("[bold cyan]Choose a module to explore:[/bold cyan]")
        console.print("1 - Aragon")
        console.print("2 - Dimayuga")
        console.print("3 - Lim")
        console.print("4 - Lopez")
        console.print("5 - Romero")
        console.print("6 - Exit")

        choice = input("\nEnter your choice: ").strip()

        clear_screen()

        if choice == "1":
            print_title("[bold magenta]You selected: Aragon Module[/bold magenta]")
        elif choice == "2":
            print_title("[bold magenta]You selected: Dimayuga Module[/bold magenta]")
        elif choice == "3":
            print_title("[bold magenta]You selected: Lim Module[/bold magenta]")
        elif choice == "4":
            print_title("[bold magenta]You selected: Lopez Module[/bold magenta]")
        elif choice == "5":
            print_title("[bold magenta]You selected: Romero Module[/bold magenta]")
            import packages.romero as romero
            romero.romero_menu()
        elif choice == "6":
            console.print("\n[bold green]Thank you! Goodbye![/bold green]")
            break
        else:
            console.print("[red]Invalid choice. Please select a number from 1 to 6.[/red]")

        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main_menu()



# TO DO
# Create a module with your last name as the module name.
#	- aragon
#	- dimayuga
#	- lim
#	- lopez
#   - romero

# TO DO
# For each member's module, create a function that display a menu with the 
# following options:
#	- basic info
#	- goals
#	- comments from other teammates

