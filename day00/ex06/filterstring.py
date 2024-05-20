import sys


def ft_filterspring(length: any):
    """filsterstring.py is a fonction that
output a list of word from S
that have a lenght greater than N"""

    x = lambda a, b: len(a) - b > 0

    list_str = [y for y in sys.argv[1].split() if x(y, length)]
    print(list_str)


def main():
    assert len(sys.argv) == 3 and sys.argv[2].isnumeric(), "\033[0;31m\
the arguments are bad\033[0m"
    assert sys.argv[1].isnumeric() == 0, "\033[0;31m\
the arguments are bad\033[0m"

    ft_filterspring(int(sys.argv[2]))


if __name__ == "__main__":
    main()
