#!/usr/bin/evn python
# -*- coding: utf-8 -*-

def load_stat():
    loadavg = {}
    f = open('/proc/loadavg')
    con = f.read().split()
    f.close
    loadavg['lavg_1']=con[0]
    loadavg['lavg_5']=con[1]
    loadavg['lavg_15']=con[2]
    loadavg['nr']=con[3]
    loadavg['last_pid']=con[4]
    return loadavg

info = load_stat()
print  'load average: %s %s %s ' % (info['lavg_1'],info['lavg_5'],info['lavg_15'])

