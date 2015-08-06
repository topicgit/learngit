#!/usr/bin/env python
# File Name: isnum.py

a=raw_input('Input something : ')

if str.isdigit(a):
    print '\033[32;1mIs  a  Number : %s\033[0m' % a
else:
    print "\033[31;1m%s Not a number!\033[0m" % a


