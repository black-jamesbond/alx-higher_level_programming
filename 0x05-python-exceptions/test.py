import sys

def safe_print_integer_err(value):
    """
    This function prints an integer and returns True if the integer is printed successfully, otherwise
    it prints an error message and returns False
    
    :param value: the value to be printed
    :return: True or False
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        sys.stderr.write("error")
        return False
value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
