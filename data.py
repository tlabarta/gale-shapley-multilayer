import pandas as pd
import GSmethods
from GSmethods import MarriageModel


def run(n):

    results = pd.DataFrame()

    profits = GSmethods.generateFeatures(n, "driver", 1)
    eta = GSmethods.generateFeatures(n, "passenger", 1)
    driver_gender = GSmethods.generateFeatures(n, "driver", 2)
    passenger_gender = GSmethods.generateFeatures(n, "driver", 2)
    driver_g_preferences = GSmethods.generatePreferences(n, "driver")
    passenger_g_preferences = GSmethods.generatePreferences(n, "passenger")

    driver_l1 = GSmethods.calculatePreferences(n, "driver", 1)
    driver_l2 = GSmethods.calculatePreferences(n, "driver", 2)
    passenger_l1 = GSmethods.calculatePreferences(n, "passenger", 1)
    passenger_l2 = GSmethods.calculatePreferences(n, "passenger", 2)

    layer1 = MarriageModel(driver_l1, passenger_l1)
    stable_match_l1 = layer1.Deferred_Acceptance()

    layer2 = MarriageModel(driver_l2, passenger_l2)
    stable_match_l2 = layer2.Deferred_Acceptance()
    alg1 = ['ALG1', GSmethods.checkblockingpairs(stable_match_l1,driver_l2, passenger_l2), GSmethods.sumprofit(stable_match_l1, profits), GSmethods.sumeta(stable_match_l1, eta)]
    results.append(alg1)

    alg2 = ['ALG2', GSmethods.checkblockingpairs(stable_match_l2,driver_l1, passenger_l1), GSmethods.sumprofit(stable_match_l2, profits), GSmethods.sumeta(stable_match_l2, eta)]
    results.append(alg2)
