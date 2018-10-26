import random
from sklearn import tree
import numpy as np

# constants

schere = np.array([1, 0, 0])
stein = np.array([0, 1, 0])
papier = np.array([0, 0, 1])

toNumeric = {'schere':schere,
        'stein':stein,
        'papier':papier}

validTextInput = np.array(['schere', 'stein', 'papier', 'exit'])

possibleValues = np.array([schere, stein, papier])

# variables

model = tree.DecisionTreeClassifier()

userWon = np.array([])
userDid = np.array([])
pcDid = np.array([])

trainingSource = np.array([])
trainingTarget = np.array([])

userSays = ''
roundNumber = 0

def calculateWhatPcDoes():
    global pcDoes
    pcDoes = ''
    if (roundNumber < 3):
        pcDoes = possibleValues[random.randint(0, 2)]
    else:
        X = trainingSource[0:roundNumber - 2]
        Y = trainingTarget
        print("im tryin to fit ", X, " to ", Y)
        model.fit(X, Y)
        prediction = model.predict([trainingSource[roundNumber - 3]])
        print("I predict that you take: ", prediction)
        pcDoes = possibleValues[0]


def checkWhatUserDoes():
    global userSays, userDoes
    invalidInput = True
    while (invalidInput):
        userSays = input("Runde " + str(roundNumber + 1) + '. Was nimmst du? ').lower()
        if (userSays in validTextInput):
            if (userSays == 'exit'):
                break
            else:
                invalidInput = False
    userDoes = toNumeric[userSays]


def writeHistoryWhoWins():
    global userWon, userDid, pcDid
    userWon = np.hstack((userWon, userWin))
    if (userDid.size == 0):
        userDid = userDoes
        pcDid = pcDoes
    else:
        userDid = np.vstack((userDid, userDoes))
        pcDid = np.vstack((pcDid, pcDoes))


def printWinner():
    print(str(pcDoes) + '!')
    if (userWin == 1):
        print('Du gewinnst!')
    elif (userWin == 0):
        print('Du verlierst!')
    else:
        print('Unentschieden!')


def printHistory():
    print('------ HISTORY ------')
    for i in range(roundNumber + 1):
        print(
            'Runde ' + str(i + 1) + ': Du ' + str(userDid[i]) + ' ich ' + str(pcDid[i]) + ', Stand ' + str(userWon[i]))
    print('------ HISTORY END ------')


def collectTrainingData():
    global trainingSource, trainingTarget
    if (roundNumber >= 1):
        change = userDid[roundNumber] != userDid[roundNumber - 1]
        react = reacted(userDid[roundNumber], pcDid[roundNumber - 1])
        win = userWon[roundNumber]
        does = userDid[roundNumber]
        if (trainingSource.size == 0):
            trainingSource = np.array([change, react, win])
        else:
            trainingSource = np.vstack((trainingSource, np.array([change, react, win])))
        if (roundNumber >= 2):
            didNow = userDid[roundNumber]
            if (trainingTarget.size == 0):
                trainingTarget = np.array([didNow])
            else:
                trainingTarget = np.vstack((trainingTarget, didNow))


## helper functions

def wins(a, b):
    if(eq(a,b)):
        return 0.5
    if(eq(a, schere)):
        return eq(b,papier)
    if(eq(a,papier)):
        return eq(b,stein)
    if(eq(a,stein)):
        return eq(b,schere)
    print("error in algorithm")

def eq(a,b):
    return np.array_equal(a,b)

def reacted(a, b):
    return wins(a,b) == 1

def defeat(a):
    if(eq(a,schere)):
        return stein
    if(eq(a,stein)):
        return papier
    if(eq(a,papier)):
        return schere

while(userSays != 'exit'):
    calculateWhatPcDoes()
    checkWhatUserDoes()

    userWin = wins(userDoes, pcDoes)

    writeHistoryWhoWins()

    printWinner()

    printHistory()

    collectTrainingData()
        
    roundNumber += 1
