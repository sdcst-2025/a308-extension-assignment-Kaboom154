'''
##### Problem 1
Advanced Dungeons and Dragons
optional rolling systems include:
a) roll 4 dice, discard the lowest
b) roll 3 dice, reroll 1's.
Add these as options to your D&D Character Statistics Generator
'''
'''
Dungeons and Dragons Character Generator
In Dungeons and Dragons, players roll 3 dice to generate statistics for their characters.  The statistics recorded are:
strength
intelligence
wisdom
dexterity
constitution
charisma
Create a character generator that generates a character's statistics.
Once they have generated the result and it has been displayed, ask the user if they want to create another character.
(3 points)
'''
from random import randint
from os import system
from rich import print

def dice(type):
    die1 = randint(1,7)
    die2 = randint(1,7)
    die3 = randint(1,7)
    die4 = randint(1,7)
    if type == 1:
        result = die1 + die2 + die3
        print(f'you rolled {die1}, {die2}, and {die3}')
    if type == 2:
        dice2 = [die1,die2,die3,die4]
        dice2.sort()
        dice2.pop(0)
        result = dice2[0] + dice2[1] + dice2[2]
        print(f'you rolled {dice2[0]},')

def dndRoll():
    #system('clear||cls')
    print('[yellow]Would you like to use standard, 4-dice, or reroll ones to create your character?')
    print('''
    1 - standard roll
    2 - [white]4[/white]-dice roll
    3 - reroll ones
    4 - definitions''')
    choice = str(input())
    if choice == '1':
        dice(1)
    if choice == '2':
        dice(2)
    if choice == '3':
        dice(3)
    if choice == '4':
        define()
    else:
        dndRoll()

dndRoll()