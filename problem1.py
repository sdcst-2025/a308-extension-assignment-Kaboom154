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
import time

def diceRoll(type):
    statsList = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
    stats = {}
    for i in range(6):
        die1 = randint(1,6)
        die2 = randint(1,6)
        die3 = randint(1,6)
        die4 = randint(1,6)
        if type == 1:
            result = die1 + die2 + die3
            print(f'You rolled {die1}, {die2}, and {die3}')
            print(f'Which gives a total of {result} in {statsList[i]}')
            stats[statsList[i]] = result
            time.sleep(2)
        if type == 2:
            dice1 = [die1,die2,die3,die4]
            print(f'You rolled {dice1[0]}, {dice1[1]}, {dice1[2]}, and {dice1[3]}')
            dice1.sort()
            dice1.pop(0)
            result = dice1[0] + dice1[1] + dice1[2]
            print(f'Discarding the lowest roll gives {dice1[0]}, {dice1[1]}, and {dice1[2]}')
            print(f'Which gives a total of {result} in {statsList[i]}')
            stats[statsList[i]] = result
            time.sleep(2)
        if type == 3:
            print(f'You rolled {die1}, {die2}, and {die3}')
            if die1 == 1:
                die1 = randint(1,6)
            if die2 == 1:
                die2 = randint(1,6)
            if die3 == 1:
                die3 = randint(1,6)
            result = die1 + die2 + die3
            print(f'Rerolling ones gives {die1}, {die2}, and {die3}')
            print(f'Which gives a total of {result} in {statsList[i]}')
            stats[statsList[i]] = result
            time.sleep(2)
    print('Your character\'s stats are')
    print(stats)
    choice = input('Would you like to create another character? (Y/n)  ')
    if choice in ['Y','y']:
        dndRoll()

def define():
    print('''
    Standard roll -- rolls 3 dice and adds them to give your stats
    [white]4[/white]-dice roll -- rolls 4 dice and discards the lowest one
    Reroll ones -- rolls 3 dice and rerolls any that roll a 1 a single time''')
    choice = input('Continue? (Y/n)  ')
    if choice in ['Y','y']:
        dndRoll()
    else:
        define()

def dndRoll():
    system('clear||cls')
    print('[yellow]Would you like to use standard, 4-dice, or reroll ones to create your character?')
    print('''
    1 - Standard roll
    2 - [white]4[/white]-dice roll
    3 - Reroll ones
    4 - Definitions''')
    choice = str(input())
    if choice == '1':
        diceRoll(1)
    if choice == '2':
        diceRoll(2)
    if choice == '3':
        diceRoll(3)
    if choice == '4':
        define()
    if choice not in ['1','2','3','4']:
        dndRoll()

dndRoll()