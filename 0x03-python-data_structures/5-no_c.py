#!/usr/bin/env python3

def no_c(my_string):
    filtered_chars = [
            character for character in my_string
            if character != 'c' and character != 'C'
    ]
    new_string = ''.join(filtered_chars)
    return new_string


