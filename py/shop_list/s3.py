#!/usr/bin/env python

products = []
prices   = []

f = file('shops.txt')

for line in f.readlines():
	p     = line.split()[0]
	price = line.split()[1]
	products.append(p)
	prices.append(price)


print products,prices
