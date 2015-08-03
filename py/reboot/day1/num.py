#!/usr/bin/env python
# -*- coding: utf-8 -*-

x=0

while True:
    num=raw_input('Please input number  [Q/q to exit] : ')
    if num == 'q'  or num == 'Q':
        print 'total num : %d' % x
        break
    elif num == '':
        continue
    else:
        x=x+int(num)

