# !/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program093:
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the
# above given lists.

# Hints:
# Use set() and "&=" to do set intersection operation.


def main(list1, list2):
    intersect1 = set(list1)
    intersect2 = set(list2)
    intersect1 &= intersect2
    return intersect1


if __name__ == '__main__':
    print main([1, 3, 6, 78, 35, 55], [12, 24, 35, 24, 88, 120, 155])
