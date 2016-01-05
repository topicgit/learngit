#!/usr/bin/python

import cPickle as p

dbfile = 'addr.data'

con_dict = {'Gengjie': ['123', 'jie@12.com'],
     'Xiaoming': ['456','ming@456.com'],
	'Redis':['789','123@redis.org']
    }

f = file(dbfile,'w')
p.dump(con_dict,f)

f.close()
