import GSmethods


def run(n):
    results = []

    profits = GSmethods.generateFeatures(n, "driver", 1)
    eta = GSmethods.generateFeatures(n, "passenger", 1)
    driver_gender = GSmethods.generateFeatures(n, "driver", 2)
    passenger_gender = GSmethods.generateFeatures(n, "passenger", 2)
    driver_g_preferences = GSmethods.generatePreferences(n, "driver")
    passenger_g_preferences = GSmethods.generatePreferences(n, "passenger")

    driver_l1 = GSmethods.calculatePreferencesNumerical(profits, 'Profit')
    driver_l2 = GSmethods.calculatePreferences(driver_g_preferences, passenger_gender)
    passenger_l1 = GSmethods.calculatePreferencesNumerical(eta, 'ETA')
    passenger_l2 = GSmethods.calculatePreferences(passenger_g_preferences, driver_gender)

    stable_match_l1_d = GSmethods.stableMatching(n, driver_l1, passenger_l1)
    stable_match_l2_d = GSmethods.stableMatching(n, driver_l2, passenger_l2)

    alg1_d = [
        'ALG1',
        'Driver-optimal',
        GSmethods.checkblockingpairs(stable_match_l1_d, driver_l2, passenger_l2),
        GSmethods.sumprofit(stable_match_l1_d, profits),
        GSmethods.sumeta(stable_match_l1_d, eta),
        GSmethods.minmaxall(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1_d, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d, profits, 'Max'),
        GSmethods.minmaxall(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d, eta, 'Max')
    ]
    results.append(alg1_d)

    alg2_d = [
        'ALG2',
        'Driver-optimal',
        GSmethods.checkblockingpairs(stable_match_l2_d, driver_l1, passenger_l1),
        GSmethods.sumprofit(stable_match_l2_d, profits),
        GSmethods.sumeta(stable_match_l2_d, eta),
        GSmethods.minmaxall(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2_d, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d, profits, 'Max'),
        GSmethods.minmaxall(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d, eta, 'Max')
    ]
    results.append(alg2_d)

    stable_match_l1_p = GSmethods.stableMatching(n, passenger_l1, driver_l1)
    stable_match_l1_p = {y: x for x, y in stable_match_l1_p.items()}

    stable_match_l2_p = GSmethods.stableMatching(n, passenger_l2, driver_l2)
    stable_match_l2_p = {y: x for x, y in stable_match_l2_p.items()}

    alg1_p = [
        'ALG1',
        'Passenger-optimal',
        GSmethods.checkblockingpairs(stable_match_l1_p, driver_l2, passenger_l2),
        GSmethods.sumprofit(stable_match_l1_p, profits),
        GSmethods.sumeta(stable_match_l1_p, eta),
        GSmethods.minmaxall(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1_p, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p, profits, 'Max'),
        GSmethods.minmaxall(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p, eta, 'Max')
    ]
    results.append(alg1_p)

    alg2_p = [
        'ALG2',
        'Passenger-optimal',
        GSmethods.checkblockingpairs(stable_match_l2_p, driver_l1, passenger_l1),
        GSmethods.sumprofit(stable_match_l2_p, profits),
        GSmethods.sumeta(stable_match_l2_p, eta),
        GSmethods.minmaxall(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2_p, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p, profits, 'Max'),
        GSmethods.minmaxall(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p, eta, 'Max')
    ]
    results.append(alg2_p)

    return results


