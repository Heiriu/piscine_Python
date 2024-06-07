from load_csv import load
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def aff_life():
    """displays the country information of your campus versus other
country of your choice: here is Belgium"""

    dataFrames = load("life_expectancy_years.csv")
    array_average_year = np.array(dataFrames.iloc[58])
    array_average_year = np.delete(array_average_year, 0)

    years = np.array(dataFrames.columns.tolist())
    years = np.delete(years, 0)
    years = years.astype(int)

    plt.plot(years, array_average_year)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(np.arange(1800, 2120, step=40))
    plt.ylabel("Life expectancy")
    plt.show()


def main():
    try:
        pd.read_csv("life_expectancy_years.csv")
    except FileNotFoundError:
        print("Error: path is wrong")
        return None
    aff_life()


if __name__ == "__main__":
    main()
