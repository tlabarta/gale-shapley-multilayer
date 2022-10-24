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
        inter_results = data.run(config.n[n_index])
        results.append(inter_results[0])
        results.append(inter_results[1])
        inter_results.clear()

    #8 Algorithms:
    # 2 sides (driver/passenger optimal) x 2 options (fixed order, shuffled order) x 2 Alg extensions (L1-first, L2-first)
    #To-DO:
    #Implement shuffling in stable matching runs -> 2 options
    #Select Min and Max Profit + ETA in addition to sum
    # Add option for passenger optimal matching

    df_results = pd.DataFrame(results, columns=[
        'ALG',
        'Blocking Pairs',
        'Sum_Profit',
        'Sum_ETA',
        'Min_Profit',
        'Max_Profit',
        'Min_ETA',
        'Max_ETA'
    ])

    print(df_results)

    #Visualize
    visual.boxplot(df_results, 'Blocking Pairs', config.n[n_index], config.iterations[iter_index])
    visual.boxplot(df_results, 'Sum_Profit', config.n[n_index], config.iterations[iter_index])
    visual.boxplot(df_results, 'Sum_ETA', config.n[n_index], config.iterations[iter_index])

    visual.barchart_1dimension(df_results, 'Blocking Pairs', config.n[n_index], config.iterations[iter_index])
    visual.barchart_1dimension(df_results, 'Sum_Profit', config.n[n_index], config.iterations[iter_index])
    visual.barchart_1dimension(df_results, 'Sum_ETA', config.n[n_index], config.iterations[iter_index])

    visual.corr_matrix(df_results, config.n[n_index], config.iterations[iter_index])


main()

