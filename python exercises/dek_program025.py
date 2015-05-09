# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# Define a class, which have a class parameter and have a same instance
# parameter.

# Hints:
# Define a instance parameter, need add it in __init__ method
# You can init a object with construct parameter or set the value later


class Student():
    name = "DefaultNameDK"

    def __init__(self, name):
        self.name = name

stud = Student(raw_input("Enter Name :"))

print stud.name
print Student.name
