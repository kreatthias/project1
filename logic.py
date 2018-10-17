import os
import time
import random
from sklearn import tree

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

def reacted(a, b):
    return wins(a,b) == 1

model = tree.DecisionTreeClassifier()

userWon = []
userDid = []
pcDid = []
trainingSource = [] 
trainingTarget = []
possibleValues = ['schere', 'stein', 'papier']
userDoes = ''
count = 0
while(userDoes != 'exit'):
    pcDoes = ''
    if (count == 0):
        pcDoes = possibleValues[random.randint(0,2)]
    else:
        #predict here!
        #model.fit(trainingSource, trainingTarget)
        
        pcDoes = possibleValues[random.randint(0,0)]


    invalidInput = True
    while(invalidInput):
        userDoes = input("Runde " + str(count + 1) + '. Was nimmst du? ')
        if (userDoes in possibleValues):
            invalidInput = False
        elif (userDoes == 'exit'):
            break
    userWin = wins(userDoes, pcDoes)
    
    userWon.append(userWin)
    userDid.append(userDoes)
    pcDid.append(pcDoes)

    print(pcDoes + '!')
    if (userWin == 1):
        print('Du gewinnst!')
    elif (userWin == 0):
        print('Du verlierst!')
    else:
        print('Unentschieden!')

    print('------ HISTORY ------')
    for i in range(count+1):
        print('Runde ' + str(i + 1) + ': Du ' + str(userDid[i]) + ' ich ' + str(pcDid[i]) + ', Stand ' + str(userWon[i])) 
    print('------ HISTORY END ------')

    if (count != 0):
        change = userDid[count] != userDid[count-1]
        react = reacted(userDid[count], pcDid[count-1])
        winBefore = userWon[count-1]
        didBefore = userDid[count-1]
        didNow = userDid[count]
        trainingSource.append([[change],[react],[winBefore],[didBefore]])
        trainingTarget.append(didNow)
        print('Entering prediction mode:')
        print(trainingSource)
        print(trainingTarget)
    count += 1
