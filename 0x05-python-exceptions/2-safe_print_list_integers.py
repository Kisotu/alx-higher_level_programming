#!/usr/bin/python3
def safe_print_list_integer(my_list=[], x=0):
    ctr = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            ctr += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ctr)
