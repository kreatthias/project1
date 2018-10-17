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


winnings = []
userDid = []
pcDid = []
possibleValues = ['schere', 'stein', 'papier']
userDoes = ''
lastPC = possibleValues[random.randint(0,2)]
count = 0
while(userDoes != 'exit'):
    pcDoes = ''
    if (count == 0):
        pcDoes = possibleValues[random.randint(0,2)]
    else:
        #predict here!
        pcDoes = possibleValues[random.randint(0,0)]

    invalidInput = True
    while(invalidInput):
        userDoes = input("Runde " + str(count + 1) + '. Was nimmst du? ')
        if (userDoes in possibleValues):
            invalidInput = False
        elif (userDoes == 'exit'):
            break
    userWon = wins(userDoes, pcDoes)
    
    winnings.append(userWon)
    userDid.append(userDoes)
    pcDid.append(pcDoes)

    print(pcDoes + '!')
    if (userWon == 1):
        print('Du gewinnst!')
    elif (userWon == 0):
        print('Du verlierst!')
    else:
        print('Unentschieden!')

    count += 1
    
    print('------ HISTORY ------')
    for i in range(count):
        print('Runde ' + str(i) + ': Du ' + str(userDid[i]) + ' ich ' + str(pcDid[i]) + ', Stand ' + str(winnings[i])) 
    print('------ HISTORY END ------')
