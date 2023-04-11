import time
import utilities


def run(n, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, arrival_time, d_gender):
    interm_results = []

    # Enable for driver-optimal results
    #stable_match_l1_d = GSmethods.stableMatching(n, driver_l1, passenger_l1)
    #stable_match_l2_d = GSmethods.stableMatching(n, driver_l2, passenger_l2)

    stable_match_l1_p = utilities.stableMatching(n, passenger_l1, driver_l1)
    stable_match_l1_p = {y: x for x, y in stable_match_l1_p.items()}

    stable_match_l2_p = utilities.stableMatching(n, passenger_l2, driver_l2)
    stable_match_l2_p = {y: x for x, y in stable_match_l2_p.items()}

    # Enable for driver-optimal results
    # alg1_d = [
    #     'ALG1',
    #     'Driver-optimal',
    #     utilities.checkblockingpairs(stable_match_l1_d, driver_l2, passenger_l2),
    #     utilities.sumprofit(stable_match_l1_d, profits),
    #     utilities.sumeta(stable_match_l1_d, arrival_time),
    #     utilities.minmaxweightmatching(profits, 'Max'),
    #     utilities.minmaxresult(stable_match_l1_d, profits, 'Min'),
    #     utilities.minmaxresult(stable_match_l1_d, profits, 'Max'),
    #     utilities.minmaxweightmatching(arrival_time, 'Min'),
    #     utilities.minmaxresult(stable_match_l1_d, arrival_time, 'Min'),
    #     utilities.minmaxresult(stable_match_l1_d, arrival_time, 'Max')
    # ]
    # interm_results.append(alg1_d)
    #
    # Enable for driver-optimal results
    # alg2_d = [
    #     'ALG2',
    #     'Driver-optimal',
    #     utilities.checkblockingpairs(stable_match_l2_d, driver_l1, passenger_l1),
    #     utilities.sumprofit(stable_match_l2_d, profits),
    #     utilities.sumeta(stable_match_l2_d, arrival_time),
    #     utilities.minmaxweightmatching(profits, 'Max'),
    #     utilities.minmaxresult(stable_match_l2_d, profits, 'Min'),
    #     utilities.minmaxresult(stable_match_l2_d, profits, 'Max'),
    #     utilities.minmaxweightmatching(arrival_time, 'Min'),
    #     utilities.minmaxresult(stable_match_l2_d, arrival_time, 'Min'),
    #     utilities.minmaxresult(stable_match_l2_d, arrival_time, 'Max')
    # ]
    # interm_results.append(alg2_d)

    alg1_p = [
        'ALG1',
        'Passenger-optimal',
        utilities.checkblockingpairs(stable_match_l1_p, driver_l2, passenger_l2, d_gender),
        utilities.sumprofit(stable_match_l1_p, profits),
        utilities.sumeta(stable_match_l1_p, arrival_time),
        utilities.minmaxweightmatching(profits, 'Max'),
        utilities.minmaxresult(stable_match_l1_p, profits, 'Min'),
        utilities.minmaxresult(stable_match_l1_p, profits, 'Max'),
        utilities.minmaxweightmatching(arrival_time, 'Min'),
        utilities.minmaxresult(stable_match_l1_p, arrival_time, 'Min'),
        utilities.minmaxresult(stable_match_l1_p, arrival_time, 'Max')
    ]
    interm_results.append(alg1_p)

    alg2_p = [
        'ALG2',
        'Passenger-optimal',
        utilities.checkblockingpairs(stable_match_l2_p, driver_l1, passenger_l1, arrival_time),
        utilities.sumprofit(stable_match_l2_p, profits),
        utilities.sumeta(stable_match_l2_p, arrival_time),
        utilities.minmaxweightmatching(profits, 'Max'),
        utilities.minmaxresult(stable_match_l2_p, profits, 'Min'),
        utilities.minmaxresult(stable_match_l2_p, profits, 'Max'),
        utilities.minmaxweightmatching(arrival_time, 'Min'),
        utilities.minmaxresult(stable_match_l2_p, arrival_time, 'Min'),
        utilities.minmaxresult(stable_match_l2_p, arrival_time, 'Max')
    ]
    interm_results.append(alg2_p)


    return interm_results


