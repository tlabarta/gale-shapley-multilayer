import GSmethods
from GaleShapley import MarriageModel

n = 4

def main():
    driver_l1 = GSmethods.generatePreferences(n, "driver", 1)
    driver_l2 = GSmethods.generatePreferences(n, "driver", 2)
    passenger_l1 = GSmethods.generatePreferences(n, "passenger", 1)
    passenger_l2 = GSmethods.generatePreferences(n, "passenger", 2)


    print(GSmethods.stableMatching(n, driver_l1, passenger_l1))

    layer1 = MarriageModel(driver_l1, passenger_l1)
    stable_match = layer1.Deferred_Acceptance()
    print(stable_match)

    layer2 = MarriageModel(driver_l2, passenger_l2)
    print(layer2.is_stable(stable_match))
    if layer2.is_stable(stable_match) != True:
        no_blocking_pairs = int(len(layer2.is_stable(stable_match)) / 2)
        print(no_blocking_pairs)

main()
