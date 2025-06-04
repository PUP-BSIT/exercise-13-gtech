import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box

# List for the quote of the day method
fun_facts = [
    "🐱 Cats have over 20 muscles that control their ears.",
    "🦋 Butterflies can taste with their feet.",
    "🎨 Picasso learned to draw before he could talk.",
    "🌍 There are more trees on Earth than stars in the Milky Way.",
    "🧁 The first computer bug was an actual bug — a moth!",
    "🎈 Bananas are berries, but strawberries aren't.",
    "🐶 Dogs can understand up to 250 words and gestures.",
    "📚 Reading for just 6 minutes can reduce stress by 68%.",
]

# Create a styled output console
console = Console()

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Border function
def print_title(text):
    panel = Panel(
        Align.center(text, vertical="middle"),
        border_style="magenta",
        width=60,
        box=box.ROUNDED
    )
    console.print(panel)

def basic_info():
    print_title("[yellow]⋆˚✿˖° BASIC INFORMATION ⋆˚✿˖°")
    console.print("[cyan]☆ Name     : Hoshea Shania C. Lopez")
    console.print("[cyan]☆ Age      : 20")
    console.print("[cyan]☆ Birthday : July 10, 2004")
    console.print("[cyan]☆ Gender   : Female")
    console.print("[cyan]☆ City     : Paranaque")
    console.print("[cyan]☆ Program  : BS in Information Technology")
    console.print("[cyan]☆ Hobbies  : Drawing, sleeping, gaming, and reading")
    console.print("[cyan]☆ Favorite Color : Blue")
    console.print("[cyan]☆ Favorite Food  : French Fries")
    console.print("[cyan]☆ Pets  : 4 dogs (Teddy, Sophie, Mingyu, Abujing)")

def goals():
    print_title("[yellow]⟡ ݁₊ . MY GOALS IN LIFE ᯓ★")
    console.print("𖹭 [bold]Return to my passion: creating art 𖹭.ᐟ")
    console.print("୭˚ [bold]Live a prosperous and meaningful life ⋆.˚")
    console.print("⋆.˚ [bold]Help neglected and abused animals ୭ ˚. !")
    console.print("☾ [bold]Become better in programming ࣪ ִֶָ☾.[/]")

def random_fact():
    fact = random.choice(fun_facts)
    print_title("[yellow]Random Fact of the day!")
    console.print(f"[italic magenta]💡 Fun Fact: {fact}[/]\n")

def comments_aragon():
    print_title("[yellow]✦ Great member! Happy to have you in our group. ✦")
    # Put your comments here. (e.g. console.print("<comment> - Name"))

def comments_dimayuga():
    print_title("[yellow]✦ COMMENTS FROM TEAMMATE DIMAYUGA ✦")
    console.print("Not all heroes wear capes... "
                  "some debug without crying - AJ")

def comments_lim():
    print_title("[yellow]✦ COMMENTS FROM TEAMMATE LIM ✦")
    console.print("I like your design!")

def comments_romero():
    console.print("[yellow]✦ Your positivity is contagious!"
                "Thanks for always lifting the team’s mood.✦")

def goodbye():
    print_title("[yellow]Thank you for using the menu! (˶ˆᗜˆ˵)")

def lopez_menu():
    while True:
        clear_screen()
        print_title("[yellow]⋆｡°✩ WELCOME TO HOSHEA'S MENU ✩°｡⋆")

        print_title("[yellow]Good day! I'm Hoshea Shania C. Lopez, "
                    "a 2nd Year BSIT Student in PUPT. Always hoping "
                    "that the odds may ever be in my favor!")

        console.print("[1] ✦ Basic Information", style="bold cyan")
        console.print("[2] ✦ Goals", style="bold cyan")
        console.print("[3] ✦ Random Fact of the day!", style="bold cyan")
        console.print("[4] ✦ Comments from Teammate Aragon", style="bold cyan")
        console.print("[5] ✦ Comments from Teammate Dimayuga", 
                        style="bold cyan")
        console.print("[6] ✦ Comments from Teammate Lim", style="bold cyan")
        console.print("[7] ✦ Comments from Teammate Romero", style="bold cyan")
        console.print("[8] ✦ Exit", style="bold red")

        choice = console.input("\n[green]Choose an option:[/] ")

        clear_screen()

        if choice == "1":
            basic_info()
        elif choice == "2":
            goals()
        elif choice == "3":
            random_fact()
        elif choice == "4":
            comments_aragon()
        elif choice == "5":
            comments_dimayuga()
        elif choice == "6":
            comments_lim()
        elif choice == "7":
            comments_romero()
        elif choice == "8":
            goodbye()
            break
        else:
            console.print("[bold red]Invalid choice." \
                        "Please select a number that is available. (• ᴖ •｡ )")
            
        return