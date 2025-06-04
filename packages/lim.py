from rich.panel import Panel 
from rich.align import Align
from rich import print
import os

# Clears the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Displays the menu options 
def menu_choices():
    # Displayed inside a panel
    print(Align.center("[bold deep_sky_blue1]⊹₊ Good Day! "
    "I am Grace Anne Lim ⊹₊[/bold deep_sky_blue1]"))
    print(Align.center(Panel("[bold light_cyan1][1] "
    "Basic Info[/bold light_cyan1]")))
    print(Align.center(Panel("[bold light_cyan1][2] "
    "Goals[/bold light_cyan1]")))
    print(Align.center(Panel("[bold light_cyan1][3] "
    "Comment from Aragon[/bold light_cyan1]")))
    print(Align.center(Panel("[bold light_cyan1][4] "
    "Comment from Dimayuga[/bold light_cyan1]")))
    print(Align.center(Panel("[bold light_cyan1][5] "
    "Comment from Lopez[/bold light_cyan1]")))
    print(Align.center(Panel("[bold light_cyan1][6] "
    "Comment from Romero[/bold light_cyan1]")))
    print(Align.center(Panel("[bold light_cyan1][7] "
    "Exit[/bold light_cyan1]")))
    print()
    print(Align.center("[bold deep_sky_blue1]" \
    "Choose an option: [/bold deep_sky_blue1]"))

def display_basic_info():
    print(Align.center(Panel(
        "[bold deep_sky_blue1]Name     : [bold light_cyan1]"
        "Grace Anne Lim"
        "[bold deep_sky_blue1]\nAge      : [bold light_cyan1]"
        "20 years old"
        "[bold deep_sky_blue1]\nBirthday : [bold light_cyan1]"
        "March 21, 2005"
        "[bold deep_sky_blue1]\nGender   : [bold light_cyan1]"
        "Female"
        "[bold deep_sky_blue1]\nProgram  : [bold light_cyan1]"
        "Bachelor of Science in Information Technology"
        "[bold deep_sky_blue1]\nHobbies  : [bold light_cyan1]"
        "My hobbies include dance and graphic design.",
        title="[italic deep_sky_blue1]Basic Info",
        )))   
    
def display_goals():
    print(Align.center(Panel(
        "[bold light_cyan1]I aspire to live a successful and "
        "fulfilling life, striving for financial stability, mental "
        "well-being, personal growth, and a sense of purpose in "
        "everything I do.[bold light_cyan1]",                 
        title="[italic deep_sky_blue1]Goals",
        )))            

def comment_aragon():
    print(Align.center(Panel("[bold light_cyan1] A team player! Thank you for"
                            " always being ready to help. ",
                            title="[italic deep_sky_blue1]Comment from Aragon",
                            )))   
    
def comment_dimayuga():
    print(Align.center(Panel("[bold light_cyan1]You make working on this "
                             "project actually fun.",
                        title="[italic deep_sky_blue1]Comment from Dimayuga",
                        )))
    
def comment_lopez():
    print(Align.center(Panel("[bold light_cyan1]A great programmer! "
                             "I have always liked your style and aesthetic.",
                        title="[italic deep_sky_blue1]Comment from Lopez",
                        )))

def comment_romero():
    print(Align.center(Panel("[bold light_cyan1]Your creativity really " 
                            "stands out — you bring such unique " \
                            "ideas every time!",
                            title="[italic deep_sky_blue1]Comment from Romero",
                            ))) 

def display_lim_menu():
    while True:
        clear_screen()
        menu_choices()

        user_choice = input()

        if user_choice == "1":
            display_basic_info()    
        elif user_choice == "2":
            display_goals()            
        elif user_choice == "3":
            comment_aragon()     
        elif user_choice == "4":
            comment_dimayuga()  
        elif user_choice == "5":
            comment_lopez()            
        elif user_choice == "6":
            comment_romero()           
        elif user_choice == "7":
            clear_screen()
            print(Align.center("[italic deep_sky_blue1] "
                               "Thank you, Goodbye! ༄"))  
            break
        else:
            print(Align.center("[bold deep_pink3]"
            "Invalid choice. Select from 1 to 3 only."))
            
        input()
        return