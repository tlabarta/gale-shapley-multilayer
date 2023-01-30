import GSmethods
import numpy as np


def run(n, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, arrival_time):
    interm_results = []

    stable_match_l1_d = GSmethods.stableMatching(n, driver_l1, passenger_l1)
    stable_match_l2_d = GSmethods.stableMatching(n, driver_l2, passenger_l2)

    stable_match_l1_p = GSmethods.stableMatching(n, passenger_l1, driver_l1)
    stable_match_l1_p = {y: x for x, y in stable_match_l1_p.items()}

    stable_match_l2_p = GSmethods.stableMatching(n, passenger_l2, driver_l2)
    stable_match_l2_p = {y: x for x, y in stable_match_l2_p.items()}

    alg1_d = [
        'ALG1',
        'Driver-optimal',
        GSmethods.checkblockingpairs(stable_match_l1_d, driver_l2, passenger_l2),
        GSmethods.sumprofit(stable_match_l1_d, profits),
        GSmethods.sumeta(stable_match_l1_d, arrival_time),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1_d, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d, profits, 'Max'),
        GSmethods.minmaxweightmatching(arrival_time, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d, arrival_time, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d, arrival_time, 'Max')
    ]
    interm_results.append(alg1_d)

    alg2_d = [
        'ALG2',
        'Driver-optimal',
        GSmethods.checkblockingpairs(stable_match_l2_d, driver_l1, passenger_l1),
        GSmethods.sumprofit(stable_match_l2_d, profits),
        GSmethods.sumeta(stable_match_l2_d, arrival_time),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2_d, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d, profits, 'Max'),
        GSmethods.minmaxweightmatching(arrival_time, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d, arrival_time, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d, arrival_time, 'Max')
    ]
    interm_results.append(alg2_d)

    alg1_p = [
        'ALG1',
        'Passenger-optimal',
        GSmethods.checkblockingpairs(stable_match_l1_p, driver_l2, passenger_l2),
        GSmethods.sumprofit(stable_match_l1_p, profits),
        GSmethods.sumeta(stable_match_l1_p, arrival_time),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1_p, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p, profits, 'Max'),
        GSmethods.minmaxweightmatching(arrival_time, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p, arrival_time, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p, arrival_time, 'Max')
    ]
    interm_results.append(alg1_p)

    alg2_p = [
        'ALG2',
        'Passenger-optimal',
        GSmethods.checkblockingpairs(stable_match_l2_p, driver_l1, passenger_l1),
        GSmethods.sumprofit(stable_match_l2_p, profits),
        GSmethods.sumeta(stable_match_l2_p, arrival_time),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2_p, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p, profits, 'Max'),
        GSmethods.minmaxweightmatching(arrival_time, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p, arrival_time, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p, arrival_time, 'Max')
    ]
    interm_results.append(alg2_p)


    return interm_results


def shuffle_run(n, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, arrivaltime):

    interm_shuffle_results = []

    #driver_l1_shuffle = GSmethods.rearrange_order(driver_l1, n)
    #driver_l2_shuffle = GSmethods.rearrange_order(driver_l2, n)
    passenger_l1_shuffle = GSmethods.rearrange_order(passenger_l1, n)
    passenger_l2_shuffle = GSmethods.rearrange_order(passenger_l2, n)

    stable_match_l1_d_shuffle = GSmethods.stableMatching(n, driver_l1, passenger_l1_shuffle)
    stable_match_l2_d_shuffle = GSmethods.stableMatching(n, driver_l2, passenger_l2_shuffle)

    stable_match_l1_p_shuffle = GSmethods.stableMatching(n, passenger_l1_shuffle, driver_l1)
    stable_match_l1_p_shuffle = {y: x for x, y in stable_match_l1_p_shuffle.items()}

    stable_match_l2_p_shuffle = GSmethods.stableMatching(n, passenger_l2_shuffle, driver_l2)
    stable_match_l2_p_shuffle = {y: x for x, y in stable_match_l2_p_shuffle.items()}

    alg1_d = [
        'ALG1',
        'Driver-optimal',
        GSmethods.checkblockingpairs(stable_match_l1_d_shuffle, driver_l2, passenger_l2_shuffle),
        GSmethods.sumprofit(stable_match_l1_d_shuffle, profits),
        GSmethods.sumeta(stable_match_l1_d_shuffle, arrivaltime),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1_d_shuffle, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d_shuffle, profits, 'Max'),
        GSmethods.minmaxweightmatching(arrivaltime, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d_shuffle, arrivaltime, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d_shuffle, arrivaltime, 'Max')
    ]
    interm_shuffle_results.append(alg1_d)

    alg2_d = [
        'ALG2',
        'Driver-optimal',
        GSmethods.checkblockingpairs(stable_match_l2_d_shuffle, driver_l1, passenger_l1_shuffle),
        GSmethods.sumprofit(stable_match_l2_d_shuffle, profits),
        GSmethods.sumeta(stable_match_l2_d_shuffle, arrivaltime),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2_d_shuffle, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d_shuffle, profits, 'Max'),
        GSmethods.minmaxweightmatching(arrivaltime, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d_shuffle, arrivaltime, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d_shuffle, arrivaltime, 'Max')
    ]
    interm_shuffle_results.append(alg2_d)

    alg1_p = [
        'ALG1',
        'Passenger-optimal',
        GSmethods.checkblockingpairs(stable_match_l1_p_shuffle, driver_l2, passenger_l2_shuffle),
        GSmethods.sumprofit(stable_match_l1_p_shuffle, profits),
        GSmethods.sumeta(stable_match_l1_p_shuffle, arrivaltime),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1_p_shuffle, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p_shuffle, profits, 'Max'),
        GSmethods.minmaxweightmatching(arrivaltime, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p_shuffle, arrivaltime, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p_shuffle, arrivaltime, 'Max')
    ]
    interm_shuffle_results.append(alg1_p)

    alg2_p = [
        'ALG2',
        'Passenger-optimal',
        GSmethods.checkblockingpairs(stable_match_l2_p_shuffle, driver_l1, passenger_l1_shuffle),
        GSmethods.sumprofit(stable_match_l2_p_shuffle, profits),
        GSmethods.sumeta(stable_match_l2_p_shuffle, arrivaltime),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2_p_shuffle, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p_shuffle, profits, 'Max'),
        GSmethods.minmaxweightmatching(arrivaltime, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p_shuffle, arrivaltime, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p_shuffle, arrivaltime, 'Max')
    ]
    interm_shuffle_results.append(alg2_p)


    return interm_shuffle_results
