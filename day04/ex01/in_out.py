def square(x: int | float) -> int | float:
    """return the square of a number"""
    return (x * x)


def pow(x: int | float) -> int | float:
    """return the power of a number"""
    count = x - 1
    resultat = x
    while count >= 1:
        resultat *= x
        count -= 1
    if count > 0:
        resultat *= x**count
    return (resultat)


def outer(x: int | float, function) -> object:
    """this fonction count how many time she is calling"""
    outer.count = 0

    def inner() -> float:
        """this fonction return a number depending of
 an int and the function receive"""
        outer.count += 1
        i = 0
        result = x
        while i < outer.count:
            result = function(result)
            i += 1
        new_object = in_out(result, function)
        return new_object
    return inner


class in_out(object):
    """class in_out for the function outer"""
    def __init__(self, x, function):
        """constructor for class in_out"""
        self.nbr = x
        self.function = function
        self.count = 1

    def __str__(self):
        """return the number of the class"""
        return str(self.nbr)


def main():
    return


if __name__ == "__main__":
    main()
