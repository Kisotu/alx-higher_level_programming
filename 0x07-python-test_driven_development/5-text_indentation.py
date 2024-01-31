#!/usr/bin/python3
'''Task 4 - Text indentation'''


def text_indentation(text):
    '''prints a text with 2 new lines after (, . ? :)

    Args:
        text (string): text to print.
    Raises:
        TypeError: If not string.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chara = 0
    while chara < len(text) and text[chara] == ' ':
        chara += 1

    while chara < len(text):
        print(text[chara], end="")
        if text[chara] == "\n" or text[chara] in ".?:":
            if text[chara] in ".?:":
                print("\n")
            chara += 1
            while chara < len(text) and text[chara] == ' ':
                chara += 1
            continue
        chara += 1
