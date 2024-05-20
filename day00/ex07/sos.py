import sys


def convert_into_morse():
    """sos.py is a programm that takes a string as an argument
and encode it into Morse Code
. The program supports space and alphanumeric characters
. An alphanumeric character is represented by dots . and dashes -
. Complete morse characters are separated by a single space
. A space character is represented by a slash /
usage: python3 sos.py 'sos'"""

    dict_morse = {" ": "/",
                  "A": ".-",
                  "B": "-...",
                  "C": "-.-.",
                  "D": "-..",
                  "E": ".",
                  "F": "..-.",
                  "G": "--.",
                  "H": "....",
                  "I": "..",
                  "J": ".---",
                  "K": "-.-",
                  "L": ".-..",
                  "M": "--",
                  "N": "-.",
                  "O": "---",
                  "P": ".--.",
                  "Q": "--.-",
                  "R": ".-.",
                  "S": "...",
                  "T": "-",
                  "U": "..-",
                  "V": "...-",
                  "W": ".--",
                  "X": "-..-",
                  "Y": "-.--",
                  "Z": "--..",
                  "1": ".----",
                  "2": "..---",
                  "3": "...--",
                  "4": "....-",
                  "5": ".....",
                  "6": "-....",
                  "7": "--...",
                  "8": "---..",
                  "9": "----.",
                  "0": "-----"}

    morse = ""
    for i in sys.argv[1]:
        if i >= 'a' and i <= 'z':
            i = i.upper()
        assert dict_morse.get(i), "\033[0;31mthe arguments are bad\033[0m"
        morse += dict_morse[i.upper()]
        morse += ' '
    morse = morse[:-1]
    print(morse)


def main():
    assert len(sys.argv) == 2 and isinstance(sys.argv[1], str), "\033[0;31m\
the arguments are bad\033[0m"
    convert_into_morse()


if __name__ == "__main__":
    main()