def shuffle_run(n, i):
    results = []

    profits = GSmethods.generateFeatures(n, "driver", 1)
    eta = GSmethods.generateFeatures(n, "passenger", 1)
    driver_gender = GSmethods.generateFeatures(n, "driver", 2)
    passenger_gender = GSmethods.generateFeatures(n, "passenger", 2)
    driver_g_preferences = GSmethods.generatePreferences(n, "driver")
    passenger_g_preferences = GSmethods.generatePreferences(n, "passenger")

    driver_l1 = GSmethods.calculatePreferencesNumerical(profits, 'Profit')
    driver_l2 = GSmethods.calculatePreferences(driver_g_preferences, passenger_gender)
    passenger_l1 = GSmethods.calculatePreferencesNumerical(eta, 'ETA')
    passenger_l2 = GSmethods.calculatePreferences(passenger_g_preferences, driver_gender)

    for k in range(i):
        driver_l1 = GSmethods.rearrange_order(driver_l1, n)
        driver_l2 = GSmethods.rearrange_order(driver_l2, n)
        passenger_l1 = GSmethods.rearrange_order(passenger_l1, n)
        passenger_l2 = GSmethods.rearrange_order(passenger_l2, n)

        stable_match_l1_d = GSmethods.stableMatching(n, driver_l1, passenger_l1)
        stable_match_l2_d = GSmethods.stableMatching(n, driver_l2, passenger_l2)

        alg1_d = [
            'ALG1',
            'Driver-optimal',
            GSmethods.checkblockingpairs(stable_match_l1_d, driver_l2, passenger_l2),
            GSmethods.sumprofit(stable_match_l1_d, profits),
            GSmethods.sumeta(stable_match_l1_d, eta),
            GSmethods.minmaxall(profits, 'Max'),
            GSmethods.minmaxresult(stable_match_l1_d, profits, 'Min'),
            GSmethods.minmaxresult(stable_match_l1_d, profits, 'Max'),
            GSmethods.minmaxall(eta, 'Min'),
            GSmethods.minmaxresult(stable_match_l1_d, eta, 'Min'),
            GSmethods.minmaxresult(stable_match_l1_d, eta, 'Max')
        ]
        results.append(alg1_d)

        alg2_d = [
            'ALG2',
            'Driver-optimal',
            GSmethods.checkblockingpairs(stable_match_l2_d, driver_l1, passenger_l1),
            GSmethods.sumprofit(stable_match_l2_d, profits),
            GSmethods.sumeta(stable_match_l2_d, eta),
            GSmethods.minmaxall(profits, 'Max'),
            GSmethods.minmaxresult(stable_match_l2_d, profits, 'Min'),
            GSmethods.minmaxresult(stable_match_l2_d, profits, 'Max'),
            GSmethods.minmaxall(eta, 'Min'),
            GSmethods.minmaxresult(stable_match_l2_d, eta, 'Min'),
            GSmethods.minmaxresult(stable_match_l2_d, eta, 'Max')
        ]
        results.append(alg2_d)


        stable_match_l1_p = GSmethods.stableMatching(n, passenger_l1, driver_l1)
        stable_match_l1_p = {y: x for x, y in stable_match_l1_p.items()}



        stable_match_l2_p = GSmethods.stableMatching(n, passenger_l2, driver_l2)
        stable_match_l2_p = {y: x for x, y in stable_match_l2_p.items()}

        alg1_p = [
            'ALG1',
            'Passenger-optimal',
            GSmethods.checkblockingpairs(stable_match_l1_p, driver_l2, passenger_l2),
            GSmethods.sumprofit(stable_match_l1_p, profits),
            GSmethods.sumeta(stable_match_l1_p, eta),
            GSmethods.minmaxall(profits, 'Max'),
            GSmethods.minmaxresult(stable_match_l1_p, profits, 'Min'),
            GSmethods.minmaxresult(stable_match_l1_p, profits, 'Max'),
            GSmethods.minmaxall(eta, 'Min'),
            GSmethods.minmaxresult(stable_match_l1_p, eta, 'Min'),
            GSmethods.minmaxresult(stable_match_l1_p, eta, 'Max')
        ]
        results.append(alg1_p)

        alg2_p = [
            'ALG2',
            'Passenger-optimal',
            GSmethods.checkblockingpairs(stable_match_l2_p, driver_l1, passenger_l1),
            GSmethods.sumprofit(stable_match_l2_p, profits),
            GSmethods.sumeta(stable_match_l2_p, eta),
            GSmethods.minmaxall(profits, 'Max'),
            GSmethods.minmaxresult(stable_match_l2_p, profits, 'Min'),
            GSmethods.minmaxresult(stable_match_l2_p, profits, 'Max'),
            GSmethods.minmaxall(eta, 'Min'),
            GSmethods.minmaxresult(stable_match_l2_p, eta, 'Min'),
            GSmethods.minmaxresult(stable_match_l2_p, eta, 'Max')
        ]
        results.append(alg2_p)


    return results
