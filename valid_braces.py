'''Module providing a function to check valid braces.'''

import sys


def valid_braces(string):
    '''Checks valid braces - using a stack'''
    braces = {"(": ")", "[": "]", "{": "}"}
    str_stack = []

    for s in string:
        if s in braces.keys():
            str_stack.append(s)
        else:
            if len(str_stack) == 0 or braces[str_stack.pop()] != s:
                return False
    return len(str_stack) == 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide a string of braces')
    else:
        print(valid_braces(sys.argv[1]))
