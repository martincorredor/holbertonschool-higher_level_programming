#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if (idx < 0) or (idx >= len(my_list)):
            return my_list.copy()

        for i in range(len(my_list)):
            if i == idx:
                copy_list = my_list.copy()
                copy_list[i] = element
                return copy_list
