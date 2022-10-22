import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

def boxplot(df, column: str, n_index: int, iter_index: int):
    input = df
    x = input[input['ALG']=='ALG1']
    y = input[input['ALG']=='ALG2']
    z = input

    data = [z[column],x[column], y[column]]

    fig, ax = plt.subplots()
    ax.set_title(f'Boxplot for column "{column}".')
    ax.boxplot(data)
    plt.xticks([1, 2, 3], ['All', 'ALG1', 'ALG2'])
    plt.xlabel(column)
    plt.show()
    plt.savefig(f'/results/boxplot/boxplot_{column}_n{n_index}_iter{iter_index}.jpg')



