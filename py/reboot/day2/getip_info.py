#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name : getip_info.py 
# get ip info from http://ip.taobao.com/

import sys
import json
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')

# modify api address
url='http://ip.taobao.com/service/getIpInfo.php?ip='

# Function:  Get IP information
def getip(x):
    ipurl = url + x
    ipinfo=urllib2.urlopen(ipurl).read()
    ipdict=json.loads(ipinfo)

    if  ipdict['code'] == 1 :
        print ''
        print '无效的ip地址|获取失败,请重新输入.'
        print ''
    else :
        print ''
        print '---- 获取ip %s 信息成功 : ' % x
        print ' 国家 : %s ' % ipdict['data']['country']
        print ' 区域 : %s ' % ipdict['data']['area']
        print ' 城市 : %s ' % ipdict['data']['city']
        print ' ISP  : %s ' % ipdict['data']['isp']
        print '-------------------------------'

if  len(sys.argv) != 2:
    print "-------------------------------------"
    print "  Usage : %s  ip_address"  % sys.argv[0]
    print "-------------------------------------"
else :
    print ''
    print 'IP数据获取中,请您稍等...'
    getip(sys.argv[1])

