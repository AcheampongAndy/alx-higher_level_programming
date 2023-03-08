#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_ = ""
    for cha in str:
        if i != n:
            new_ += cha
        i += 1
    return new_
