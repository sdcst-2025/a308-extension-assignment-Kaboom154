'''
##### Problem 2
Create a list that contains a deck of cards.
Shuffle and deal 5 card hands to 2 different players.  You may want to make use of the list commands we have previously explored to remove cards when they have been dealt to players.
'''

import random


cards = ['ks','kh','kd','kc','qs','qh','qd','qc','js','jh','jd','jc','10s','10h','10d','10c','9s','9h','9d','9c','8s','8h','8d','8c','7s','7h','7d','7c','6s','6h','6d','6c','5s','5h','5d','5c','4s','4h','4d','4c','3s','3h','3d','3c','2s','2h','2d','2c','1s','1h','1d','1c']
random.shuffle(cards)

#print(cards)

player1 = []
player2 = []

for i in range(5):
    player1.append(cards[0])
    cards.pop(0)
    player2.append(cards[0])
    cards.pop(0)

#print(cards)

print('p1:',player1)
print('p2:',player2)
