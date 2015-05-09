# !/user/bin/python
# -*- coding: utf-8 -*-
# Author : (DEK) Devendra Kavthekar

# You are required to write a program to sort the (name, age, height)
# tuples by ascending order where name is string, age and height are numbers.
# The tuples are input by console. The sort criteria is:

# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.

# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85

# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
# ('Json', '21', '85'), ('Tom', '19', '80')]

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


def main():
    print 'Sample Input Data'
    print 'Tom,19,80\n', 'John,20,90\n',\
        'Jony,17,91\n', 'Jony,17,93\n', 'Json,21,85\n'
    rows = []
    print 'Enter Data : '
    while True:
        rawData = raw_input('')  # 'Tom,19,80'
        if not rawData:
            break
        tpl = tuple(rawData.split(','))
        rows.append(tpl)
        # print rows
    print 'sorted List'
    return sorted(rows)
if __name__ == '__main__':
    print main()

#****************************DUMP****************************
#****************************DUMP****************************
# class Person:

#     def __init__(self):
#         self.name = ''
#         self.age = -1
#         self.score = -1


# def sortTuple(rows, sortIndex):#half done,left
#     for rowi in rows:
#         for rowj in rows()
#             if rows[sortIndex] > rows[sortIndex + 1]:
#                 temp = row[sortIndex]
#                 rows[sortIndex] = rows[sortIndex + 1]
#                 rows[sortIndex + 1] = temp
#         print rows, sortIndex
