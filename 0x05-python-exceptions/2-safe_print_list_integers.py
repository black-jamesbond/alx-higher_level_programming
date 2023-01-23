#!/usr/bin/python3

king = [1,2,3,'d',3,4,'r']
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
            print ("{:d}".format(my_list[i]), end = "")
            times += 1
        except (ValueError,TypeError):
            continue
    print("\n")
    return(times)

safe_print_list_integers(king, 5)


