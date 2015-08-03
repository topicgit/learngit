#!/usr/bin/env python

a=raw_input('Input a num: ')


if str.isdigit(a):
    print '\033[32;1mNumber : %d\033[0m' % int(a)
else:
    print "\033[31;1m%s Not a number!\033[0m" % a


