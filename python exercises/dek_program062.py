# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Write a program to read an ASCII string and to convert it to a unicode
# string encoded by utf - 8.

# Hints:
# Use unicode() function to convert.


def do(sentence):
            # print ord('as')
    unicodeString = unicode(sentence, "utf-8")
    print unicodeString


def main():
    sentence = 'this is a test'
    do(sentence)
if __name__ == '__main__':
    main()
    # main(raw_input('Enter String  :'))
