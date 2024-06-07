from load_csv import load
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def aff_pop():
    """display the population of two country between the year 1800 and 2050"""

    dataFrames = load("population_total.csv")
    france_population = np.array(dataFrames.iloc[58])
    france_population = np.delete(france_population, 0)

    belge_population = np.array(dataFrames.iloc[12])
    belge_population = np.delete(belge_population, 0)

    i = 0
    while i < len(france_population):
        france_population[i] = france_population[i].rstrip("M")
        belge_population[i] = belge_population[i].rstrip("M")
        i += 1

    france_population = france_population.astype(float)
    belge_population = belge_population.astype(float)

    france_years = np.array(dataFrames.columns.tolist())
    france_years = np.delete(france_years, 0)
    france_years = france_years.astype(float)
    belge_years = np.array(dataFrames.columns.tolist())
    belge_years = np.delete(belge_years, 0)
    belge_years = belge_years.astype(float)

    plt.plot(france_years, france_population)
    plt.plot(belge_years, belge_population)
    plt.legend(["France", "Belgium"], loc="lower right")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.xlim(1790, 2050)
    plt.xticks(np.arange(1800, 2080, step=40))
    plt.ylabel("population(Million)")
    plt.yticks(np.arange(20, 80, step=20))
    plt.gcf().autofmt_xdate()
    plt.show()


def main():
    try:
        pd.read_csv("population_total.csv")
    except FileNotFoundError:
        print("Error: path is wrong")
        return None
    aff_pop()


if __name__ == "__main__":
    main()
