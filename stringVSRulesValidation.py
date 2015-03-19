#!/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar

# program# : ValidatingData
# =>
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between[a - z]
# 2. At least 1 number between[0 - 9]
# 1. At least 1 letter between[A - Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and
# will check them according to the above criteria.
# Passwords that match the criteria are to be printed,
# each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1, a F1  # ,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# Q29kZSBNYWdpYwo=
# SXQgbWF5IGJsb3cgeW91IG9mZgo=
# RW50ZXJwcmlzZSBDb2RlIGFoZWFkCg==
# d3JpdHRlbmJ5REVLCg==

# There could have been a simple approach
# or regEX approach
# or any other
# But
# wanted to try the design pattern approach with more
# Quality
# reliable,more enterprise kind,more reusable,maintainable,robust
# modular,cohesive,decoupled


class Rules:
    dynaFun = []  # functions to test
    customrules = []  # set of rules for the instance
    # public method

    def addRule(self, f, str=""):
        self.dynaFun.append(f)
        self.customrules.append(str)
        # if str == '':
        #     print f
        # print type(f)

    # public method
    def validate(self, textToValidate):
        result = {}
        i = 0
        # print textToValidate
        validationResult = True
        res = False
        errorMSG = ''
        for dfunc in self.dynaFun:
            # print res, " ", dfunc.func_name, " ", self.customrules[i]
            res = dfunc(textToValidate, self.customrules[i])
            # print res, " ", dfunc.func_name, " ", self.customrules[i]
            if not res:
                validationResult = False
                # False
                errorMSG += "== Rule Violated: " + \
                    dfunc.func_name + " " + self.customrules[i] + " "
                # return False
            i = i + 1
        result = {'result': validationResult, 'errorMSG': errorMSG}
        return result

    # private method
    @staticmethod
    def contains(str, c):
        # print "\t", str, " contains ", c
        for abc in c:
            for bca in str:
                if bca == abc:
                    return True
        index = str.find(c)
        # print index, str, c
        if index != -1:
            return True
        return False

    # public method
    @staticmethod
    def atLeastOne(str, ruleExpression):  # mandate,compulsion
        # print str, ruleExpression
        statusRes = False
        isRange = False
        if ruleExpression.find('-') != -1:
            isRange = True
        for char in str:
            # print char
            if isRange:
                # print "char $$ ", char, ruleExpression[0], ruleExpression[2]
                if Rules.isInRange(char, ruleExpression[0], ruleExpression[2]):
                    # print "True", "Rule ", str, ruleExpression
                    return True
        if not isRange and Rules.contains(str, ruleExpression):
            # print str, ruleExpression
            return True
        # print "statusRes ", statusRes
        return statusRes

    # private method
    @staticmethod
    def isInRange(c, min, max):
        if c >= min and c <= max:
            return True
        False

    @staticmethod
    def forcelen(textToValidate, rule):
        numA = [int(value) for value in rule.split(',')]
        # print numA
        lent = len(textToValidate)
        if lent >= numA[0] and lent <= numA[1]:
            return True
        else:
            return False


def main():
    # start from here
    print "main starts here"
    # password = "ABd1234@1"  # All Green
    # password = "AB$"  # violating some rules
    # password = "aassd"  # violating some rules
    # password = 'ABd1234no@1'  # no rule violated
    password = '2w3E*,2We3345'
    # specifying the rules that must not be violated
    rules = Rules()
    rules.addRule(f=Rules.atLeastOne, str='a-z')
    rules.addRule(f=Rules.atLeastOne, str='A-Z')
    rules.addRule(f=Rules.atLeastOne, str='0-9')
    rules.addRule(f=Rules.atLeastOne, str='$#@')
    rules.addRule(f=Rules.forcelen, str='6,12')

    # requesting to validate the password text agaist rules
    result = rules.validate(password)

    # result is in the following form
    #   {
    #       'result': validationResult(True/False),
    #       'errorMSG': errorMSG(set of rules violated)
    #   }
    print "Is", password, "Valid Password ?", result['result']
    print result['errorMSG']
if __name__ == '__main__':
    main()
