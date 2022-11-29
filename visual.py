import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def boxplot(df, column: str, n_index: int, iter_index: int, category):
    input = df
    x = input[input['ALG']=='ALG1']
    x_d = input[(input['ALG']=='ALG1') & (input['Optimum']=='Driver-optimal')]
    x_p = input[(input['ALG']=='ALG1') & (input['Optimum']=='Passenger-optimal')]
    y = input[input['ALG']=='ALG2']
    y_d = input[(input['ALG']=='ALG2') & (input['Optimum']=='Driver-optimal')]
    y_p = input[(input['ALG']=='ALG2') & (input['Optimum']=='Passenger-optimal')]
    z = input

    data = [z[column], x[column], x_d[column], x_p[column], y[column], y_d[column], y_p[column]]

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_title(f'Boxplot for "{column}", n = {n_index}, iterations = {iter_index}.')
    ax.boxplot(data)
    plt.xticks([1, 2, 3, 4, 5, 6, 7], ['All', 'ALG1', 'ALG1-Driver', 'ALG1-Pass.', 'ALG2', 'ALG2-Driver', 'ALG2-Pass.'])
    plt.xlabel(column)
    plt.savefig(f'./results/{category}/boxplot/boxplot_{column}_n{n_index}_iter{iter_index}.jpg')
    plt.show()


def barchart_1dimension(df, column: str, n_index: int, iter_index: int, category):
    input = df
    x = input[input['ALG']=='ALG1']
    x = x[column].mean()

    x_d = input[(input['ALG']=='ALG1') & (input['Optimum']=='Driver-optimal')]
    x_d = x_d[column].mean()

    x_p = input[(input['ALG']=='ALG1') & (input['Optimum']=='Passenger-optimal')]
    x_p = x_p[column].mean()

    y = input[input['ALG']=='ALG2']
    y = y[column].mean()

    y_d = input[(input['ALG']=='ALG2') & (input['Optimum']=='Driver-optimal')]
    y_d = y_d[column].mean()

    y_p = input[(input['ALG']=='ALG2') & (input['Optimum']=='Passenger-optimal')]
    y_p = y_p[column].mean()

    z = input[column].mean()

    data = [z, x, x_d, x_p, y, y_d, y_p]

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(['All', 'ALG1', 'ALG1-Driver', 'ALG1-Pass.', 'ALG2', 'ALG2-Driver', 'ALG2-Pass.'], data, align='center')
    ax.bar_label(bars)

    plt.ylabel(column)
    plt.title(f'Average ALG results for "{column}", n = {n_index}, iterations = {iter_index}.')
    plt.savefig(f'./results/{category}/barchart_1dimension/barchart_1dimension_{column}_n{n_index}_iter{iter_index}.jpg')
    plt.show()


def corr_matrix(df, n_index: int, iter_index: int, category):
    sns.set(rc={"figure.figsize": (15, 13)})
    corr = sns.heatmap(df.corr().round(3), annot=True, cmap="Blues")
    corr.set(title="Correlation matrix of Blocking Pairs, Profit and ETA")
    plt.savefig(f'./results/{category}/corr_matrix/corr_matrix_n{n_index}_iter{iter_index}.jpg')
    plt.show()



