#!/usr/bin/python
# -*- coding: utf-8 -*-
#- Author : (DEK) Devendra Kavthekar

# program086:
# Please write a program to generate all sentences where subject is in
# ["I", "You"] and verb is in ["Play", "Love"] and the object is in
# ["Hockey","Football"].

# Hints:
# Use list[index] notation to get a element from a list.


def main():
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]

    for subject in range(len(subjects)):
        for verb in range(len(verbs)):
            for obj in range(len(objects)):
                print "%s %s %s." \
                    % (subjects[subject], verbs[verb], objects[obj])

if __name__ == '__main__':
    main()
