import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box

fun_facts = [
    "🐱 Cats have over 20 muscles that control their ears.",
    "🦋 Butterflies can taste with their feet.",
    "🎨 Picasso learned to draw before he could talk.",
    "🌍 There are more trees on Earth than stars in the Milky Way.",
    "🧁 The first computer bug was an actual bug — a moth!",
    "🎈 Bananas are berries, but strawberries aren’t.",
    "🐶 Dogs can understand up to 250 words and gestures.",
    "📚 Reading for just 6 minutes can reduce stress by 68%.",
]

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title(text):
    panel = Panel(
        Align.center(text, vertical="middle"),
        border_style="magenta",
        width=60,
        box=box.ROUNDED
    )
    console.print(panel)

def lopez_menu():
    while True:
        clear_screen()
        print_title("[yellow]⋆｡°✩ WELCOME TO HOSHEA'S MENU ✩°｡⋆")

        console.print("[1] ✦ Basic Info", style="bold cyan")
        console.print("[2] ✦ Goals", style="bold cyan")
        console.print("[3] ✦ Random Fact of the Day!", style="bold cyan")
        console.print("[4] ✦ Comments from Aragon", style="bold cyan")
        console.print("[5] ✦ Comments from Dimayuga", style="bold cyan")
        console.print("[6] ✦ Comments from Lim", style="bold cyan")
        console.print("[7] ✦ Comments from Romero", style="bold cyan")
        console.print("[8] ✦ Exit", style="bold red")

        choice = console.input("\n[green]Choose an option:[/] ")

        clear_screen()

        if choice == "1":
            print_title("[yellow]⋆˚✿˖° BASIC INFORMATION ⋆˚✿˖°")
            console.print("[cyan]☆ Name     : Hoshea Shania C. Lopez")
            console.print("[cyan]☆ Age      : 20")
            console.print("[cyan]☆ Birthday : July 10, 2004")
            console.print("[cyan]☆ Gender   : Female")
            console.print("[cyan]☆ Program  : Bachelor of Science in Information Technology")
            console.print("[cyan]☆ Hobbies  : Drawing, sleeping, gaming, and reading")
            console.print("[cyan]☆ Favorite Color : Blue")
            console.print("[cyan]☆ Favorite Food  : French Fries")

        elif choice == "2":
            print_title("[yellow]⟡ ݁₊ . MY GOALS IN LIFE ᯓ★")
            console.print("𖹭 [bold]Return to my passion: creating art 𖹭.ᐟ")
            console.print("୭˚ [bold]Live a prosperous and meaningful life ⋆.˚")
            console.print("⋆.˚ [bold]Help neglected and abused animals ୭ ˚. !")
            console.print("☾ [bold]Become better in programming ࣪ ִֶָ☾.")

        elif choice == "3":
            fact = random.choice(fun_facts)
            print_title("[yellow]Random Fact of the day!")
            console.print(f"[italic magenta]💡 Fun Fact: {fact}[/]\n")

        elif choice == "4":
            print_title("[yellow]✦ COMMENTS FROM TEAMMATE ARAGON ✦")
            #Put your Comment Here. (e.g. console.print("<comment> - Name"))

        elif choice == "5":
            print_title("[yellow]✦ COMMENTS FROM TEAMMATE DIMAYUGA ✦")
            #Put your Comment Here. (e.g. console.print("<comment> - Name"))

        elif choice == "6":
            print_title("[yellow]✦ COMMENTS FROM TEAMMATE LIM ✦")
            #Put your Comment Here. (e.g. console.print("<comment> - Name"))

        elif choice == "7":
            print_title("[yellow]✦ COMMENTS FROM TEAMMATE ROMERO ✦")
            #Put your Comment Here. (e.g. console.print("<comment> - Name"))
            
        elif choice == "8":
            print_title("Thank you for using the menu! (˶ˆᗜˆ˵)")
            break
        else:
            console.print("[bold red]Invalid choice.[/] Please select a number from 1 to 4.")

        console.input("\n[grey]Press Enter to return to the menu...[/]")

lopez_menu()