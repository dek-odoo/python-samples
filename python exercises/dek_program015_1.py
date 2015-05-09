#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program# : Name
# =>
# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


# Mathematical Approach

def createNumber(number, limit):
    ans = 0
    for current in range(0, limit):
        # multiply number(9) by 10, current(4) number of times
        ans = ans + (number * 10 ** current)
    print "\t", ans
    return ans


def main():
    try:
        # start from here
        numbertoCreate = int(raw_input('Enter Number: '))
        iterations = int(raw_input('Enter Number: '))
        # print "main starts here"
        ans = 0

        # print recurrent(number=9, limit=4)  # 9+99+999+9999
        # print recurrent(number=9, limit=2)  # mult(9, times=5)
        for inc in range(1, 5):
            number = createNumber(
                number=numbertoCreate, limit=iterations)  # 99999
            ans = ans + number
            # print ansrecurrent(number=tempnum, limit=inc)
        print ans
    except:
        print 'Exception:Invalid Input'
if __name__ == '__main__':
    main()


# 9, 4
# 9000
# 900
# 90
# 9
# 9999 + 999+ 99+9
