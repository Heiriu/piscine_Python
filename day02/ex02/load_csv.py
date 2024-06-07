import pandas as pd


def load(path: str) -> pd:
    """take a path, check if the file is a .csv
write the dimension of the data set and return it"""

    try:
        data = pd.read_csv(path)
    except FileNotFoundError:
        print("\033[0;31mError: path is wrong\033[0m")
        return None
    file_desc = path[len(path) - 4:]
    if file_desc != ".csv":
        print("\033[0;31mError: path have the wrong format\033[0m")
        return None
    print("\033[0;33mLoading dataset of dimensions\033[0m", data.shape)
    data = data.set_index('country')
    return (data)


def main():
    print(load("life_expectancy_years.cs"))
    print(load("population_total.sv"))
    return


if __name__ == "__main__":
    main()
