#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program can calculate the cost of a pizza by its diameter in inches


import constants


def main():
    # This function calculates the cost of a pizza

    # Input
    diameter = int(input("Enter the diameter of the pizza you would like in " +
                         "inches here: "))

    # Process
    sub_total = constants.LABOR + constants.RENT + \
        (diameter*constants.COST_PER_INCH)
    total = sub_total + (sub_total*constants.HST)

    # Output
    print("")
    print("The cost of a {0} inch pizza would be ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
