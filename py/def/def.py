#!/usr/bin/env python


def check_digit(x):
    if str.isdigit(x):
        int(x)
    if not isinstance(x, (int, float)):
        print "%s is Not a number" % x
    else:
        print "OK :%s is a Number" % x



num=raw_input('Please input sth: ')

check_digit(num)

