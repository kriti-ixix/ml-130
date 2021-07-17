import random as r

player1 = input("Enter first player's name: ")
#player2 = input("Enter second player's name: ")
player2 = "Computer"

turn1 = input("First player's turn: ")
#turn2 = input("Second player's turn: ")
turn2 = r.choice(['paper', 'scissor', 'stone'])
print("Computer chose:", turn2)

'''
paper/scissor/stone
'''

#First player wins
if (turn1 == 'paper' and turn2 == 'stone') or (turn1 == 'scissor' and turn2 == 'paper') or (turn1 == 'stone' and turn2 == 'scissor'):
    print("The winner is", player1)

#Second player wins
elif (turn2 == 'paper' and turn1 == 'stone') or (turn2 == 'scissor' and turn1 == 'paper') or (turn2 == 'stone' and turn1 == 'scissor'):
    print("The winner is", player2)

else:
    print("Draw")