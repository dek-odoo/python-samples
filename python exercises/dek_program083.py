#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program083:
# Please write a program to print the running time of execution of "1+1"
# for 100 times.

# Hints:
# Use timeit() function to measure the running time.

from timeit import Timer


def main():
    time = Timer("for iter in range(100):1+1")
    print time.timeit()

if __name__ == '__main__':
    main()
