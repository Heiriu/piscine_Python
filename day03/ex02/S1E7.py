from S1E9 import Character


class Baratheon(Character):
    """representing the baratheon family."""

    def __init__(self, first_name: str, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "Brown"
        self.hairs = "dark"

    def __str__(self):
        """return the characteristic of
the baratheon object when caling __str__"""

        return f'Vector\
: (\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'

    def __repr__(self):
        """return the characteristic of
the baratheon object when caling __repr__"""

        return f'Vector\
: (\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'


class Lannister(Character):
    """representing the Lannister family."""

    def __init__(self, first_name: str, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """return the characteristic of
the baratheon object when caling __str__"""

        return f'Vector\
: (\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'

    def __repr__(self):
        """return the characteristic of
the baratheon object when caling __repr__"""

        return f'Vector\
: (\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'

    @classmethod
    def create_lannister(cls, first_name: str, is_alive=True):
        return cls(first_name, is_alive)


def main():
    Jamie = Lannister("Jamie")
    print(Jamie)
    print(Jamie.__dict__)
    print(Jamie.__doc__)


if __name__ == "__main__":
    main()
