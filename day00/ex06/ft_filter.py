def ft_filter(fonc, ite) -> list:
    """Return an iterator yielding those items of iterable
for which function(item)
is true. If function is None, return the items that are true."""
    if fonc is None:
        list = [i for i in ite]
        return (list)

    list = [i for i in ite if fonc(i) == 1]
    return (list)


def main():
    str1 = "TesT"
    str1 = ft_filter(None, str1)
    for i in str1:
        print(i)
    print()

    str2 = "TesT"
    str2 = filter(None, str2)
    for i in str2:
        print(i)
    print()

    result = ft_filter(ft_up, str1)
    str1 = "TesT"
    for i in result:
        print(i)
    print()

    str2 = "TesT"
    result = filter(ft_up, str2)
    for i in result:
        print(i)


def ft_down(str):
    """ft_down return true if the character given is lower
else, the fonction return false"""
    if str.islower():
        return (1)
    return (0)


def ft_up(str):
    """ft_down return true if the character given is upper
else, the fonction return false"""
    if str.isupper():
        return (1)
    return (0)


if __name__ == "__main__":
    main()
