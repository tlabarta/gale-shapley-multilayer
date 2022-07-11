import GSmethods

n = 20

def main():
    driver_l1 = GSmethods.generatePreferences(n, "driver", 1)
    driver_l2 = GSmethods.generatePreferences(n, "driver", 2)
    passenger_l1 = GSmethods.generatePreferences(n, "passenger", 1)
    passenger_l2 = GSmethods.generatePreferences(n, "passenger", 2)

    print(GSmethods.stableMatching(n, driver_l1, passenger_l1))
    #print(GSmethods.stableMatching(n, driver_l2, passenger_l2))


main()
