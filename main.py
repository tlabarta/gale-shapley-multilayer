import pandas as pd

import config
import data


def main():

    config.init()

    results_fix = []

    runs = [20, 40, 60, 80, 100]
    #runtime_test = [100, 200, 400, 600, 800, 1000, 2000, 4000, 6000, 8000, 10000]
    #iter_index = 5

    for l in runs:
        for k in range(100000):
            inter_results = data.run(l)
            results_fix.append(inter_results[0])
            results_fix.append(inter_results[1])
            results_fix.append(inter_results[2])
            results_fix.append(inter_results[3])
            inter_results.clear()
        print(l)

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


        df_results_fix.to_csv(f'./results/Fix/data/data_fix_n{l}.csv')
        del df_results_fix
        results_fix.clear()


# To-Do: Reduce results to ALG1, ALG2, ALG3, ALG4
#
#     To-Do: Set axis for boxplots as 0.5 x max profit/ETA/Blocking pairs  x n
#     Check n limits without iterations, record execution time
#     n = [100, 200, 400, 600, 800, 1000, 2000, 4000, 6000, 8000, 10000]
#     If Algs terminate in less than 1 hour, write down computation time in addition to other results

    # for r in runs:
    #     results_shuffle = data.shuffle_run(r, 100000)
    #
    #     df_results_shuffle = pd.DataFrame(results_shuffle, columns=[
    #         'ALG',
    #         'Optimum',
    #         'Blocking Pairs',
    #         'Sum_Profit',
    #         'Sum_ETA',
    #         'Sum_Max_Possible_Profit',
    #         'Min_Profit',
    #         'Max_Profit',
    #         'Sum_Min_Possible_ETA',
    #         'Min_ETA',
    #         'Max_ETA'
    #     ])
    #
    #     df_results_shuffle.to_csv(f'./results/Shuffle/data/data_shuffle_n{r}.csv')
    #     print(r)


# #Record run time all
#     runtime = []
#     for j in runtime_test:
#         start_time = time.process_time()
#         run = data.run(j)
#         inter_results = [j, time.process_time() - start_time]
#         runtime.append(inter_results)
#
#
#
#     df_runtime = pd.DataFrame(runtime, columns=['n=','Run Time in s'])
#
#     df_runtime.to_csv(f'./results/run_time.csv')
#     del df_runtime

# Record run time preferences

    # runtime = []
    # for n in runtime_test:
    #     start_time = time.process_time()
    #
    #     profits = GSmethods.generateFeatures(n, "driver", 1)
    #     eta = GSmethods.generateFeatures(n, "passenger", 1)
    #     driver_gender = GSmethods.generateFeatures(n, "driver", 2)
    #     passenger_gender = GSmethods.generateFeatures(n, "driver", 2)
    #     driver_g_preferences = GSmethods.generatePreferences(n, "driver")
    #     passenger_g_preferences = GSmethods.generatePreferences(n, "passenger")
    #
    #     GSmethods.calculatePreferencesNumerical(profits, 'Profit')
    #     GSmethods.calculatePreferences(driver_g_preferences, passenger_gender)
    #     GSmethods.calculatePreferencesNumerical(eta, 'ETA')
    #     GSmethods.calculatePreferences(passenger_g_preferences, driver_gender)
    #
    #
    #     inter_results = [n, time.process_time() - start_time]
    #     runtime.append(inter_results)
    #     print(n)
    #
    #
    #
    # df_runtime = pd.DataFrame(runtime, columns=['n=','Run Time in s'])
    #
    # df_runtime.to_csv(f'./results/run_time_preferences.csv')
    # del df_runtime





main()

