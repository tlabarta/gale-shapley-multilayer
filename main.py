import GSmethods
from GSmethods import MarriageModel

n = 5

def main():
    profits = GSmethods.generateFeatures(n, "driver", 1)
    eta = GSmethods.generateFeatures(n, "passenger", 1)
    driver_gender = GSmethods.generateFeatures(n, "driver", 2)
    passenger_gender = GSmethods.generateFeatures(n, "driver", 2)
    driver_g_preferences = GSmethods.generatePreferences(n, "driver")
    passenger_g_preferences = GSmethods.generatePreferences(n, "passenger")

    print("L1 Profits: " + str(profits))
    print("L1 ETA: " + str(eta))

    print("L2 Driver Preferences: " + str(driver_g_preferences))
    print("L2 Driver Gender: " + str(driver_gender))
    print("L2 Driver Preferences: " + str(passenger_g_preferences))
    print("L2 Passenger Gender: " + str(passenger_gender))



    driver_l1 = GSmethods.calculatePreferences(n, "driver", 1)
    driver_l2 = GSmethods.calculatePreferences(n, "driver", 2)
    passenger_l1 = GSmethods.calculatePreferences(n, "passenger", 1)
    passenger_l2 = GSmethods.calculatePreferences(n, "passenger", 2)



    layer1 = MarriageModel(driver_l1, passenger_l1)
    stable_match = layer1.Deferred_Acceptance()
    print("Stable Matching L1: " + str(stable_match))
    layer2 = MarriageModel(driver_l2, passenger_l2)
    print("Blocking Pair on L2: " + str(layer2.is_stable(stable_match)))
    if layer2.is_stable(stable_match) != True:
        no_blocking_pairs = int(len(layer2.is_stable(stable_match)) / 2)
        print("No. blocking pair: " + str(no_blocking_pairs))

main()
