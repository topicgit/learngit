#!/usr/bin/env python


contacts_list={
		'gengjie' : ['what',13426210052,'IT'],
		'huanhuan': '13520859616',
		'QQ'	  : '1111111',
		'others'  : {
                      'xiaoming' : 'tempo',
                   }
	     	}

#contacts_list['ww'] = '222222222'
#contacts_list['gengjie'] = '66666666'
#del contacts_list['gengjie']
#print contacts_list


for k,v in contacts_list.items():
	if type(v) is list:
		for i in v:
			print '___',i
	elif type(v) is dict:
		for key,value in v.items():
			print '---->',key,value
	else: print k,v

#	print k,type(v)
