#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_my_list = my_list[::-1]
    for i in reversed_my_list:
        print("{:d}".format(i))
