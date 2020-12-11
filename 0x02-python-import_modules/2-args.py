#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    lenght = len(argv)
    _argument = "arguments"

    if lenght == 1:
        print("0 {}.".format(_argument))
    elif lenght == 2:
        print("{} argument:".format(lenght - 1))
        print("1:{}".format(argv[1]))
    else:
        print("{} {}:".format(lenght - 1, _argument))
        for i in range(1, lenght):
            print("{}: {}".format(i, argv[i]))
