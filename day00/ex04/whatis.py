import sys

assert len(sys.argv) <= 2, "\033[0;31mmore than one argument\
 is provided\033[0m"
if len(sys.argv) == 1:
    sys.exit(1)

arg = sys.argv[1]
if arg[0] == '-':
    arg = arg[1:]
assert arg.isnumeric(), "\033[0;31margument is not an integer\033[0m"
nbr = int(arg)
if nbr < 0:
    nbr *= -1
if nbr % 2 == 0:
    print("I'm even")
else:
    print("I'm odd")
