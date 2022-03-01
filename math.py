#!/usr/bin/env python3

# Created by Yiyun Qin
# Created on March 2022
# This is the math program, with proper style

import math


def main():
    # This function calculates the area and perimetre of a rectangle

    # input
    length = int(input("Enter the length of the rectangle (mm): "))
    width = int(input("Enter the width of the rectangle (mm): "))

    # process
    area = length * width
    perimetre = 2 * (length + width)

    # output
    print("")

    print("Area is {} mm².".format(area))
    print("Perimetre is {} mm.".format(perimetre))

    print("\nDone.")


if __name__ == "__main__":
    main()
