import pandas as pd
import GSmethods
import data2
import time


def main():

    results_fix = []
    results_shuffle = []
    shuffle_time = []

    results_fix_waiting = []
    results_shuffle_waiting = []

    runs = [20, 40, 60, 80, 100]
    shuffle = [25, 50, 100, 200]
    #iter_index = 5

    #change ETA 1-60
    #and Waiting Time 1-30
    #Change shuffling ALG: Shuffle for s = [100, 200, 500, 1000] times per i and track the time to find a good amount of shuffling
    #keep old result


    for n in runs:


        for k in range(1000):

            #Generate features and preferences for this run
            profits = GSmethods.generateFeatures(n, "driver", 1)
            eta = GSmethods.generateFeatures(n, "passenger", 1)
            waiting_time = GSmethods.generateFeatures(n, "waiting time", 1)
            eta_waiting_time = GSmethods.calculateWaitingTime(eta, waiting_time)
            driver_gender = GSmethods.generateFeatures(n, "driver", 2)
            passenger_gender = GSmethods.generateFeatures(n, "passenger", 2)
            driver_g_preferences = GSmethods.generatePreferences(n, "driver")
            passenger_g_preferences = GSmethods.generatePreferences(n, "passenger")

            driver_l1 = GSmethods.calculatePreferencesNumerical(profits, 'Profit')
            driver_l2 = GSmethods.calculatePreferences(driver_g_preferences, passenger_gender)
            passenger_l1 = GSmethods.calculatePreferencesNumerical(eta, 'ETA')
            passenger_l1_waiting_time = GSmethods.calculatePreferencesNumerical(eta_waiting_time, 'ETA')
            passenger_l2 = GSmethods.calculatePreferences(passenger_g_preferences, driver_gender)

            #Run Fix
            inter_results_fix = data2.run(n, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, eta, driver_gender)
            results_fix.append(inter_results_fix[0])
            results_fix.append(inter_results_fix[1])
            # results_fix.append(inter_results_fix[2])
            # results_fix.append(inter_results_fix[3])
            inter_results_fix.clear()

            #Run Fix Waiting Time
            inter_results_fix_waiting = data2.run(n, driver_l1, passenger_l1_waiting_time, driver_l2, passenger_l2, profits, eta_waiting_time, driver_gender)
            results_fix_waiting.append(inter_results_fix_waiting[0])
            results_fix_waiting.append(inter_results_fix_waiting[1])
            # results_fix_waiting.append(inter_results_fix_waiting[2])
            # results_fix_waiting.append(inter_results_fix_waiting[3])
            inter_results_fix_waiting.clear()

            for s in shuffle:
                for ss in range(s):
                    #Run Shuffle
                    inter_results_shuffle = data2.shuffle_run(n, s, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, eta, driver_gender, s)
                    results_shuffle.append(inter_results_shuffle[0])
                    results_shuffle.append(inter_results_shuffle[1])
                    shuffle_time.append(inter_results_shuffle[2])
                    shuffle_time.append(inter_results_shuffle[3])
                    inter_results_shuffle.clear()

                    #Run Shuffle Waiting Time
                    inter_results_shuffle_waiting = data2.shuffle_run(n, s, driver_l1, passenger_l1_waiting_time, driver_l2, passenger_l2, profits, eta_waiting_time, driver_gender, s)
                    results_shuffle_waiting.append(inter_results_shuffle_waiting[0])
                    results_shuffle_waiting.append(inter_results_shuffle_waiting[1])
                    shuffle_time.append(inter_results_shuffle_waiting[2])
                    shuffle_time.append(inter_results_shuffle_waiting[3])
                    inter_results_shuffle_waiting.clear()
            print(k)
        print(n)

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

        df_results_fix.to_csv(f'./results/Fix/data/data_fix_n{n}.csv')
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

        df_results_shuffle.to_csv(f'./results/Shuffle/data/data_shuffle_n{n}.csv')
        del df_results_shuffle
        results_shuffle.clear()

        #Waiting Time
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

        df_results_fix_waiting.to_csv(f'./results/Fix/data/data_fix_waiting_n{n}.csv')
        del df_results_fix_waiting
        results_fix_waiting.clear()

        #Waiting Time
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

        df_results_shuffle_waiting.to_csv(f'./results/Shuffle/data/data_shuffle_waiting_n{n}.csv')
        del df_results_shuffle_waiting
        results_shuffle_waiting.clear()

        df_shuffle_time = pd.DataFrame(shuffle_time, columns=[
            'Type',
            'ALG',
            'N=',
            'Shuffle',
            'Time'
        ])

        df_shuffle_time.to_csv(f'./results/Shuffle/data/shuffle_timen{n}.csv')
        del df_shuffle_time
        shuffle_time.clear()


#Record run time
    # runtime_all = []
    # runtime_test = [100, 200, 400, 600, 800, 1000, 2000, 4000, 6000, 8000, 10000]
    # for j in runtime_test:
    #     start_time_all = time.process_time()
    #
    #     profits = GSmethods.generateFeatures(j, "driver", 1)
    #     eta = GSmethods.generateFeatures(j, "passenger", 1)
    #     driver_gender = GSmethods.generateFeatures(j, "driver", 2)
    #     passenger_gender = GSmethods.generateFeatures(j, "driver", 2)
    #     driver_g_preferences = GSmethods.generatePreferences(j, "driver")
    #     passenger_g_preferences = GSmethods.generatePreferences(j, "passenger")
    #
    #     driver_l1 = GSmethods.calculatePreferencesNumerical(profits, 'Profit')
    #     driver_l2 = GSmethods.calculatePreferences(driver_g_preferences, passenger_gender)
    #     passenger_l1 = GSmethods.calculatePreferencesNumerical(eta, 'ETA')
    #     passenger_l2 = GSmethods.calculatePreferences(passenger_g_preferences, driver_gender)
    #
    #     preference_time = time.process_time() - start_time_all
    #
    #     run = data2.run(j, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, eta)
    #
    #     inter_results = [j, preference_time, time.process_time() - start_time_all]
    #     runtime_all.append(inter_results)
    #     print(j)
    #
    # df_runtime = pd.DataFrame(runtime_all, columns=['n=', 'Run Time Pref in s', 'Run Time All in s'])
    #
    # df_runtime.to_csv(f'./results/run_time.csv')
    # del df_runtime


main()

