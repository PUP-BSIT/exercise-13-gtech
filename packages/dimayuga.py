from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.align import Align

console = Console()

def comment_aragon():
    console.print(
        Align.center(Panel(
            "[bold light_cyan1]Reliable team member! Always balance the team."
            "[/bold light_cyan1]",
            title="[italic deep_sky_blue1]Comment from Aragon",
            border_style="cyan"))
    )

def comment_lim():
    console.print(
        Align.center(Panel(
            "[bold light_cyan1]This is incredible! Good job![/bold light_cyan1]",
            title="[italic deep_sky_blue1]Comment from Lim",
            border_style="cyan"))
    )

def comment_lopez():
    console.print(
        Align.center(Panel(
            "[bold light_cyan1]A reliable teammate! Fun, smart, and a " \
                "great singer. IRL John Lloyd Cruz![/bold light_cyan1]",
            title="[italic deep_sky_blue1]Comment from Lopez",
            border_style="cyan"))
    )

def comment_romero():
    console.print(
        Align.center(Panel(
            "[bold light_cyan1]Smart, quick, and always ready to contribute. " 
            "You’re a huge asset to the team![/bold light_cyan1]",
            title="[italic deep_sky_blue1]Comment from Romero",
            border_style="cyan"))
    )

def display_menu():
    while True:
        console.print(
            Panel.fit("[bold cyan]Hi! I am AJ![/bold cyan]", style="bold magenta"),
            justify="center"
        )

        menu_text = Text()
        menu_text.append("1. ", style="bold green")
        menu_text.append("Basic Information\n")
        menu_text.append("2. ", style="bold green")
        menu_text.append("My Goals and Dreams\n")
        menu_text.append("3. ", style="bold green")
        menu_text.append("Comment from Aragon\n")
        menu_text.append("4. ", style="bold green")
        menu_text.append("Comment from Lim\n")
        menu_text.append("5. ", style="bold green")
        menu_text.append("Comment from Lopez\n")
        menu_text.append("6. ", style="bold green")
        menu_text.append("Comment from Romero\n")
        menu_text.append("0. ", style="bold red")
        menu_text.append("Exit\n")

        console.print(
            Panel(menu_text, title="Get to know me!", style="bold blue"),
            justify="center"
        )

        choice = Prompt.ask("👉 Select an option", choices=["0", "1", "2", "3", 
                                                           "4", "5", "6"])

        if choice == "1":
            console.print("[bold yellow]Name: Adriel Joseph Dimayuga"
                          "[/bold yellow]")
            console.print("[bold yellow]Age: 21[/bold yellow]")
            console.print("[bold yellow]Birthday: 21[/bold yellow]")
            console.print("[bold yellow]Gender: Male[/bold yellow]")
            console.print("[bold yellow]Program: Bachelor of Science in "
                          "Information Technology[/bold yellow]")
            console.print("[bold yellow]Hobbies:[/bold yellow]")
            console.print("[bold yellow] - I play games like League of Legends "
                          "and Valorant[/bold yellow]")
            console.print("[bold yellow] - I listen to music and practice "
                          "vocals[/bold yellow]")
            console.print("[bold yellow] - I watch tech-related YouTube videos "
                          "regularly to keep updated[/bold yellow]")

        elif choice == "2":
            console.print("🎯 [bold green]My goal is to become a skilled "
                          "developer. With this, I will be able to solve "
                          "problems through technology, because solving "
                          "something that gives a big impact to me and others "
                          "always excites me.[/bold green]")
            console.print("")
            console.print("[bold green]There is a Bible verse that helped me "
                          "get through hardships. To remember that there is "
                          "always someone who will be with you, will help you, "
                          "and will guide you.[/bold green]")
            console.print("")
            console.print("[italic green]I can do all things through Christ "
                          "who strengthens me.[/italic green] "
                          "[italic green]- Philippians 4:13[/italic green]")

        elif choice == "3":
            comment_aragon()
        elif choice == "4":
            comment_lim()
        elif choice == "5":
            comment_lopez()
        elif choice == "6":
            comment_romero()
        elif choice == "0":
            console.print("[bold red]Exiting the menu. Goodbye![/bold red]")
            break

        console.print("")
        Prompt.ask("🔁 Press Enter to return to the menu", 
                   default="", 
                   show_default=False)       
        console.clear()

