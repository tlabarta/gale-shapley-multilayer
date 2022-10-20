import GSmethods
from GSmethods import MarriageModel

n = 4

def main():
    profits = GSmethods.generateFeatures(n, "driver", 1)
    eta = GSmethods.generateFeatures(n, "passenger", 1)
    driver_gender = GSmethods.generateFeatures(n, "driver", 2)
    passenger_gender = GSmethods.generateFeatures(n, "driver", 2)
    driver_g_preferences = GSmethods.generatePreferences(n, "driver")
    passenger_g_preferences = GSmethods.generatePreferences(n, "passenger")

#Test Example: Remove if done
    #profits = {0: [0, 2, 3, 3], 1: [2, 3, 1, 1], 2: [2, 0, 3, 3], 3: [2, 1, 0, 1]}
    #eta = {0: [0.6, 0.5, 1.0, 0.8], 1: [1.0, 0.7, 0.5, 0.1], 2: [0.3, 0.7, 0.5, 0.5], 3: [1.0, 0.9, 0.2, 0.6]}

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

#Test Example: Remove if done
    # driver_l1 ={0: [1, 3, 2, 0], 1: [1, 3, 2, 0], 2: [3, 0, 2, 1], 3: [3, 2, 0, 1]}
    # driver_l2 = {0: [1, 3, 0, 2], 1: [0, 3, 2, 1], 2: [3, 1, 2, 0], 3: [1, 3, 2, 0]}
    # passenger_l1 = {0: [2, 0, 1, 3], 1: [1, 2, 0, 3], 2: [3, 0, 1, 2], 3: [3, 0, 1, 2]}
    # passenger_l2 = {0: [1, 3, 2, 0], 1: [1, 0, 3, 2], 2: [2, 3, 1, 0], 3: [1, 3, 2, 0]}

    print(f'L1 Driver Preference List: {driver_l1}')
    print(f'L1 Passenger Preference List: {passenger_l1}')
    print(f'L2 Driver Preference List: {driver_l2}')
    print(f'L2 Passenger Preference List: {passenger_l2}')

    layer1 = MarriageModel(driver_l1, passenger_l1)
    stable_match = layer1.Deferred_Acceptance()
    print("Stable Matching L1: " + str(stable_match))
    layer2 = MarriageModel(driver_l2, passenger_l2)
    print("Blocking Pair on L2: " + str(layer2.is_stable(stable_match)))
    if layer2.is_stable(stable_match) != True:
        no_blocking_pairs = int(len(layer2.is_stable(stable_match)) / 2)
        print("No. blocking pair: " + str(no_blocking_pairs))

    print(GSmethods.checkblockingpairs(stable_match,driver_l2, passenger_l2))
    print(GSmethods.sumprofit(stable_match, profits))
    print(GSmethods.sumeta(stable_match, eta))

main()
