#!/usr/bin/python3
def search_replace(my_list, search, replace):
    repl_list = list(map(lambda i: replace if i == search else i, my_list))
    return (repl_list)
