# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# A robot moves in a plane starting from the original point (0,0). The
# robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The
# trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps.
# Please write a program to compute the distance from current
# position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.

# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# n case of input data being supplied to the question, it should be
# assumed to be a console input.

import math
print 'Enter Input like UP 5, DOWN 4, LEFT 3, RIGHT 5 ..'


def main():
    position = [0, 0]
    while True:
        input_value = raw_input()
        position_value = input_value.split(' ')
        if position_value[0].upper() == 'UP':
            position[0] += int(position_value[1])
        elif position_value[0].upper() == 'DOWN':
            position[0] -= int(position_value[1])
        elif position_value[0].upper() == 'LEFT':
            position[1] -= int(position_value[1])
        elif position_value[0].upper() == 'RIGHT':
            position[1] += int(position_value[1])
        elif not input_value:
            break
        else:
            pass
    print position[0], position[1]
    print 'Current Position is :',
    print int(round(math.sqrt(position[0] ** 2 + position[1] ** 2)))
if __name__ == '__main__':
    main()
