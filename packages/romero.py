import os  # For clearing the screen based on the OS

# ANSI escape sequences for colored terminal output
PINK = '\033[38;2;255;105;180m'  
RESET = '\033[0m'  

# Function to clear the screen depending on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  

# Function to print a bordered title box with centered text
def print_border(title):
    print(PINK + "╔" + "═" * 50 + "╗") 
    print(f"║{title:^50}║")            
    print("╚" + "═" * 50 + "╝" + RESET)  

# Main menu function
def romero_menu():
    while True:
        clear_screen()  
        print_border("WELCOME TO RAIN'S MENU") 

        # Menu options
        print(PINK + "1 - Basic Info")
        print("2 - Goals")
        print("3 - Comments from Other Aragon")
        print("4 - Comments from Lopez")
        print("5 - Comments from Dimayuga")
        print("6 - Comments from Lim")
        print("7 - Exit" + RESET)

        choice = input("\nChoose an option: ")

        clear_screen() 

        # Show selected content based on choice
        if choice == "1":
            print_border("BASIC INFORMATION")
            print(PINK + "Name     : Dianna Rain M. Romero")
            print("Age      : 19")
            print("Birthday : October 31, 2005")
            print("Gender   : Female")
            print("Program  : Bachelor of Science in Information Technology")
            print("Hobbies  : I love to sing, cook, and sleep." + RESET)

        elif choice == "2":
            print_border("GOALS")
            print(PINK + "My goal is to never stop learning, to grow through every challenge,"
            " and to live a life filled with curiosity, creativity, and purpose." )

        elif choice == "3":
            print_border("COMMENTS FROM OTHER TEAMMATES")
            print(PINK + "" + RESET)  # You can add actual comments here

        elif choice == "4":
            print_border("COMMENTS FROM LOPEZ")
            print(PINK + "" + RESET)

        elif choice == "5":
            print_border("COMMENTS FROM DIMAYUGA")
            print(PINK + "" + RESET)

        elif choice == "6":
            print_border("COMMENTS FROM LIM")
            print(PINK + "" + RESET)

        elif choice == "7":
            # Exit the menu and return to main program
            print(PINK + "\nThank you for using the menu. Goodbye!" + RESET )
            return 

        else:
            # Handle invalid inaput
            print(PINK + "Invalid choice. Please select a number between 1 and 7." + RESET)

        # Wait for the user to press Enter before showing the menu again
        input("\nPress Enter to return to the menu...")

# Run the menu if this file is executed directly
romero_menu()
