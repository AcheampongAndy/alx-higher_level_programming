#!/usr/bin/python3
def get_hex(number):
    hexstr = '0123456789abcdef'
    tens = number // 16
    ones = number % 16
    if tens > 0:
        return hexstr[tens] + hexstr[ones]
    else:
        return hexstr[ones]

for number in range(99):
    print('{:d} = 0x{}'.format(number, get_hex(number)))
