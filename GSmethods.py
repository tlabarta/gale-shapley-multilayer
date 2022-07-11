import random
import numpy as np


#Add additional Profit ranges to generateFeatures
# [1, 100], [25, 75], [1, 25] --> assumption is that number of stable matchings (on both layers) inceases, if the profit range is lower

def generateFeatures(n, party, layer):
    features = {}

    for i in range(n):
        randomlist = []
        if layer == 1:
            if party == "driver":
                randomlist = random.choices(range(0, n), k=n) # --> Change to range between 5 to 100€
            elif party == "passenger":
                randomlist = random.choices(np.linspace(0,1.0,11),k=n)
        elif layer == 2:
            if party == "driver":
                randomlist = str(random.randint(0, 2))
                randomlist = randomlist.replace('0', 'f').replace('1', 'm').replace('2', 'd')
            elif party == "passenger":
                randomlist = str(random.randint(0, 2))
                randomlist = randomlist.replace('0', 'f').replace('1', 'm').replace('2', 'd')

        features[i] = randomlist
    return features

def generatePreferences(n, party):
    gpreferences = {}

    for i in range(n):
        randomlist = random.sample(range(0, 3), 3)
        randomlist = [str(x) for x in randomlist]
        randomlist = [x.replace('0', 'f').replace('1', 'm').replace('2', 'd') for x in randomlist]
        gpreferences[i] = randomlist
    return gpreferences

def calculatePreferences(n, party, layer):
    preferences = {}

    for i in range(n):
        randomlist = []
        if layer == 1:
            if party == "driver":
                randomlist = random.sample(range(0, n), n)
                #randomlist = ["p" + str(val) for val in randomlist] -> Use to add prefix for value
            elif party == "passenger":
                randomlist = random.sample(range(0, n), n)
                #randomlist = ["d" + str(val) for val in randomlist] -> Use to add prefix for value
        elif layer == 2:
            if party == "driver":
                randomlist = random.sample(range(0, n), n)
                #randomlist = ["p" + str(val) for val in randomlist] -> Use to add prefix for value
            elif party == "passenger":
                randomlist = random.sample(range(0, n), n)
                #randomlist = ["d" + str(val) for val in randomlist] -> Use to add prefix for value
        if party == "driver":
            preferences[i] = randomlist
            #preferences["d" + str(i)] = preferences.pop(i) -> Use to add prefix for key
        elif party == "passenger":
            preferences[i] = randomlist
            #preferences["p" + str(i)] = preferences.pop(i) -> Use to add prefix for key

    return preferences

def calculatePreferencesNumerical(n, features):
    features = features

    for i in range(n):
        features[i].sort(reverse=True)
        indexlist =[]
        for k in range(len(features[i])):
            indexlist.append(features[i].index(k))
        print(indexlist)
    return features



def stableMatching(n, driverPreferences, passengerPreferences):
    unmatched = list(driverPreferences.keys())
    driverID = {f"driver{key}": val for key, val in driverPreferences.items()}
    driverID = list(driverID.keys())
    driverMatch = [None] * n
    passengerMatch = [None] * n
    nextChoice = [0] * n

    while unmatched:

        driver = unmatched[0]
        dPreferences = driverPreferences[driver]
        passenger = dPreferences[nextChoice[driver]]
        pPreferences = passengerPreferences[passenger]
        currentMatch = passengerMatch[passenger]

        if currentMatch == None:
            passengerMatch[passenger] = driver
            driverMatch[driver] = passenger
            nextChoice[driver] = nextChoice[driver] + 1
            unmatched.pop(0)
        else:
            currentIndex = pPreferences.index(currentMatch)
            hisIndex = pPreferences.index(driver)
            if currentIndex > hisIndex:
                passengerMatch[passenger] = driver
                driverMatch[driver] = passenger
                nextChoice[driver] = nextChoice[driver] + 1
                unmatched.pop(0)
                unmatched.insert(0, currentMatch)
            else:
                nextChoice[driver] = nextChoice[driver] + 1

    driverMatch = dict(zip(list(driverPreferences.keys()), driverMatch)) # -> change driverPreferences to DriverID if prefix wanted
    return driverMatch
