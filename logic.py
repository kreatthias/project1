import os
import time
import random

def wins(a, b):
    if (a == b):
        return 0.5
    if(a == 'schere'):
        return b == 'papier'
    if(a == 'papier'):
        return b == 'stein'
    if(a == 'stein'):
        return b == 'schere'
    print("error in algorithm")

possibleValues = ['schere', 'stein', 'papier']
ipt = ''
lastHuman = ''
lastPC = possibleValues[random.randint(0,2)]
count = 0
while(ipt != 'exit'):
    count += 1
    invalidInput = True
    while(invalidInput):
        ipt = input("Runde " + str(count) + '. Was nimmst du? ')
        if (ipt in possibleValues):
            invalidInput = False
    lastHuman = ipt
    userWon = wins(lastHuman, lastPC)
    print(lastPC + '!')
    if (userWon == 1):
        print('Du gewinnst!')
    elif (userWon == 0):
        print('Du verlierst!')
    else:
        print('Unentschieden!')
