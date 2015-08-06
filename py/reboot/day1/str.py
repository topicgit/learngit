#!/usr/bin/env  python
# -*- coding: utf-8 -*-

import re
import string

s='''Have you thought about what you want pEople to say about you after you're
gone?Can you hear the voice saying, "He was a great man." Or "She really
will be missed." What else do they say?
One of the strangest phenomena of life is to engage in a work that will last
long after death. Isn't that a lot like investing all your money so that
future generations can bare interest on it? Perhaps, yet if you look deep in
your own heart, you'll find something drives you to make this kind of
contribution---something drives every human being to find a purpose that lives
on after death.'''


str=s.lower()

dict={}
for i in string.lowercase:
    a=len(re.findall(i,str))
    if a == 0:
        continue
    dict[i]=a

adit=sorted(dict.iteritems(), key=lambda key:key[1], reverse = True ) 

for x in range(len(adit)):
    print '| %s | %s |' % (adit[x][0],adit[x][1]) 
