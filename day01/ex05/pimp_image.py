import numpy as np
import cv2
import array
import matplotlib.pyplot as plt

def ft_invert(array) -> array:

    image_i = cv2.bitwise_not(array)

    plt.imshow(image_i)
    plt.show()


def ft_red(array) -> array:
    print()


def ft_green(array) -> array:
    print()


def ft_blue(array) -> array:
    print()


def ft_grey(array) -> array:

    plt.imshow(array, cmap="gray")
    plt.show()


def main():
    return


if __name__ == "__main__":
    main()
