import pandas as pd
import matching
import time
import utilities


def runtime():
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

        run = matching.runtime_run(j, driver_l1, passenger_l1, driver_l2, passenger_l2, profits, eta)

        inter_results = [j, preference_time, time.process_time() - start_time_all]
        runtime_all.append(inter_results)
        print(j)

    df_runtime = pd.DataFrame(runtime_all, columns=['n=', 'Run Time Pref in s', 'Run Time All in s'])

    df_runtime.to_csv(f'./results/run_time.csv')
    del df_runtime