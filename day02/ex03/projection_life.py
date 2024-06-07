from load_csv import load
from matplotlib import pyplot as plt
import numpy as np


def projection_life(life: any, income: any):
    """display the result of a .scv from the year 1900"""

    life = np.array(life['1900'])
    life = life.astype(float)
    income = np.array(income['1900'])
    income = income.astype(float)

    plt.plot(income, life, 'o')
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("life expectancy")
    plt.gcf().autofmt_xdate()
    plt.show()


def main():
    """load a .csv and display his result as a dot graph"""

    file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_expectancy_year = load("life_expectancy_years.csv")
    income_per_personne = load(file)
    if life_expectancy_year is None or income_per_personne is None:
        return
    projection_life(life_expectancy_year, income_per_personne)


if __name__ == "__main__":
    main()
