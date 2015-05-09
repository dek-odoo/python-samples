# !/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program092:
# By using list comprehension, please write a program to print the list
# after removing the value 24 in [12,24,35,24,88,120,155].

# Hints:
# Use list's remove method to delete a value.


def main(nlist, element):
    nlist.remove(element)
    return nlist

if __name__ == '__main__':
    list1 = [12, 24, 35, 70, 88, 120, 155]
    print "list1", list1
    list2 = main(list1, 24)
    print "list2", list2
