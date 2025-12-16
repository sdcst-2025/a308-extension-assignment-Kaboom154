'''Rock Paper Scissors
Create the classic "Rock, Paper Scissors Game".  It will keep playing until someone wins.
(5 points)
Extension:
Play the classic "Rock Paper Scissors Lizard Spock" game
'''
'''
scissors > paper
paper > rock
rock > lizard
lizard > spock
spock > scissors
scissors > lizard
lizard > paper
paper > spock
spock > rock
rock > scissors
'''
from random import randint
from os import system
from rich import print
def RPSLS():
    system("clear||cls")
    gameState = "tie"
    list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    wins = {
        'Scissors' : ['Paper', 'Lizard'],
        'Paper' : ['Rock', 'Spock'],
        'Rock' : ['Lizard', 'Scissors'],
        'Lizard' : ['Spock', 'Paper'],
        'Spock' : ['Scissors', 'Rock']
    }
    print("[yellow]Rock Paper Scissors Lizard Spock")
    while gameState == "tie":
        choice = (str(input("What do you play?\n"))).capitalize()
        compChoice = list[randint(0,4)]
        print(f'The computer chose {compChoice}')
        if choice != compChoice:
            gameState = 'not tie'
        if choice not in list:
            gameState = 'tie'
    winsVs = wins[choice]
    if compChoice in winsVs:
        print('You win !')
    else:
        print('You lose')
    playAgain = str(input('Would you like to play again [Y/n]\n'))
    if playAgain == 'Y' or playAgain =='y':
        RPSLS()

RPSLS()