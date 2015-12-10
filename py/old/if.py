#!/usr/bin/env python
# -*- coding: utf-8 -*-

fa = open('a','r')
fb = open('b','r')

a_dict={}
b_dict={}

for kv in [d.strip().split('    ') for d in fa]:
    a_dict[kv[0]] = kv[1]
print a_dict


for kv in [d.strip().split('  ') for d in fb]:
    b_dict[kv[0]] = kv[1]
print b_dict


fa.close
fb.close
