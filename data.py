import pandas as pd
import GSmethods
from GSmethods import MarriageModel
import random


def run(n):

    results = []

    profits = GSmethods.generateFeatures(n, "driver", 1)
    eta = GSmethods.generateFeatures(n, "passenger", 1)
    driver_gender = GSmethods.generateFeatures(n, "driver", 2)
    passenger_gender = GSmethods.generateFeatures(n, "driver", 2)
    driver_g_preferences = GSmethods.generatePreferences(n, "driver")
    passenger_g_preferences = GSmethods.generatePreferences(n, "passenger")


    driver_l1 = GSmethods.calculatePreferencesNumerical(profits, 'Profit')
    driver_l2 = GSmethods.calculatePreferences(driver_g_preferences, passenger_gender)
    passenger_l1 = GSmethods.calculatePreferencesNumerical(profits, 'ETA')
    passenger_l2 = GSmethods.calculatePreferences(passenger_g_preferences, driver_gender)

    #Done:
    #1. Random Feature Generation
    #2. Generating Preferences based on the random features
    #3. Find stable matchings for given preference list (0:... to n:...)
    #4. Calculate blocking pairs on other layer
    #5. Summarize and visualize results
    #6. Loop to run for n passengers/drivers and i iterations
    #7. Shuffle dictionary order randomly

    #To-DO:
    #Implement shuffling in stable matching runs.
    #Select Min and Max Profit + ETA



    layer1 = MarriageModel(driver_l1, passenger_l1)
    stable_match_l1 = layer1.Deferred_Acceptance()

    layer2 = MarriageModel(driver_l2, passenger_l2)
    stable_match_l2 = layer2.Deferred_Acceptance()
    alg1 = [
        'ALG1',
        GSmethods.checkblockingpairs(stable_match_l1,driver_l2, passenger_l2),
        GSmethods.sumprofit(stable_match_l1, profits),
        GSmethods.sumeta(stable_match_l1, eta),
        GSmethods.minmaxresult(stable_match_l1, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1, profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1, eta, 'Max')
    ]
    results.append(alg1)

    alg2 = [
        'ALG2',
        GSmethods.checkblockingpairs(stable_match_l2,driver_l1, passenger_l1),
        GSmethods.sumprofit(stable_match_l2, profits),
        GSmethods.sumeta(stable_match_l2, eta),
        GSmethods.minmaxresult(stable_match_l2, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2, profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2, eta, 'Max')
    ]
    results.append(alg2)

    return results
