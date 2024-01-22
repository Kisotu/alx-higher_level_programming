#!/usr/bin/python3
def safe_print_list_integer(my_list=[], x=0):
    ctr = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
        except (ValueError, TypeError):
            pass
        else:
            ctr += 1
    print()
    return (ctr)
