#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    This function prints the first x elements of a list and returns the number of integers successfully
    printed
    
    :param my_list: a list of integers
    :param x: the number of elements to print, defaults to 0 (optional)
    :return: The number of integers printed.
    """
    times = 0
    for i in range(x):
        try:
            print ("{}".format(my_list[i]), end = "")
            times += 1
        except (ValueError,TypeError,IndexError):
            continue
    print("\n")
    return (times)


