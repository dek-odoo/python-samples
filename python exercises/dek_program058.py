# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Assuming that we have some email addresses in the
# "username@companyname.com" format, please write program to print the
# user name of a given email address. Both user names and company names
# are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# john@google.com

# Then, the output of the program should be:

# john

# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# Hints:
# Use \w to match letters.

import re
print 'Enter Email Address :'


def do(emailAddress):
    pattern = "(\w+)@((\w+\.)+(com))"
    result = re.match(pattern, emailAddress)
    print result.group(1)


def main():
    do('dkatodoo@gmail.com')

if __name__ == '__main__':
    main()
    # main(raw_input())
