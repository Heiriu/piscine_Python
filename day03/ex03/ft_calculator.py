class calculator:
    """class calculator, able to do calculation"""

    def __init__(self, list_nbr: list):
        """__init__ for the class calculator"""

        self.list_nbr = list_nbr

    def __add__(self, object) -> None:
        """fonction to make an addition"""

        self.list_nbr = [i + object for i in self.list_nbr]
        print(self.list_nbr)

    def __mul__(self, object) -> None:
        """fonction to make a multiplication"""

        self.list_nbr = [i * object for i in self.list_nbr]
        print(self.list_nbr)

    def __sub__(self, object) -> None:
        """fonction to make a substraction"""

        self.list_nbr = [i - object for i in self.list_nbr]
        print(self.list_nbr)

    def __truediv__(self, object) -> None:
        """fonction to make a division"""

        for i in self.list_nbr:
            if i == 0:
                print("Error: division by 0 found in the list")
                return
        self.list_nbr = [i / object for i in self.list_nbr]
        print(self.list_nbr)


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 / 5


if __name__ == "__main__":
    main()
