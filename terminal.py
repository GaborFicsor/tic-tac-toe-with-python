def menu():
    """
    This function is called first, when the program starts running.
    Prints out game title and asks for user input to either 
    proceed to playing or quit the game
    """
    ascii = ("""
 ______   __     ______        ______   ______     ______        ______   ______     ______    
/\__  _\ /\ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\   
\/_/\ \/ \ \ \  \ \ \____     \/_/\ \/ \ \  __ \  \ \ \____     \/_/\ \/ \ \ \/\ \  \ \  __\   
   \ \_\  \ \_\  \ \_____\       \ \_\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\ 
    \/_/   \/_/   \/_____/        \/_/   \/_/\/_/   \/_____/        \/_/   \/_____/   \/_____/
    """)
    print('')
    print(ascii)
    print("Welcome to tic-tac-toe")
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
        play(t, x_player, o_player, print_game=True)
       

 while game.current_winner:
            answer = str(input('Run again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
            if answer == 'y':
                print("loop breaks")
            else:
                print("Goodbye")

 if game.current_winner:
                # triggers if a value was assigned by winner()
                # returns the letter of the winner
                # ends the game loop
                if print_game:
                    print(letter + ' wins!')
                return letter
                # print_game = False
                # play_again()