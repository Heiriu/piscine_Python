from abc import ABC, abstractmethod


class Character(ABC):
    """character is an abstract class which can
take a first_name as first param
is_alive as second non mandatory parameter"""

    @abstractmethod
    def __init__(self, first_name: str):
        pass

    def die(self):
        """die, is a fonction that set the variable is_alive to False"""

        self.is_alive = False


class Stark(Character):
    """stark is a class who inherit from character"""

    def __init__(self, first_name: str, is_alive=True):
        """__init__ is the constructor for the class stark"""

        self.first_name = first_name
        self.is_alive = is_alive


def main():
    Ned = Stark("Ned")
    print(Ned)
    print(Ned.__dict__)
    print(Ned.__doc__)


if __name__ == "__main__":
    main()
