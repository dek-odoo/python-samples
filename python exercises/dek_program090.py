# !/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program090:
# By using list comprehension, please write a program generate a 3*5*8 3D
# array whose each element is 0.

# Hints:
# Use list comprehension to make an array.


def main(depth, rows, cols):
    array = [[[0 for col in range(cols)]
              for row in range(rows)]
             for dpth in range(depth)]

    print array


if __name__ == '__main__':
    main(3, 5, 8)
