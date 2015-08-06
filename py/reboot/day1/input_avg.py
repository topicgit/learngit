#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File : input_avg.py

x=0
count=0

while True:
    num=raw_input('Please input number  [Q/q to exit] : ')
    if num == 'q'  or num == 'Q':
        print 'total num : %d' % x
        break
    elif num == '':
        continue
    else:
        x=x+int(num)
        count+=1
print "avg num : %s" % int(x/count)

