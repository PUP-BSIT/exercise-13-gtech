import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box

console = Console()

fun_facts = [
    "Cats have over 20 muscles that control their ears.",
    "Butterflies can taste with their feet.",
    "Picasso learned to draw before he could talk.",
    "There are more trees on Earth than stars in the Milky Way.",
    "The first computer bug was an actual bug — a moth!",
    "Bananas are berries, but strawberries aren’t.",
    "Dogs can understand up to 250 words and gestures.",
    "Reading for just 6 minutes can reduce stress by 68%.",
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title(title):
    panel = Panel(
        Align.center(title, vertical="middle"),
        border_style="bright_magenta",
        style="bold white on black",
        box=box.ROUNDED,
        width=65,
        padding=(1, 2)
    )
    console.print(panel)

def section_header(text):
    panel = Panel(
        f"[magenta]{text}",
        border_style="magenta",
        box=box.SQUARE,
        width=60,
        padding=(1, 2)
    )
    console.print(panel)

def basic_info():
    section_header("BASIC INFORMATION")
    console.print("[bold magenta]• Name      :[/] Dianna Rain M. Romero")
    console.print("[bold magenta]• Age       :[/] 19")
    console.print("[bold magenta]• Birthday  :[/] October 31, 2005")
    console.print("[bold magenta]• Gender    :[/] Female")
    console.print("[bold magenta]• Program   :[/] BSIT")
    console.print("[bold magenta]• Hobbies   :[/] Singing and cooking")

def goals():
    section_header("LIFE GOALS")
    console.print("[italic magenta]“Never stop learning."
                  "Grow through every challenge.”[/]")
    console.print("[italic magenta]“Live a life filled"
                 " with curiosity, creativity, and purpose.”[/]")

def comments_aragon():
    section_header("COMMENTS FROM ARAGON")
    #add comments here
    console.print("[magenta]»  ")

def comments_lopez():
    section_header("COMMENTS FROM LOPEZ")
    #add comments here
    console.print("[magenta]You always have an unstoppable force! " \
                        "Always fun and energetic.")

def comments_dimayuga():
    section_header("COMMENTS FROM DIMAYUGA")
    #add comments here
    console.print("[magenta]» Appreciate the effort you've been putting in "
                  "lately — keep it up!")

def comments_lim():
    section_header("COMMENTS FROM LIM")
    #add comments here
    console.print("[magenta]» Good job! Keep it up!")

def random_fact():
    fact = random.choice(fun_facts)
    section_header("RANDOM FACT OF THE DAY")
    console.print(f"[bright_magenta]💡 {fact}")

def goodbye():
    print_title("Thank you for exploring the menu, Rain! 🌙")

def romero_menu():
    while True:
        clear_screen()
        print_title("✦ I am Dianna Rain Romero ✦")

        console.print("[bold magenta][1][/bold magenta]Basic Info")
        console.print("[bold magenta][2][/bold magenta]Goals")
        console.print("[bold magenta][3][/bold magenta]Random Fact")
        console.print("[bold magenta][4][/bold magenta]Comments from Aragon")
        console.print("[bold magenta][5][/bold magenta]Comments from Lopez")
        console.print("[bold magenta][6][/bold magenta]Comments from Dimayuga")
        console.print("[bold magenta][7][/bold magenta]Comments from Lim")
        console.print("[bold red][8][/bold red]  Exit")

        choice = console.input("\n[bold magenta]Select an option:[/] ")

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
            comments_lopez()
        elif choice == "6":
            comments_dimayuga()
        elif choice == "7":
            comments_lim()
        elif choice == "8":
            goodbye()
            break
        else:
            console.print("[red]Invalid option. " 
            "Please select a number between 1 and 8.")

        console.input("\n[dim]Press Enter to return to the menu...[/]")
        return