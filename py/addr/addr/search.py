#!/usr/bin/python

import sys
import cPickle as p

dbfile = 'addr.data'

def help():
        print '''
Usage: %s  [Type(s)] [Options]

\t-A|--add Name phone  email
\t-S|--sea {Name|phone|email}
\t-M|--mod old_value  new_value
\t-D|--del name
''' % sys.argv[0]

if len(sys.argv) < 3 :
        help()
        sys.exit()


def Search(sea):
	addrFile = file(dbfile,'rb')
	d = p.load(addrFile)
	addrFile.close()

	if sea in d :
		print
		print '\t--------------------------------'
		print '\t Name : %s' % sea
		print '\t Tel  : %s' % d[sea][0] 
		print '\t Email: %s' % d[sea][1]
		print '\t--------------------------------'
		print
	else :
		num = 0
		for k,v in d.items():
			if sea in v  :
				print
				print '\t--------------------------------'
				print '\t Name : %s' % k
				print '\t Tel  : %s' % v[0]
				print '\t Email: %s' % v[1]
				print '\t--------------------------------'
				print
				num = 1
			else :
				continue
		if not num:
			print 'not found'


def Add(a_name,a_tel,a_email):
	d={}
	tmp_list=[]
	tmp_list.append(a_tel)
	tmp_list.append(a_email)
	d[a_name] = tmp_list[0:] 
	print d
	

	addrFile = file(dbfile,'ab')
	p.dump(d,addrFile)
	addrFile.close()




if sys.argv[1] == '--sea' or sys.argv[1] == '-S':
	Tmpsea=sys.argv[2]
	Search(Tmpsea)

elif sys.argv[1] == '-A' or sys.argv[1] == '--add':

	Name = sys.argv[2]
	Tel = sys.argv[3]
	Email = sys.argv[4]
	Add(Name,Tel,Email)

else:
	help()	
