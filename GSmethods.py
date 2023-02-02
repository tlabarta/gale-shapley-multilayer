import random
import numpy as np
import time
import pandas as pd
from scipy.optimize import linear_sum_assignment




def generateFeatures(n, party, layer):
    features = {}

    for i in range(n):
        randomlist = []
        if layer == 1:
            if party == "driver":
                randomlist = random.choices(range(1, 100), k=n)
            elif party == "passenger":
                randomlist = random.choices(range(1, 60),k=n)
            elif party == "waiting time":
                randomlist = random.choices(range(1, 30), k=n)
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

def calculatePreferences(preferences, features):
    preferences = preferences
    features = features
    preference_list = []
    result = {}

    for i in preferences:
        preference_list = []
        preference = preferences[i]
        for k in preference:
            for key,value in features.items():
                if k == value:
                    preference_list.append(key)
        result[i]=preference_list



    return result

def calculatePreferencesNumerical(features, category):

    initial = features
    x = len(features)
    results = {}

    for i in range(x):

        if category == 'Profit':
            sorted_features = sorted(initial[i], reverse=True)
        elif category == 'ETA':
            sorted_features = sorted(initial[i])

        indexlist =[]

        for k in sorted_features:
            if initial[i].index(k) not in indexlist:
                indexlist.append(initial[i].index(k))
            else:
                indexlist.append(initial[i].index(k, indexlist[-1]+1))

        results[i] = indexlist
    return results

def calculateWaitingTime(eta, waiting_time):
    initial = pd.DataFrame(eta)
    substr = pd.DataFrame(waiting_time)
    result = initial - substr
    result[result < 0] = 0
    result = result.to_dict('list')

    return result

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

def rearrange_order(preference_list, n):
    new_order = random.sample(range(0,n),n)
    rearranged_dict = {k: preference_list[k] for k in new_order}
    return rearranged_dict

def checkblockingpairs(matches: dict, driver_preferences: dict , passenger_preferences: dict, feature):
    x = matches
    x_inv = {v: k for k, v in x.items()}
    y = driver_preferences
    z = passenger_preferences
    z_val = feature
    blocking_pair_count = 0
    blocking_pair_list = []

    for key, value in x_inv.items():
        match_preferences = z[key]
        match_preference_index = match_preferences.index(value)

        if match_preference_index != 0:
            for i in range(match_preference_index-1, -1, -1):
                higher_preference = match_preferences[i]
                higher_preference_pref = y[higher_preference]
                key_preference_index = higher_preference_pref.index(key)
                higher_preference_match = x[higher_preference]
                higher_preference_match_ind = higher_preference_pref.index(higher_preference_match)
                if isinstance(z_val[higher_preference], list):
                    higher_pref_value = z_val[key][higher_preference]
                    match_value = z_val[key][value]
                else:
                    higher_pref_value = z_val[higher_preference]
                    match_value = z_val[value]
                if key_preference_index < higher_preference_match_ind and higher_pref_value != match_value:
                    blocking_pair_count +=1
                    blocking_pair_list.append([key, higher_preference])

    #print(blocking_pair_list)
    return blocking_pair_count


def sumprofit(matches: dict, profits: dict) -> int:
    sum_profit = 0
    x = matches
    y = profits

    for key, value in x.items():
        match_profits_all = y[key]
        match_profit = match_profits_all[value]
        sum_profit = sum_profit + match_profit
    return sum_profit

def sumeta(matches: dict, eta: dict) -> float:
    sum_eta = 0.0
    x = matches
    y = eta

    for key, value in x.items():
        match_eta_all = y[key]
        match_eta = match_eta_all[value]
        sum_eta = sum_eta + match_eta
    return round(sum_eta,2)

def minmaxresult(matches: dict, l1_features: dict, Min_Max: str):
    x = matches
    y = l1_features
    match = []

    for key, value in x.items():
        match_all = y[key]
        match.append(match_all[value])

    if Min_Max == 'Min':
        result = min(match)
    elif Min_Max == 'Max':
        result = max(match)

    return result

#to be removed
# def minmaxall(l1_features: dict, Min_Max: str):
#     y = l1_features
#     results = []
#
#     for key, value in y.items():
#         if Min_Max == 'Min':
#             results.append(min(value))
#         elif Min_Max == 'Max':
#             results.append(max(value))
#
#     sum_results = sum(results)
#
#     return sum_results

def minmaxweightmatching(l1_features,Min_Max):
    y = np.array(list(l1_features.values()))^

    if Min_Max == 'Min':
        row_ind, col_ind = linear_sum_assignment(y)
    elif Min_Max == 'Max':
        row_ind, col_ind = linear_sum_assignment(-y)

    result = y[row_ind, col_ind].sum()
    return result
