import GSmethods
import numpy as np


def run(n, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, eta):
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
        GSmethods.sumeta(stable_match_l1_d, eta),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1_d, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d, profits, 'Max'),
        GSmethods.minmaxweightmatching(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d, eta, 'Max')
    ]
    interm_results.append(alg1_d)

    alg2_d = [
        'ALG2',
        'Driver-optimal',
        GSmethods.checkblockingpairs(stable_match_l2_d, driver_l1, passenger_l1),
        GSmethods.sumprofit(stable_match_l2_d, profits),
        GSmethods.sumeta(stable_match_l2_d, eta),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2_d, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d, profits, 'Max'),
        GSmethods.minmaxweightmatching(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d, eta, 'Max')
    ]
    interm_results.append(alg2_d)

    alg1_p = [
        'ALG1',
        'Passenger-optimal',
        GSmethods.checkblockingpairs(stable_match_l1_p, driver_l2, passenger_l2),
        GSmethods.sumprofit(stable_match_l1_p, profits),
        GSmethods.sumeta(stable_match_l1_p, eta),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1_p, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p, profits, 'Max'),
        GSmethods.minmaxweightmatching(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p, eta, 'Max')
    ]
    interm_results.append(alg1_p)

    alg2_p = [
        'ALG2',
        'Passenger-optimal',
        GSmethods.checkblockingpairs(stable_match_l2_p, driver_l1, passenger_l1),
        GSmethods.sumprofit(stable_match_l2_p, profits),
        GSmethods.sumeta(stable_match_l2_p, eta),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2_p, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p, profits, 'Max'),
        GSmethods.minmaxweightmatching(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p, eta, 'Max')
    ]
    interm_results.append(alg2_p)


    return interm_results


def shuffle_run(n, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, eta):

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
        GSmethods.sumeta(stable_match_l1_d_shuffle, eta),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1_d_shuffle, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d_shuffle, profits, 'Max'),
        GSmethods.minmaxweightmatching(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d_shuffle, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_d_shuffle, eta, 'Max')
    ]
    interm_shuffle_results.append(alg1_d)

    alg2_d = [
        'ALG2',
        'Driver-optimal',
        GSmethods.checkblockingpairs(stable_match_l2_d_shuffle, driver_l1, passenger_l1_shuffle),
        GSmethods.sumprofit(stable_match_l2_d_shuffle, profits),
        GSmethods.sumeta(stable_match_l2_d_shuffle, eta),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2_d_shuffle, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d_shuffle, profits, 'Max'),
        GSmethods.minmaxweightmatching(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d_shuffle, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_d_shuffle, eta, 'Max')
    ]
    interm_shuffle_results.append(alg2_d)

    alg1_p = [
        'ALG1',
        'Passenger-optimal',
        GSmethods.checkblockingpairs(stable_match_l1_p_shuffle, driver_l2, passenger_l2_shuffle),
        GSmethods.sumprofit(stable_match_l1_p_shuffle, profits),
        GSmethods.sumeta(stable_match_l1_p_shuffle, eta),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l1_p_shuffle, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p_shuffle, profits, 'Max'),
        GSmethods.minmaxweightmatching(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p_shuffle, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l1_p_shuffle, eta, 'Max')
    ]
    interm_shuffle_results.append(alg1_p)

    alg2_p = [
        'ALG2',
        'Passenger-optimal',
        GSmethods.checkblockingpairs(stable_match_l2_p_shuffle, driver_l1, passenger_l1_shuffle),
        GSmethods.sumprofit(stable_match_l2_p_shuffle, profits),
        GSmethods.sumeta(stable_match_l2_p_shuffle, eta),
        GSmethods.minmaxweightmatching(profits, 'Max'),
        GSmethods.minmaxresult(stable_match_l2_p_shuffle, profits, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p_shuffle, profits, 'Max'),
        GSmethods.minmaxweightmatching(eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p_shuffle, eta, 'Min'),
        GSmethods.minmaxresult(stable_match_l2_p_shuffle, eta, 'Max')
    ]
    interm_shuffle_results.append(alg2_p)


    return interm_shuffle_results
