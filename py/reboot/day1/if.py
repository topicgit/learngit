#!/usr/bin/env python

a=raw_input('Input a num: ')


if str.isdigit(a):
    print '\033[32;1mNumber : %s\033[0m' % a
else:
    print "\033[31;1m%s Not a number!\033[0m" % a


