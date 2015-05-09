#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program088:
# By using list comprehension, please write a program to print the list
# after removing delete numbers which are divisible by 5 and 7 in
# [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.


def main(numlist):
    return [num for num in numlist if int(num) % 5 and int(num) % 7]

if __name__ == '__main__':
    print main([12, 24, 35, 70, 88, 120, 155, 54])
