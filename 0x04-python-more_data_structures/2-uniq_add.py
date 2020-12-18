#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniques = list(dict.fromkeys(my_list))
    suma = 0
    for i in uniques:
        suma += i
    return suma
