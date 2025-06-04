import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

# Clear terminal screen depending on OS 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def aragon_menu():
    # Main menu function displaying options and handling selections
    clear()
    while True:
        menu = (
            "[pink]꩜ .ᐟ Hello! I am Althea Mae C. Aragon .☘︎[pink]\n\n"
            "[1] Basic Information\n"
            "[2] Goals\n"
            "[3] Comments from Adriel Joseph Dimayuga\n"
            "[4] Comments from Grace Anne Lim\n"
            "[5] Comments from Hoshea Shania Lopez\n"
            "[6] Comments from Dianna Rain Romero\n"
            "[7] Back to Team Menu"
        )
        console.print(Panel(menu, title="⋆˚࿔ Althea's Menu ⋆˚࿔",
                             border_style="magenta"))

        #Prompt the user to choose an option
        choice = input("\nChoose an option: ").strip()
        clear()

        # Match-case in handling user input 
        match choice:
            case "1":
                basic_info()
            case "2":
                goals()
            case "3":
                comment_dimayuga()
            case "4":
                comment_lim()
            case "5":
                comment_lopez()
            case "6":
                comment_romero()
            case "7":
                console.print("\n[blue]Returning to Team Menu...[blue]")
                return
            case _:
                console.print("[red]Invalid choice. Please try again.[red]")
                input("Press ENTER to continue.")
                clear()

def basic_info():
    # Function to display basic information
    clear()
    # Displaying basic information
    console.print(Panel(
        "ʚɞ ⁺˖ Name: Althea Mae C. Aragon\n"
        "ʚɞ ⁺˖ Age: 20 years old\n"
        "ʚɞ ⁺˖ Birthday: April 30, 2005\n"
        "ʚɞ ⁺˖ Gender: Female\n"
        "ʚɞ ⁺˖ Hobbies: Watching dramas and doing makeup\n"
        "ʚɞ ⁺˖ Fun Fact: I am really into fashion and love thrifting!"
                       " I enjoy karaoke, I definitely can sing all day!",
        title="⋆𐙚₊˚ Basic Information ⋆˚࿔",
        border_style="magenta"
    ))
    # Displaying a short description about me
    console.print(
        Align.center(
        Panel.fit(
            "I am just a curious soul who loves diving into new experiences."
            " I enjoy making genuine connections, spreading good vibes, and"
            " cheering others on. I believe we rise by lifting others, so let"
            " us bond, grow, and inspire each other, because collaboration" 
            " will always beat competition!",
            title="⋆𐙚₊˚ About Me ⋆˚࿔",
            border_style="magenta"
        ))
    )
    input("\nPress ENTER to return to Althea's Menu")
    clear()

def goals():
    # Function to display goals
    clear()
    console.print(Panel(
        "✦ My Current Goals:\n\n"
        "ʚɞ ⁺˖ Pass all my college subjects.\n"
        "ʚɞ ⁺˖ Give back to my community and make a difference.\n"
        "ʚɞ ⁺˖ Enter the medical field after graduation and"
                " become who I really want to be.",
        title="⋆𐙚₊˚ Goals ⋆˚࿔",
        border_style="magenta"
    ))
    input("\nPress ENTER to return to Althea's Menu")
    clear()

def comment_dimayuga():
    # Function to display teammate Dimayuga comments
    console.print(Panel(
        "[yellow]⋆ˎˊ˗ Adriel Joseph Dimayuga: \n",
        title="⋆𐙚₊˚ Teammate Comments ⋆˚࿔",
        border_style="magenta"
    ))
    input("\nPress ENTER to return to Althea's Menu")
    clear()

def comment_lim():
    # Function to display teammate Lim comments
    console.print(Panel(
        "[yellow]⋆ˎˊ˗ Grace Anne Lim: \n",
        title="⋆𐙚₊˚ Teammate Comments ⋆˚࿔",
        border_style="magenta"
    ))
    input("\nPress ENTER to return to Althea's Menu")
    clear()

def comment_lopez():
    # Function to display teammate Lopez comments
    console.print(Panel(
        "[yellow]⋆ˎˊ˗ Hoshea Shania Lopez: \n",
        title="⋆𐙚₊˚ Teammate Comments ⋆˚࿔",
        border_style="magenta"
    ))
    input("\nPress ENTER to return to Althea's Menu")
    clear()

def comment_romero():
    # Function to display teammate Romero comments
    console.print(Panel(
        "[yellow]⋆ˎˊ˗ Dianna Rain Romero: \n",
        title="⋆𐙚₊˚ Teammate Comments ⋆˚࿔",
        border_style="magenta"
    ))
    input("\nPress ENTER to return to Althea's Menu")
    clear()

aragon_menu()
