#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 让用户输入工资.
# 输出购物菜单以及产品价格
# 基数按用户是否可支付
# 输出用户剩余的钱，问用户是否继续购物.
# 如果选择继续，继续进行，直到钱不够为止

import  sys
product = ['Car', 'iphone','coffee','mac','cloths','Bicyle']
price   = [250000,4999,35,9688,438,1500]
shop_list = []

while True:
	try:
		salary = int(raw_input('please input your  salary: '))
		break
	except ValueError:
		print 'Please input a number, not string.'

while True:
	print 'Things have in the shop,please choose one to buy:'
	for p in product:
		print '\033[32;1m%s \t %s \033[0m' % (p, price[product.index(p)])

	choice = raw_input('Please input one item to buy:')
	F_choice = choice.strip()
	if F_choice == 'quit':
		print '\033[36;1m\nyou have bought these things: %s \033[0m' % shop_list
		sys.exit()

	if F_choice in product:
		product_price_index = product.index(F_choice)
		product_price = price[product_price_index]
		print '%s $%s' %(F_choice,product_price)
	
		if salary > product_price:
			shop_list.append(F_choice)
			print 'Added %s into your shop list' % F_choice
			salary = salary - product_price
			print 'Salary left: $',salary
		else:
			if salary < min(price):
				print '%s %s' % (salary, min(price))
				print 'Sorry,rest of your salary cannot buy anything. bye'
				print '\033[31;1myou have bought thest things: %s \033[0m' % shop_list
				sys.exit()
			else:
				print '\033[31;1mSorry, you cannot afford this product,please try other ones\033[0m'
