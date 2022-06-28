import GSmethods
from GaleShapley import MarriageModel

n = 5

def main():
    profits = GSmethods.generateFeatures(n, "driver", 1)
    eta = GSmethods.generateFeatures(n, "passenger", 1)
    driver_gender = GSmethods.generateFeatures(n, "driver", 2)
    passenger_gender = GSmethods.generateFeatures(n, "driver", 2)
    driver_g_preferences = GSmethods.generatePreferences(n, "driver")
    passenger_g_preferences = GSmethods.generatePreferences(n, "passenger")

    print(profits)
    #print(eta)

    #print(GSmethods.calculatePreferencesNumerical(n, profits))

    # print(driver_g_preferences)
    # print(passenger_gender)
    # print(passenger_g_preferences)
    # print(driver_gender)

    driver_l1 = GSmethods.calculatePreferences(n, "driver", 1)
    driver_l2 = GSmethods.calculatePreferences(n, "driver", 2)
    passenger_l1 = GSmethods.calculatePreferences(n, "passenger", 1)
    passenger_l2 = GSmethods.calculatePreferences(n, "passenger", 2)




    # print(GSmethods.stableMatching(n, driver_l1, passenger_l1))
    #
    layer1 = MarriageModel(driver_l1, passenger_l1)
    stable_match = layer1.Deferred_Acceptance()
    print(stable_match)
    layer2 = MarriageModel(driver_l2, passenger_l2)
    print(layer2.is_stable(stable_match))
    if layer2.is_stable(stable_match) != True:
        no_blocking_pairs = int(len(layer2.is_stable(stable_match)) / 2)
        print(no_blocking_pairs)

main()
