

def ft_mean(*args: any) -> None:
    """return the mean of a list of number"""

    mean = 0
    for nbr in args:
        mean += nbr
    mean /= len(args)
    print("mean : ", mean)


def ft_median(*args: any) -> None:
    """return the median of a list of number"""

    lst = list(args)
    lst.sort()
    if len(lst) % 2 == 0:
        print("median : ", (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2)
    else:
        print("median : ", lst[len(lst) // 2])


def ft_quartile(*args: any) -> None:
    """return the quartile of a list of number"""

    lst = list(args)
    lst.sort()
    quart = []
    lenght = len(args)
    lenght = lenght // 2
    quart.append(float(lst[lenght // 2]))
    lenght = lenght // 2
    lenght *= 3
    if len(lst) % 2 == 0:
        lenght -= 1
    quart.append(float(lst[lenght]))
    print("quartile :", quart)


def ft_std(*args: any) -> None:
    """return the std of a list of number"""

    mean = 0
    for nbr in args:
        mean += nbr
    mean /= len(args)
    lst = []
    for nbr in args:
        lst.append(nbr - mean)
    i = 0
    while i < len(lst):
        lst[i] *= lst[i]
        i += 1
    sum = 0
    for nbr in lst:
        sum += nbr
    sum /= len(lst)
    std = sum ** .5
    print("std: ", std)


def ft_var(*args: any) -> None:
    """return the var of a list of number"""

    mean = 0
    for nbr in args:
        mean += nbr
    mean /= len(args)
    lst = []
    for nbr in args:
        lst.append(nbr - mean)
    i = 0
    while i < len(lst):
        lst[i] *= lst[i]
        i += 1
    var = 0
    for nbr in lst:
        var += nbr
    var /= len(lst)
    print("var: ", var)


def check_number(args: any) -> bool:
    """check is the value reveice is a int"""

    if isinstance(args, int):
        return False
    return True


def ft_statistics(*args: any, **kwargs: any) -> None:
    """return a number depending of the str given"""

    if len(args) == 0:
        print("\033[0;31mError: list of numbers is empty\033[0m")
        return
    for i in args:
        if check_number(i):
            print("\033[0;31mError: list of numbers contain letters\033[0m")
            return
    for i in kwargs.values():
        if i == "mean":
            ft_mean(*args)
        elif i == "median":
            ft_median(*args)
        elif i == "quartile":
            ft_quartile(*args)
        elif i == "std":
            ft_std(*args)
        elif i == "var":
            ft_var(*args)


def main():
    return


if __name__ == "__main__":
    main()
