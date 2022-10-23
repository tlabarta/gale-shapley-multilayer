import pandas as pd
import data
import visual
import config

def main():

    config.init()

    results = []

    n_index = 0
    iter_index = 0

    for k in range(config.iterations[iter_index]):
        results.append(data.run(config.n[n_index])[0])
        results.append(data.run(config.n[n_index])[1])

    print(results)

    df_results = pd.DataFrame(results, columns=['ALG', 'Blocking Pairs', 'Profit', 'ETA'])
    print(df_results)

    #Visualize
    visual.boxplot(df_results, 'Blocking Pairs', config.n[n_index], config.iterations[iter_index])
    visual.boxplot(df_results, 'Profit', config.n[n_index], config.iterations[iter_index])
    visual.boxplot(df_results, 'ETA', config.n[n_index], config.iterations[iter_index])

    visual.barchart_1dimension(df_results, 'Blocking Pairs', config.n[n_index], config.iterations[iter_index])
    visual.barchart_1dimension(df_results, 'Profit', config.n[n_index], config.iterations[iter_index])
    visual.barchart_1dimension(df_results, 'ETA', config.n[n_index], config.iterations[iter_index])

    visual.corr_matrix(df_results, config.n[n_index], config.iterations[iter_index])


main()

