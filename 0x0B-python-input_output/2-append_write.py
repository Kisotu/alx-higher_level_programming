#!/usr/bin/python3
'''Task 2 - Amend to a file'''


def append_write(filename="", text=""):
    '''Appends string to end of a text file(UTF8)
    Args:
        filename (str): Name of the file to append to.
        text (str): String to append to the file.
    Returns:
        The number of characters added
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
