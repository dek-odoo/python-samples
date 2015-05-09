# !/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar

# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9

# Then, the output should be:
# 1,3,5,7,9

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


def stringToNumberSequence(numsString):
    return [int(nm) for nm in numsString.split(',')]  # if nm % 2 != 0]


def main(numsString):
    result = []
    nums = stringToNumberSequence(numsString)
    [result.append(str(num)) for num in nums if num % 2 != 0]
    return ','.join(result)

if __name__ == '__main__':
    # arg = raw_input()
    arg = '1,2,3,4,5,6,7,8,9'
    print main(arg)
