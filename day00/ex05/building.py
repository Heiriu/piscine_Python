import sys


def count_and_print_argv(argv: str):
    """count_and_print_argv is a fonction that take
a single string as arguments
and displays the sums of its upper-case characters, lower-case
characters, punctuation characters, digits and spaces"""

    building = {"upper": 0, "lower": 0, "punct": 0, "digits": 0, "spaces": 0}
    for carac in argv:
        if carac.isupper():
            building['upper'] += 1
        elif carac.islower():
            building['lower'] += 1
        elif carac.isdigit():
            building['digits'] += 1
        elif carac.isspace():
            building['spaces'] += 1
        elif carac.isalpha() == 0:
            building['punct'] += 1

    length = 0
    for i in building:
        length += int(building[i])
    print("The text contains", length, "characters:")
    print(building['upper'], "upper letters")
    print(building['lower'], "lower letters")
    print(building['punct'], "punctuation marks")
    print(building['spaces'], "spaces")
    print(building['digits'], "digits")


def main():

    if len(sys.argv) < 2:
        try:
            argv = input("\033[0;33mwhat is the text to count ?\033[0m\n")
            argv += " "
        except EOFError:
            print("\033[0;33musing ctrl + d as delimiter\
, exiting program.\033[0m")
            sys.exit(1)
    else:
        assert len(sys.argv) <= 2, "\033[0;31mtoo many argument\
 given\033[0m"
        argv = sys.argv[1]
    count_and_print_argv(argv)


if __name__ == "__main__":
    main()
