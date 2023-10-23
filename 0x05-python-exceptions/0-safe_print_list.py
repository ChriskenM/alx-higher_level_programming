#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    element_printed = 0

    try:
        for i in range(x):
            print(my_list[], end="")
            element_printed += 1
    except IndexError:
        pass

    print()
    return element_printed
