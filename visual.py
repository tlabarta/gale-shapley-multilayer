import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def boxplot(df, column: str, n_index: int, iter_index: int):
    input = df
    x = input[input['ALG']=='ALG1']
    y = input[input['ALG']=='ALG2']
    z = input

    data = [z[column], x[column], y[column]]

    fig, ax = plt.subplots()
    ax.set_title(f'Boxplot for "{column}", n = {n_index}, iterations = {iter_index}.')
    ax.boxplot(data)
    plt.xticks([1, 2, 3], ['All', 'ALG1', 'ALG2'])
    plt.xlabel(column)
    plt.show()
    plt.savefig(f'./results/boxplot/boxplot_{column}_n{n_index}_iter{iter_index}.jpg')


def barchart_1dimension(df, column: str, n_index: int, iter_index: int):
    input = df
    x = input[input['ALG']=='ALG1']
    x = x[column].mean()

    y = input[input['ALG']=='ALG2']
    y = y[column].mean()

    z = input[column].mean()

    data = [z, x, y]

    fig, ax = plt.subplots()
    bars = ax.bar(['All', 'ALG1', 'ALG2'], data, align='center')
    ax.bar_label(bars)

    plt.ylabel(column)
    plt.title(f'Average ALG results for "{column}", n = {n_index}, iterations = {iter_index}.')
    plt.show()
    plt.savefig(f'./results/barchart_1dimension/barchart_1dimension_{column}_n{n_index}_iter{iter_index}.jpg')


def corr_matrix(df, n_index: int, iter_index: int):
    sns.set(rc={"figure.figsize": (15, 13)})
    corr = sns.heatmap(df.corr().round(3), annot=True, cmap="Blues")
    corr.set(title="Correlation matrix of Blocking Pairs, Profit and ETA")
    plt.show()
    plt.savefig(f'./results/corr_matrix/corr_matrix_n{n_index}_iter{iter_index}.jpg')



