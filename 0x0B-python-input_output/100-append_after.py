#!/usr/bin/python3
'''Task 13 - Search and Update'''


def append_after(filename="", search_string="", new_string=""):
    '''Insert line of text into a file.

    Args:
        filename (str): the file.
        search_string (str): The string to search.
        new_string (str): The string to insert.
    '''
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
