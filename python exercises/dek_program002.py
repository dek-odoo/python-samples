#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program002 : factorial
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


def factorial(num):
    ans = 1
    for iter in range(1, num + 1):
        ans = ans * iter
    return ans


def main():
    print "sample input ", '8'
    num = int(raw_input('Enter a Number: '))
    print 'Factorial of ', num, ' is : ', factorial(num)
    # print 'Factorial of 5 is : ', factorial(5)

if __name__ == '__main__':
    main()
# checked
