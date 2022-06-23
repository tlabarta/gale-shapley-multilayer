import numpy as np
import random
import pandas as pd

n = 20


def generatePreferences(n, party, layer):
    preferences = {}

    for i in range(n):
        randomlist = []
        if layer == 1:
            if party == "driver":
                randomlist = random.sample(range(0, n), n)
            elif party == "passenger":
                randomlist = random.sample(range(0, n), n)
        elif layer == 2:
            randomlist = random.choices(range(0, 3), k=n)
        if party == "driver":
            preferences[i] = randomlist
        elif party == "passenger":
            preferences[i] = randomlist
    return preferences


driver_l1 = generatePreferences(n, "driver", 1)
driver_l2 = generatePreferences(n, "driver", 2)
passenger_l1 = generatePreferences(n, "passenger", 1)
passenger_l2 = generatePreferences(n, "passenger", 2)

driverPreferences = driver_l1
passengerPreferences = passenger_l1


def stableMatching(n, driverPreferences, passengerPreferences):
    # Initially, all n men are unmarried
    unmatched = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    driverMatch = [None] * n
    # None of the women has a spouse yet, we denote this by the value None
    passengerMatch = [None] * n
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextChoice = [0] * n

    # While there exists at least one unmarried man:
    while unmatched:
        # Pick an arbitrary unmarried man
        driver = unmatched[0]
        # Store his ranking in this variable for convenience
        dPreferences = driverPreferences[driver]
        # Find a woman to propose to
        passenger = dPreferences[nextChoice[driver]]
        # Store her ranking in this variable for convenience
        pPreferences = passengerPreferences[passenger]
        # Find the present husband of the selected woman (it might be None)
        currentMatch = passengerMatch[passenger]

        # Now "he" proposes to "she".
        # Decide whether "she" accepts, and update the following fields
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice
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
    return driverMatch


print(stableMatching(n, driverPreferences, passengerPreferences))