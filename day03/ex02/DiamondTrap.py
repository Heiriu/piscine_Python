from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """representing the king, a mix of Baratheon and Lannister"""

    def set_eyes(self, eyes_colors: str):
        """set the variable eyes"""

        self.eyes = eyes_colors

    def set_hairs(self, hairs_colors: str):
        """set the variable hairs"""

        self.hairs = hairs_colors

    def get_eyes(self) -> str:
        """get the variable eyes"""

        return (self.eyes)

    def get_hairs(self) -> str:
        """get the variable hairs"""

        return (self.hairs)


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