def shuffle_run(n, shuffle, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, arrivaltime, d_gender, s):

    interm_shuffle_results = []
    start_time_shuffle = time.process_time()

    #driver_l1_shuffle = GSmethods.rearrange_order(driver_l1, n)
    #driver_l2_shuffle = GSmethods.rearrange_order(driver_l2, n)
    passenger_l1_shuffle = utilities.rearrange_order(passenger_l1, n)
    passenger_l2_shuffle = utilities.rearrange_order(passenger_l2, n)

    #stable_match_l1_d_shuffle = GSmethods.stableMatching(n, driver_l1, passenger_l1_shuffle)
    #stable_match_l2_d_shuffle = GSmethods.stableMatching(n, driver_l2, passenger_l2_shuffle)

    stable_match_l1_p_shuffle = utilities.stableMatching(n, passenger_l1_shuffle, driver_l1)
    stable_match_l1_p_shuffle = {y: x for x, y in stable_match_l1_p_shuffle.items()}

    shuffle_time_l1p = ["ETA", "ALG1", n, s, time.process_time() - start_time_shuffle]
    start_time_shuffle = time.process_time()

    stable_match_l2_p_shuffle = utilities.stableMatching(n, passenger_l2_shuffle, driver_l2)
    stable_match_l2_p_shuffle = {y: x for x, y in stable_match_l2_p_shuffle.items()}

    shuffle_time_l2p = ["ETA", "ALG2", n, s, time.process_time() - start_time_shuffle]


    # alg1_d = [
    #     'ALG1',
    #     'Driver-optimal',
    #     utilities.checkblockingpairs(stable_match_l1_d_shuffle, driver_l2, passenger_l2_shuffle),
    #     utilities.sumprofit(stable_match_l1_d_shuffle, profits),
    #     utilities.sumeta(stable_match_l1_d_shuffle, arrivaltime),
    #     utilities.minmaxweightmatching(profits, 'Max'),
    #     utilities.minmaxresult(stable_match_l1_d_shuffle, profits, 'Min'),
    #     utilities.minmaxresult(stable_match_l1_d_shuffle, profits, 'Max'),
    #     utilities.minmaxweightmatching(arrivaltime, 'Min'),
    #     utilities.minmaxresult(stable_match_l1_d_shuffle, arrivaltime, 'Min'),
    #     utilities.minmaxresult(stable_match_l1_d_shuffle, arrivaltime, 'Max')
    # ]
    # interm_shuffle_results.append(alg1_d)
    #
    # alg2_d = [
    #     'ALG2',
    #     'Driver-optimal',
    #     utilities.checkblockingpairs(stable_match_l2_d_shuffle, driver_l1, passenger_l1_shuffle),
    #     utilities.sumprofit(stable_match_l2_d_shuffle, profits),
    #     utilities.sumeta(stable_match_l2_d_shuffle, arrivaltime),
    #     utilities.minmaxweightmatching(profits, 'Max'),
    #     utilities.minmaxresult(stable_match_l2_d_shuffle, profits, 'Min'),
    #     utilities.minmaxresult(stable_match_l2_d_shuffle, profits, 'Max'),
    #     utilities.minmaxweightmatching(arrivaltime, 'Min'),
    #     utilities.minmaxresult(stable_match_l2_d_shuffle, arrivaltime, 'Min'),
    #     utilities.minmaxresult(stable_match_l2_d_shuffle, arrivaltime, 'Max')
    # ]
    # interm_shuffle_results.append(alg2_d)

    alg1_p = [
        'ALG1',
        'Passenger-optimal',
        shuffle,
        utilities.checkblockingpairs(stable_match_l1_p_shuffle, driver_l2, passenger_l2_shuffle, d_gender),
        utilities.sumprofit(stable_match_l1_p_shuffle, profits),
        utilities.sumeta(stable_match_l1_p_shuffle, arrivaltime),
        utilities.minmaxweightmatching(profits, 'Max'),
        utilities.minmaxresult(stable_match_l1_p_shuffle, profits, 'Min'),
        utilities.minmaxresult(stable_match_l1_p_shuffle, profits, 'Max'),
        utilities.minmaxweightmatching(arrivaltime, 'Min'),
        utilities.minmaxresult(stable_match_l1_p_shuffle, arrivaltime, 'Min'),
        utilities.minmaxresult(stable_match_l1_p_shuffle, arrivaltime, 'Max')
    ]
    interm_shuffle_results.append(alg1_p)

    alg2_p = [
        'ALG2',
        'Passenger-optimal',
        shuffle,
        utilities.checkblockingpairs(stable_match_l2_p_shuffle, driver_l1, passenger_l1_shuffle, arrivaltime),
        utilities.sumprofit(stable_match_l2_p_shuffle, profits),
        utilities.sumeta(stable_match_l2_p_shuffle, arrivaltime),
        utilities.minmaxweightmatching(profits, 'Max'),
        utilities.minmaxresult(stable_match_l2_p_shuffle, profits, 'Min'),
        utilities.minmaxresult(stable_match_l2_p_shuffle, profits, 'Max'),
        utilities.minmaxweightmatching(arrivaltime, 'Min'),
        utilities.minmaxresult(stable_match_l2_p_shuffle, arrivaltime, 'Min'),
        utilities.minmaxresult(stable_match_l2_p_shuffle, arrivaltime, 'Max')
    ]
    interm_shuffle_results.append(alg2_p)

    interm_shuffle_results.append(shuffle_time_l1p)
    interm_shuffle_results.append(shuffle_time_l2p)


    return interm_shuffle_results

