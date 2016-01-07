#!/usr/bin/python

import cPickle as p

addrf = 'addr.data'

f=file(addrf,'rb')
d=p.load(f)
d.pop('yanhao')

print d
