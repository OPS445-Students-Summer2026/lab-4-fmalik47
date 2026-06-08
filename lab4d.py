#!/usr/bin/env python3

def first_five(string):
    return string[0:5]

def last_seven(string):
    return string[-7:]

def middle_number(number):
    string = str(number)
    return string[1:3]

def first_three_last_three(string1, string2):
    return string1[0:3] + string2[-3:]
