import pandas as pd
import matching
import time
import utilities


def runtime_both_exec():
    runtime_all = []
    runtime_test = [100, 200, 400, 600, 800, 1000, 2000, 4000, 6000, 8000, 10000]
    for j in runtime_test:
        start_time_all = time.process_time()

        profits = utilities.generateFeatures(j, "driver", 1)
        eta = utilities.generateFeatures(j, "passenger", 1)
        driver_gender = utilities.generateFeatures(j, "driver", 2)
        passenger_gender = utilities.generateFeatures(j, "driver", 2)
        driver_g_preferences = utilities.generatePreferences(j)
        passenger_g_preferences = utilities.generatePreferences(j)

        driver_l1 = utilities.calculatePreferencesNumerical(profits, 'Profit')
        driver_l2 = utilities.calculatePreferences(driver_g_preferences, passenger_gender)
        passenger_l1 = utilities.calculatePreferencesNumerical(eta, 'ETA')
        passenger_l2 = utilities.calculatePreferences(passenger_g_preferences, driver_gender)

        preference_time = time.process_time() - start_time_all

        alg1start = time.process_time()
        alg1run = matching.runtime_run(1, j, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, eta, driver_gender)
        alg1 = time.process_time() - alg1start

        alg2start = time.process_time()
        alg2run = matching.runtime_run(2, j, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, eta, driver_gender)
        alg2 = time.process_time() - alg2start

        inter_results = [j, preference_time, alg1, alg2]
        runtime_all.append(inter_results)
        print(j)

    df_runtime = pd.DataFrame(runtime_all, columns=['n=', 'Run Time Pref in s', 'Run Time Alg1 in s', 'Run Time Alg2 in s'])

    df_runtime.to_csv(f'./results/run_time_both.csv')
    del df_runtime