# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/11/2023
# Description: Write a recursive function named list_max that takes as its parameter
# a list of numbers and returns the maximum value in the list. You can assume the list
# contains at least one element. If multiple elements of the list are tied for the
# maximum, you would still return that value.

def list_max(num_list):
    """Returns the largest value in a list."""
    if len(num_list) == 1:
        return num_list[0]
    value = list_max(num_list[1:])
    return value if value > num_list[0] else num_list[0]


# num_list = [5, 9, 45, 6, 11, 22]
# print(str(list_max(num_list)))
