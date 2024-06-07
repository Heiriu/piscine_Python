import numpy as np
import cv2


def print_new_size(row: int, cow: int, image: np, list_img: np):
    """display the information of an image after zooming"""

    print("\033[0;33mNew shape after slicing:\
\033[0m ", image.shape, " or (", row, ", ", cow, ")", sep="")
    print(list_img)


def ft_load(path: str) -> np:
    """is a fonction that load an image,prints its format
and its pixels content in RGB format"""

    image = cv2.imread(path)
    if image is None:
        print("\033[0;31mError: cannot open the file\033[0m")
        return (None)

    for i in image:
        for y in i:
            first = y[0]
            y[0] = y[2]
            y[2] = first
    return (image)


def main():
    return


if __name__ == "__main__":
    main()
