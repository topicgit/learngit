#!/usr/bin/python

import cPickle as p

dbfile = 'addr.data'

con_dict = {'gengjie': ['123', 'jie@12.com'],
     'xiaoming': ['456','ming@456.com'],
	'redis':['789','123@redis.org']
    }

f = file(dbfile,'w')
p.dump(con_dict,f)

f.close()
