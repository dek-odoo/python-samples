#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar


# program# : Name
# =>
# Write a program that computes the net amount of a bank account
# based a transaction log from console input. The transaction log
# format is shown as following:
# D 100
# W 200
# ��
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def main():
    bal = 0
    print "\n************Press Enter to Exit()*******************\n"
    print '\n\'CODE(D/W) Amount\' : '
    while True:
        print "Balance: ", bal
        str = raw_input()
        if not str:  # If str is blank, exit
            break
        str = str.split()
        command = [x for x in str]
        wd = command[0]
        amount = int(command[1])
        if wd == 'd' or wd == 'D':
            bal = bal + amount
        elif wd == 'w' or wd == 'W':
            if bal > 0 and bal >= amount:
                bal = bal - amount
            else:
                print "\"can't withdraw More\", your balance is: %d" % (bal)
                # break
        else:
            print "Invalid command"
    print "Balance is ", bal
main()
# checked
