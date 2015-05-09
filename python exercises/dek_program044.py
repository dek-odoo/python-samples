# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Write a program which accepts a string as input to print "Yes"
# if the string is "yes" or "YES" or "Yes", otherwise print "No".

# Hints:
# Use if statement to judge condition.


def main(input_str):
    if input_str.upper() == 'YES':
        print 'Yes'
    else:
        print 'No'
if __name__ == '__main__':
    main(raw_input('Enter String :'))
