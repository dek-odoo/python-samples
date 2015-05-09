# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# With a given tuple (1,2,3,4,5,6,7,8,9,10),
# write a program to print the first half values in one line and the last
# half values in one line.

# Hints:
# Use [n1:n2] notation to get a slice from a tuple.


def main():
    list1 = [value for value in range(1, 11)]
    print len(list1)
    print tuple(list1)
    print tuple(list1[0:len(list1) / 2])
    print tuple(list1[len(list1) / 2:len(list1)])
if __name__ == '__main__':
    main()
