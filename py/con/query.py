#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

con_list = 'a_con.txt'  # 定义通讯录文件

while True:
	input = raw_input('\033[32;1mAdmin system Login [username]: \033[m').strip()

	if input == 'admin':
		while True:
			password = raw_input('\033[32;1mUser password: \033[m').strip()
			if len(password) == 0:continue

			if password == 'admin':
				print '+++++++++++++++++++++++++++++++'
				print '+  Welcome to inquiry system  +'
				print '+++++++++++++++++++++++++++++++'

				while True:
					user_input = raw_input('\033[32;1mSelect model [ sea/add/mod/del ]: \033[0m').strip()
						
					if len(user_input) == 0:continue
					if user_input == 'exit' :
						sys.exit()

					elif user_input == 'sea' :   # 查询模式
						f = open(con_list)
						c = f.readlines()
						while True :
							search_str = raw_input('\033[32;1mInput sth to search  : \033[0m').strip()
							if len(search_str) == 0:continue
							match=0
							for line in c:
								list = line.split()
								if search_str == list[3] or\
   	                        	search_str == list[1] or\
   	                        	search_str == list[2] :
									print '\033[35;1m%s\033[0m' % line.strip('\n')
									match=1
								
							if  search_str == 'exit':
										break
									
							if match == 0: print '\033[31;1m Sorry, %s is not found ! \033[0m' % search_str

					elif user_input == 'add':    # 添加模式
						print '---------------------------'
						print '格式:  name     dp     tel '
						print '---------------------------'
						while True :
							add_str    = raw_input('\033[32;1mInput sth to add  : \033[0m').strip()
							if len(add_str) == 0:continue
							if add_str == 'exit':
								break
							if len(add_str.split()) == 3 :
								f = open(con_list)
								c = f.readlines()
								sn = len(c) + 1
								f.close()
								f = open(con_list,'a')
								f.write('%d	%s\n' % (sn,add_str))
								f.close()
								print ''
								print '添加数据 [ id :%d %s ] 成功 ..' % (sn,add_str)
								print ''
							else:
								print '\033[31;1m 请使用正确的格式添加数据. \033[0m'
								print '---------------------------'
								print '格式:  name     dp     tel '
								print '---------------------------'
					elif user_input == 'mod':   # 修改模式
						while True:
							line_str = raw_input('\033[32;1mInput number of line which you want to modify  : \033[0m').strip()
							if line_str == 'exit': break
							if len(line_str) == 0: continue
							f = open(con_list)
							c = f.readlines()
							f.close()
							count_line = len(c)
							items = []
							for i in range(1,count_line+1):
								items.append(str(i))	
							if line_str in items:
								line_num = int(line_str)
								while True:
									mod_type = raw_input('\033[32;1mChoose mod (line/field)  : \033[0m').strip()
									if len(mod_type) == 0: continue
									if mod_type == 'exit': break
									elif mod_type == 'line':			#修改整行
										print '\033[31;1m 修改整行数据格式. \033[0m'
										print '---------------------------'
										print '格式:  name     dp     tel '
										print '---------------------------'
										while True:
											mod_str=raw_input('\033[32;1mPlease Input information : \033[0m').strip()
											if len(mod_str) == 0: continue
											if mod_str == 'exit': break
											items_num = len(mod_str.split())
											if items_num == 3:
												c[line_num - 1] = '%d		%s\n' % (line_num,mod_str)
												f = open(con_list,'w')
												f.writelines(c)
												f.close()
												print '\033[31;1m%s  is modify \033[0m' % c[line_num - 1].strip('\n')
											else:
												print '请输入正确的格式'
									elif mod_type == 'field':			#修改单独列 
										while True:
											mod_info=raw_input('\033[32;1mchoose field(name/dp/tel) : \033[0m').strip()
											if len(mod_info) == 0: continue
											if mod_info == 'exit': break
											elif mod_info == 'name':
												while True:
													new_field=raw_input('\033[32;1mInpt New name : \033[0m').strip()
													if len(new_field) == 0: continue
													if new_field == 'exit': break
													else:
														fields = c[line_num -1].split()
														fields[1] = new_field
														fields.append('\n')
														c[line_num -1] = "\t".join(fields)	
														
														f = open(con_list,'w')
														f.writelines(c)
														f.close
														print '%s' % c[line_num -1]
											elif mod_info == 'dp':
												while True:
													new_field=raw_input('\033[32;1mInpt New dp : \033[0m').strip()
													if len(new_field) == 0: continue
													if new_field == 'exit': break
													else:
														fields = c[line_num -1].split()
														fields[2] = new_field
														fields.append('\n')
														c[line_num -1] = "\t".join(fields)	
														
														f = open(con_list,'w')
														f.writelines(c)
														f.close
														print '%s' % c[line_num -1]
											elif mod_info == 'tel':
												while True:
													new_field=raw_input('\033[32;1mInpt New Tel : \033[0m').strip()
													if len(new_field) == 0: continue
													if new_field == 'exit': break
													else:
														fields = c[line_num -1].split()
														fields[3] = new_field
														fields.append('\n')
														c[line_num -1] = "\t".join(fields)	
														
														f = open(con_list,'w')
														f.writelines(c)
														f.close
														print '%s' % c[line_num -1]
							else:
								print '\033[31;1m@_@ 未找到第%s行,请输入正确的行号.\033[0m' % line_str

					elif user_input == 'del':   # 删除模式
						while True:
							del_line =raw_input('\033[32;1mInput del Line num : \033[0m').strip()							
							if len(del_line) == 0: continue
							if del_line == 'exit': break
							f = open(con_list)
							c = f.readlines()
							f.close()
							count_line = len(c)
							items = []
							for i in range(1,count_line+1):
								items.append(str(i))
							if del_line in items:
								line_num = int(del_line)
								del c[line_num -1]
								sn = 1
								for line in c:
									fields = line.split()
									fields[0] = str(sn)
									fields.append('\n')
									c[sn-1] = '\t'.join(fields)
									sn += 1
								f = open(con_list,'w')
								f.writelines(c)
								f.close()
								print '\033[36;1m ### Line %d is delete success.. \033[0m' % line_num
							else:
								print '\033[31;1m line %s not found ! \033[0m' % del_line
					else:
						print '\033[31;1m Error choose %s \033[0m' % user_input		
			else:
				print '\033[31;1m Password Error, please try again. \033[0m'
				continue

	else:
		print '\033[31;1mNo such user %s !!!\033[0m' % input
   
