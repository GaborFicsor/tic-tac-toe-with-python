import os
import time
import sys


running = True


def quit(user_input):
    """
    The program quits if the user types in "q" as user input
    """
    if user_input == "q" or user_input == "Q":
        type("thanks for playing")
        return True
    else:
        return False


def type(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


def menu():
    """ This is a docstring """
    ascii = ("""
 ______   __     ______        ______   ______     ______        ______   ______     ______    
/\__  _\ /\ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\   
\/_/\ \/ \ \ \  \ \ \____     \/_/\ \/ \ \  __ \  \ \ \____     \/_/\ \/ \ \ \/\ \  \ \  __\   
   \ \_\  \ \_\  \ \_____\       \ \_\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\ 
    \/_/   \/_/   \/_____/        \/_/   \/_/\/_/   \/_____/        \/_/   \/_____/   \/_____/
    """)
    print('')
    print(ascii)
    type("Welcome to tic-tac-toe")
    print('')
    name = input("Please enter your name: ")
    print('')
    print(f"Welcome {name}!\n\nEnter 's' to start the game or 'q' to quit!")
    user_input = input().lower()
    if user_input == "s":
        type("Game is starting...")
        time.sleep(1)
        os.system("cls")
        os.system("clear")
    elif user_input == "q":
        quit(user_input)


def main():
    while running:
        menu()
        if quit:
            break
        else:
            False


main()
