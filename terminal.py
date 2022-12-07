def main():
    """
    This function is called first, when the program starts running.
    Prints out game title and asks for user input to either
    proceed to playing or quit the game
    """
    ascii_title = (r"""
    __  .__                   __                            __
  _/  |_|__| ____           _/  |______    ____           _/  |_  ____   ____
  \   __\  |/ ___\   ______ \   __\__  \ _/ ___\   ______ \   __\/  _ \_/ __ \
   |  | |  \  \___  /_____/  |  |  / __ \\  \___  /_____/  |  | (  <_> )  ___/
   |__| |__|\___  >          |__| (____  /\___  >          |__|  \____/ \___  >
                \/                     \/     \/                            \/
""")
    print('')
    print(ascii_title)
    print("Welcome to tic-tac-toe!".center(80))
    print('')
    print("press enter to start the game".center(80))
    while True:
        user_input = input().lower()
        if user_input == "":
            print("Game is starting...")
            break
        elif user_input != "":
            print("Press enter to start the game...")

main()