def runtime_run(alg, n, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, arrival_time, d_gender):
    interm_results = []
    algo = alg

    if algo == 1:
        stable_match_l1_p = utilities.stableMatching(n, passenger_l1, driver_l1)
        stable_match_l1_p = {y: x for x, y in stable_match_l1_p.items()}

        alg1_p = [
            'ALG1',
            'Passenger-optimal',
            utilities.checkblockingpairs(stable_match_l1_p, driver_l2, passenger_l2, d_gender),
            utilities.sumprofit(stable_match_l1_p, profits),
            utilities.sumeta(stable_match_l1_p, arrival_time),
            utilities.minmaxweightmatching(profits, 'Max'),
            utilities.minmaxresult(stable_match_l1_p, profits, 'Min'),
            utilities.minmaxresult(stable_match_l1_p, profits, 'Max'),
            utilities.minmaxweightmatching(arrival_time, 'Min'),
            utilities.minmaxresult(stable_match_l1_p, arrival_time, 'Min'),
            utilities.minmaxresult(stable_match_l1_p, arrival_time, 'Max')
        ]
        interm_results.append(alg1_p)

    elif algo == 2:
        stable_match_l2_p = utilities.stableMatching(n, passenger_l2, driver_l2)
        stable_match_l2_p = {y: x for x, y in stable_match_l2_p.items()}

        alg2_p = [
            'ALG2',
            'Passenger-optimal',
            utilities.checkblockingpairs(stable_match_l2_p, driver_l1, passenger_l1, arrival_time),
            utilities.sumprofit(stable_match_l2_p, profits),
            utilities.sumeta(stable_match_l2_p, arrival_time),
            utilities.minmaxweightmatching(profits, 'Max'),
            utilities.minmaxresult(stable_match_l2_p, profits, 'Min'),
            utilities.minmaxresult(stable_match_l2_p, profits, 'Max'),
            utilities.minmaxweightmatching(arrival_time, 'Min'),
            utilities.minmaxresult(stable_match_l2_p, arrival_time, 'Min'),
            utilities.minmaxresult(stable_match_l2_p, arrival_time, 'Max')
        ]
        interm_results.append(alg2_p)

    return interm_results