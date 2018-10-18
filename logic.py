import os
import time
import random
from sklearn import tree
import numpy as np

schere = (1, 0, 0)
stein =  (0, 1, 0)
papier = (0, 0, 1)

toNumeric = {'schere':schere,
        'stein':stein,
        'papier':papier}

validInput = ['schere', 'stein', 'papier', 'exit']

def wins(a, b):
    if(a == b):
        return 0.5
    if(a == schere):
        return b == papier
    if(a == papier):
        return b == stein
    if(a == stein):
        return b == schere
    print("error in algorithm")

def reacted(a, b):
    return wins(a,b) == 1

model = tree.DecisionTreeClassifier()

userWon = []
userDid = []
pcDid = []
trainingSource = []
trainingTarget = []
possibleValues = [schere, stein, papier]
userDoes = ''
count = 0
while(userDoes != 'exit'):
    pcDoes = ''
    if (count < 3):
        pcDoes = possibleValues[random.randint(0,2)]
    else:
        X = trainingSource[0:count-2]
        Y = trainingTarget
        print(X, Y, count)
        model.fit(X, Y)
        prediction = model.predict([trainingSource[count-3]])
        print(prediction)
        pcDoes = possibleValues[random.randint(0,0)]

    invalidInput = True
    while(invalidInput):
        userSays = input("Runde " + str(count + 1) + '. Was nimmst du? ').lower()
        if (userSays in validInput):
            if (userSays == 'exit'):
                break
            else:
                invalidInput = False
    userDoes = toNumeric[userSays]
    userWin = wins(userDoes, pcDoes)
    
    userWon.append(userWin)
    userDid.append(userDoes)
    pcDid.append(pcDoes)

    print(str(pcDoes) + '!')
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

    if (count >= 1):
        change = userDid[count] != userDid[count-1]
        react = reacted(userDid[count], pcDid[count-1])
        win = userWon[count]
        does = userDid[count]
        trainingSource.append([change,react,win])
        if (count >=2):
            didNow = userDid[count]
            trainingTarget.append(didNow)
        
    count += 1
