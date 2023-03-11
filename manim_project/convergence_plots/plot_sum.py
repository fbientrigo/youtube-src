import numpy as np
import matplotlib.pyplot as plt


def plot_summation(serie, title=r'Visualizar suma'):
    """ Grafica la sumatoria, se le entrega una serie en forma de lista y realiza una sumatoria cumulativa"""

    cumulative_series = np.cumsum(serie)

    # color a las barras
    plus_color, minus_color = 'blue', 'red'

    fig, ax = plt.subplots()

    if cumulative_series[0] > 0:
        bar_color = plus_color
    else:
        bar_color = minus_color
    ax.bar(0, cumulative_series[0], color=bar_color, bottom=0) 

    for i in range(1, len(cumulative_series)):
        sum = cumulative_series[i] - cumulative_series[i-1]
        if sum < 0:
            bar_color = minus_color
        else:
            bar_color = plus_color
        ax.bar(i, cumulative_series[i] - cumulative_series[i-1], color=bar_color, bottom=cumulative_series[i-1])


    # Labels
    ax.set_title(title)
    ax.set_xlabel('Index')
    ax.set_ylabel('Suma')
    ax.set_ylim([np.min(cumulative_series) - 1, np.max(cumulative_series) + 1])

    return fig, ax

if __name__ == '__main__':
    N = 14
    # \sum_n na
    serie = [ n / np.math.factorial(n) for n in range(N)]
    plot_summation(serie)
    plt.show()