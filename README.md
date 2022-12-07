# tic-tac-toe-with-python

Tic-tac-toe-with-python is a simple game meant to be played in a Python terminal, provided by Heroku.
Users of this game will play against the computer with the goal of lining up three of their marks/letters in a row, column or a diagonal way.

Live version link

## How to play
---
Tic-tac-toe-with-python is based on the original game of tic-tac-toe.
1. At first, the user is asked to enter a name that will be displayed throughout the game.
2. Then the game tells the user the instructions, and the marks/letters the user and the computer is assigned.
3. At this point the user will be asked if they want to start the game or quit.
4. If the user has decided to start the game, they will be asked to decide who makes the first move.
5. The game proceeds according to previous decision and asks both the computer and the user to make their move.
6. This process is repeated until there is a winner, or there are no empty spaces left on the board.
7. After the result is printed the user can decide if they want to play again, thus restarting the program.

## Flowchart of the program
---
## Features 
---
As listed in the How to play section:
* The starting screen shows the game title and asks the user to hit enter to play the game.
  * screenshot of starting screen

---
* Print the instructions of the game, inform the user what mark/letter they are assigned.
  * screenshot of instructions

---
* Feature to ask the player to decide on who is going to make the first move on the board.
  * screenshot of decision

---
* The game prints the reference board and tells the user which index on the board refers to which number that they can input.
  * screenshot of referenceboard

---
* The game will start based on the user's previous decision.
* The user and the computer are both asked to make a move until there is a winner, or there are no empty spaces left on the board.
* The computer makes it's move by random based on the remaining indices of the board.
* The user is asked to type in their move manually.
* The program is handling errors with informing the player if they have entered an invalid input.

Invalid inputs include:

* Strings (words or letters)
  * The user is asked to enter whole numbers only.
* Whitespaces or no input at all.
  * The user is asked to avoid entering empty string.
* Floating point numbers, negative numbers, or input that contains numbers and strings at the same time.
  * The user is told that they can not enter floats, negative numbers or strings.

If all of the above has been validated, the user input is converted into an integer, and then once again, the program checks for validation.

Further error handlings include:

* ValueError: Input referring to an index on the board that is not available.
  * The user is told that their desired spot has been taken.

* IndexError: Input is referring to an index that does not exist in the available moves
  * The user's input needs to be between 1 and 9
  * Input can not be 0
  * Input can not be over the number 9
---
* After the game ends with a result of win or a tie, the user is asked if they want to play again, or quit the game.

## Possible features to implement in the future

At this stage the computer is relatively easy to beat. The computer is not introduced to the rules of the game and only makes it's decision by choosing a random spot that is still available on the board. This means if the computer has 2 of their letters lined up and with their next move they would be able to win the game, the pattern does not get recognized and it is possible that the computer will miss their chance. The same goes for preventing the player from lining up their letters.

This makes it considerable to implement an AI to the program, that is able to recognize the outcomes of each possible move and prioritze their decision to win the game with the least moves required.

Feature to keep the entered name throughout the game without asking the user to input every time they want to play a new game.

Feature to let the player decide what letter they want to use. (The default is "X" for the player, and "O" for the computer.)

## Object Oriented Programming

## Technologies used
* Code Institute's python essentials template
* GitHub for version control
* GitPod for writing and testing the program manually.
* Heroku for deploying the project


## Imported libraries
* time and sys
  * to make a short delay in printing to the terminal to make it easier to read
* os 
  * to make a function that declutters the terminal when it becomes crammed
* random
  * to generate random choices for the computer during the game


# Testing and validation
## PEP8
 * Code Institute's PEP8 found no errors

## Manual
* All listed features have been tested thoroughly on several tries.

# Bugs and problems
## Solved
* After the player decided to play the game again, the program restarted but the board remained filled with the last game's entries, thus preventing to play the game properly. This was caused by a class instance that was created outside of the main game function.
* Quitting the game would not work properly, unless the right input was made. This was caused by the lack of input handling within the function. Adding an else statement solved it by continuing to ask for the correct input.
* Input handling did not accomodate for floating point numbers, and inputs that included both numbers and strings at the same time. Error for this message was handled as if it was a spot already taken on the board. Making the sure the input was a number with isdigit() method helped solving this.

## Unsolved 
* After hours of testing I have nout found any bugs left unfixed.

## Problems
* The ASCII art visible on the starting screen contains more than 79 characters in the file run.py.
* The IDE interpreted the "/" characters as escape sequences.
  * Wrapping the the characters in an r-string solved this problem.
  * The only problems with the code will remain related to the lines containing the ASCII art too long.

# Deployment

Deploying this page was made possible with the use of GitHub and Heroku with the following steps:
1. Create a new account on Heroku and connect it with my GitHub account.

# Credits
* Code Institute's python essentials template
* For implementing OOP and making the main logic of the game I have used: [12 Beginner Python Projects - Coding Course](https://youtu.be/8ext9G7xspg?t=2154)
* For the type_slow() and wipe() functions I have looked up solutions on [stackoverflow](https://stackoverflow.com/)
* For exception handling and list comprehension: [W3Schools](https://www.w3schools.com/)

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

fixed a bug where the game would start over on user input but the list was already updated and would not let the player enter valid entries. 