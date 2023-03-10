#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

num = len(argv) - 1

if len(argv) == 1:
    print('0 arguments.')
elif len(argv) == 2:
    print('1 argument:')
else:
    print('{:d} arguments:'.format(len(argv) - 1))

for i in range(num):
    print('{:d}: {:s}'.format(i + 1, argv[i + 1]))
