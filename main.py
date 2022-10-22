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

    visual.boxplot(df_results, 'Blocking Pairs', n_index, iter_index)

main()

