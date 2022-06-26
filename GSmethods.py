import random

def generatePreferences(n, party, layer):
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
