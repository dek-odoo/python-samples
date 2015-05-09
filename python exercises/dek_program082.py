#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program082:
# Please write a program to compress and decompress the string "hello
# world!hello world!hello world!hello world!".

# Hints:
# Use zlib.compress() and zlib.decompress() to compress and decompress a
# string.

import zlib


def main(data):
    compData = zlib.compress(data)
    print "Compressed Form:", compData
    print "Decompressed Form:", zlib.decompress(compData)


if __name__ == '__main__':
    main(raw_input("Input String: "))
    # main('hello world!hello world!hello world!hello world!')
