from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

def display_menu():
    console = Console()
    
    while True:
        console.print(
            Panel.fit("[bold cyan]Hi! I am AJ![/bold cyan]", 
                      style="bold magenta"),
            justify="center"
        )

        menu_text = Text()
        menu_text.append("1. ", style="bold green")
        menu_text.append("Basic Information\n")
        menu_text.append("2. ", style="bold green")
        menu_text.append("My Goals and Dreams\n")
        # make sure to use the same format
        # menu_text.append("n. ", style="bold green")
        # menu_text.append("<surname - comment>\n")
        menu_text.append("0. ", style="bold red")
        menu_text.append("Exit\n")

        console.print(
            Panel(menu_text, title="Get to know me!", style="bold blue"),
            justify="center"
        )

        # Modify "choices" add a number that corresponds to your comment
        choice = Prompt.ask("👉 Select an option", choices=["1", "2", "0"])

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
                          "get through hardships. To remember that there "
                          "is always someone who will be with you, "
                          "will help you, and will guide you.[/bold green]")
            console.print("")
            console.print("[italic green]I can do all things through Christ "
                          "who strengthens me.[/italic green] "
                          "[italic green]- Philippians 4:13[/italic green]")
            
        # place another elif here that will call your function
        
        elif choice == "0":
            console.print("[bold red]Exiting the menu. Goodbye![/bold red]")
            break

        console.print("")
        Prompt.ask("🔁 Press Enter to return to the menu", default="", 
                   show_default=False)
        
        console.clear()


display_menu()

