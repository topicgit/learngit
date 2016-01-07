#!/usr/bin/python

import sys
import cPickle as p

dbfile = 'addr.data'

def help():
        print '''
Usage: %s  [Type(s)] [Options]

\t-A|--add    Name phone email
\t-S|--sea    {Name|phone|email}
\t-M|--mod    old_value  new_value
\t-D|--del    name
\t-P|--print  print all contacts info 
''' % sys.argv[0]

def Search(sea):
	addrFile = file(dbfile,'rb')
	d = p.load(addrFile)
	addrFile.close()

	if sea in d :
		print '\t--------------------------------'
		print '\t Name : %s' % sea
		print '\t Tel  : %s' % d[sea][0] 
		print '\t Email: %s' % d[sea][1]
		print
	else :
		num = 0
		for k,v in d.items():
			if sea in v  :
				print '\t--------------------------------'
				print '\t Name : %s' % k
				print '\t Tel  : %s' % v[0]
				print '\t Email: %s' % v[1]
				print
				num = 1
			else :
				continue
		if not num:
			print 'not found'

def Add(a_name,a_tel,a_email):
	addrFile = file(dbfile,'rb')
	d = p.load(addrFile)
	tmp_list=[]
	tmp_list.append(a_tel)
	tmp_list.append(a_email)
	d[a_name] = tmp_list[0:] 
	

	addrFile = file(dbfile,'w')
	p.dump(d,addrFile)
	addrFile.close()

def Del(name):
	addrFile = file(dbfile,'rb')
	d = p.load(addrFile)
	addrFile.close()

	d.pop(name)
	addrFile = file(dbfile,'w')
	p.dump(d,addrFile)
	addrFile.close()

def Print_all():
	addrFile = file(dbfile,'rb')
	d = p.load(addrFile)
	addrFile.close()

	num = 0
	for k,v in d.items():

	 	print '\t--------------------------------'
		print '\t Name : %s' % k
		print '\t Tel  : %s' % v[0]
		print '\t Email: %s' % v[1]
		print
		num += 1
	
	print '\tTotal number of local contacts : %s' % num
	print 
		

def Con_exit(num):
	if len(sys.argv) < num :
		help()
		sys.exit()

Con_exit(2)

if sys.argv[1] == '--sea' or sys.argv[1] == '-S':

	Con_exit(3)	
	Tmpsea=sys.argv[2]
	Search(Tmpsea)

elif sys.argv[1] == '-A' or sys.argv[1] == '--add':

	Con_exit(5)
	Name = sys.argv[2]
	Tel = sys.argv[3]
	Email = sys.argv[4]
	Add(Name,Tel,Email)

elif sys.argv[1] == '-D' or sys.argv[1] == '--del':

	Con_exit(3)
	Name = sys.argv[2]
	Del(Name)
elif sys.argv[1] == '-P' or sys.argv[1] == '--print':
	Con_exit(1)
	Print_all()

else:
	help()	
