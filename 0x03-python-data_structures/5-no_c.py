#!/usr/bin/python3
def no_c(my_string):
    aux = list(my_string)
    for i in aux:
        if i == 'c' or i == 'C':
            aux.remove(i)
    new_str = "".join(aux)
    return new_str
