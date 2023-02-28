import pandas as pd
import utilities
import matching



def create():
    results_fix = []
    results_shuffle = []
    shuffle_time = []

    results_fix_waiting = []
    results_shuffle_waiting = []

    n = [20, 40, 60, 80, 100]
    s = [25, 50, 100, 200]
    i = 1000

    for size in n:

        for k in range(i):

            # Generate features and preferences for this run
            profits = utilities.generateFeatures(size, "driver", 1)
            eta = utilities.generateFeatures(size, "passenger", 1)
            waiting_time = utilities.generateFeatures(size, "waiting time", 1)
            eta_waiting_time = utilities.calculateWaitingTime(eta, waiting_time)
            driver_gender = utilities.generateFeatures(size, "driver", 2)
            passenger_gender = utilities.generateFeatures(size, "passenger", 2)
            driver_g_preferences = utilities.generatePreferences(size)
            passenger_g_preferences = utilities.generatePreferences(size)

            driver_l1 = utilities.calculatePreferencesNumerical(profits, 'Profit')
            driver_l2 = utilities.calculatePreferences(driver_g_preferences, passenger_gender)
            passenger_l1 = utilities.calculatePreferencesNumerical(eta, 'ETA')
            passenger_l1_waiting_time = utilities.calculatePreferencesNumerical(eta_waiting_time, 'ETA')
            passenger_l2 = utilities.calculatePreferences(passenger_g_preferences, driver_gender)

            # Run Fix Order
            inter_results_fix = matching.run(size, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, eta,
                                             driver_gender)
            results_fix.append(inter_results_fix[0])
            results_fix.append(inter_results_fix[1])

            # Enable for driver-optimal results
            # results_fix.append(inter_results_fix[2])
            # results_fix.append(inter_results_fix[3])
            inter_results_fix.clear()

            # Run Fix Order with Waiting Time
            inter_results_fix_waiting = matching.run(size, driver_l1, passenger_l1_waiting_time, driver_l2, passenger_l2,
                                                     profits, eta_waiting_time, driver_gender)
            results_fix_waiting.append(inter_results_fix_waiting[0])
            results_fix_waiting.append(inter_results_fix_waiting[1])
            # results_fix_waiting.append(inter_results_fix_waiting[2])
            # results_fix_waiting.append(inter_results_fix_waiting[3])
            inter_results_fix_waiting.clear()

            for shuffle in s:
                for ss in range(shuffle):
                    # Run Shuffle
                    inter_results_shuffle = matching.shuffle_run(size, shuffle, driver_l1, passenger_l1, driver_l2, passenger_l2,
                                                                 profits, eta, driver_gender, shuffle)
                    results_shuffle.append(inter_results_shuffle[0])
                    results_shuffle.append(inter_results_shuffle[1])
                    shuffle_time.append(inter_results_shuffle[2])
                    shuffle_time.append(inter_results_shuffle[3])
                    inter_results_shuffle.clear()

                    # Run Shuffle Waiting Time
                    inter_results_shuffle_waiting = matching.shuffle_run(size, shuffle, driver_l1, passenger_l1_waiting_time,
                                                                         driver_l2, passenger_l2, profits,
                                                                         eta_waiting_time, driver_gender, shuffle)
                    results_shuffle_waiting.append(inter_results_shuffle_waiting[0])
                    results_shuffle_waiting.append(inter_results_shuffle_waiting[1])
                    shuffle_time.append(inter_results_shuffle_waiting[2])
                    shuffle_time.append(inter_results_shuffle_waiting[3])
                    inter_results_shuffle_waiting.clear()
            print(k)
        print(size)

        df_results_fix = pd.DataFrame(results_fix, columns=[
            'ALG',
            'Optimum',
            'Blocking Pairs',
            'Sum_Profit',
            'Sum_ETA',
            'Sum_Max_Possible_Profit',
            'Min_Profit',
            'Max_Profit',
            'Sum_Min_Possible_ETA',
            'Min_ETA',
            'Max_ETA'
        ])

        df_results_fix.to_csv(f'./results/Fix/data/data_fix_n{size}.csv')
        del df_results_fix
        results_fix.clear()

        df_results_shuffle = pd.DataFrame(results_shuffle, columns=[
            'ALG',
            'Optimum',
            'Shuffle',
            'Blocking Pairs',
            'Sum_Profit',
            'Sum_ETA',
            'Sum_Max_Possible_Profit',
            'Min_Profit',
            'Max_Profit',
            'Sum_Min_Possible_ETA',
            'Min_ETA',
            'Max_ETA'
        ])

        df_results_shuffle.to_csv(f'./results/Shuffle/data/data_shuffle_n{size}.csv')
        del df_results_shuffle
        results_shuffle.clear()

        # Waiting Time Fix Order
        df_results_fix_waiting = pd.DataFrame(results_fix_waiting, columns=[
            'ALG',
            'Optimum',
            'Blocking Pairs',
            'Sum_Profit',
            'Sum_ETA',
            'Sum_Max_Possible_Profit',
            'Min_Profit',
            'Max_Profit',
            'Sum_Min_Possible_ETA',
            'Min_ETA',
            'Max_ETA'
        ])

        df_results_fix_waiting.to_csv(f'./results/Fix/data/data_fix_waiting_n{size}.csv')
        del df_results_fix_waiting
        results_fix_waiting.clear()

        # Waiting Time Shuffle Order
        df_results_shuffle_waiting = pd.DataFrame(results_shuffle_waiting, columns=[
            'ALG',
            'Optimum',
            'Shuffle',
            'Blocking Pairs',
            'Sum_Profit',
            'Sum_ETA',
            'Sum_Max_Possible_Profit',
            'Min_Profit',
            'Max_Profit',
            'Sum_Min_Possible_ETA',
            'Min_ETA',
            'Max_ETA'
        ])

        df_results_shuffle_waiting.to_csv(f'./results/Shuffle/data/data_shuffle_waiting_n{size}.csv')
        del df_results_shuffle_waiting
        results_shuffle_waiting.clear()

        df_shuffle_time = pd.DataFrame(shuffle_time, columns=[
            'Type',
            'ALG',
            'N=',
            'Shuffle',
            'Time'
        ])

        df_shuffle_time.to_csv(f'./results/Shuffle/data/shuffle_timen{size}.csv')
        del df_shuffle_time
        shuffle_time.clear()