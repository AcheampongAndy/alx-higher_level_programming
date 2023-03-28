#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        for num in range(x):
            print("{}".format(my_list[num]), end='')
            y += 1

    except IndexError:
        pass

    print()
    return(y)
