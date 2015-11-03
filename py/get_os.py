#!/usr/bin/env python
# -*- coding:utf-8 -*-

# This script is for statistical system information, such as CPU model, CPU
# usage, memory information, memory usage, disk information, system running
# status

import os
import platform
from   collections import OrderedDict

def os_version():
    Info=platform.uname()
    distr=platform.linux_distribution()
    print '-' * 50
    print u" OS     类型 : %s "  % Info[0]
    print u" OS     版本 : %s_%s_%s "  % (distr[0],distr[1],distr[2])
    print u" OS   主机名 : %s " % Info[1]
    print u" OS 内核版本 : %s "  % Info[2]
    print ''

def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

""" print out the /proc/cpuinfo
    file
    """
def cpuinfo():

    cpuinfo=OrderedDict()
    procinfo=OrderedDict()

    nprocs=0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                cpuinfo['porc%s' % nprocs] = procinfo
                nprocs=nprocs+1
                procinfo=OrderedDict()
            else:

                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()]=line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''

    return cpuinfo

def load_stat():
    loadavg = {}
    f = open("/proc/loadavg")
    con=f.read().split()
    f.close()
    loadavg['lavg_1']=con[0]
    loadavg['lavg_5']=con[1]
    loadavg['lavg_15']=con[2]

    return loadavg


def uptime_stat():
    uptime = {}
    f = open('/proc/uptime')
    ut=f.read().split()
    f.close()

    all_sec=float(ut[0])
    MINUTE,HOUR,DAY = 60,3600,86400
    uptime['day'] = int(all_sec / DAY)
    uptime['hour'] = int((all_sec % DAY ) / HOUR)
    uptime['minute'] = int((all_sec % HOUR) / MINUTE)
    uptime['second'] = int(all_sec % MINUTE)
    uptime['Free rate'] = float(ut[1]) / float(ut[0])
    return uptime

"""
List of all process IDs currently active
"""
def process_list():
    pids=[]
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)

    return pids



if __name__ == '__main__':

    os_version()
    cpuinfo = cpuinfo()
    for processor in cpuinfo.keys():
         print "Cpu  ___型号 : %s" % (cpuinfo[processor]['model name'])
         break

    ln=len(cpuinfo)
    print 'Cpu逻辑核心数: %s\n' % ln

    meminfo=meminfo()
    total=int(meminfo['MemTotal'].split()[0])
    free=int(meminfo['MemFree'].split()[0])
    buffers=int(meminfo['Buffers'].split()[0])
    cached=int(meminfo['Cached'].split()[0])
    swap=int(meminfo['SwapTotal'].split()[0])
    MEMUsedPerc=100 * float('%0.2f' % (float(total-free-buffers-cached)/total))

    print '''内存使用情况 :
               内存使用率   : %s%%
               物理内存     : %s M
               空闲内存     : %s M 
               Swap 总空间  : %s M\n'''  %  (MEMUsedPerc,total/1024,free/1024,swap/1024)

    up_stat = uptime_stat()
    print '系统运行时间 : %s天%s小时%s分%s秒' \
         % (up_stat['day'],up_stat['hour'],\
            up_stat['minute'],up_stat['second'])
    print '服务器空闲率 : %s%%' % (float('%0.2f'%up_stat['Free rate'])*100)
    load=load_stat()
    print 'load average : %s | %s | %s' % \
          (load['lavg_1'],load['lavg_5'],load['lavg_15'])
    pids = process_list()
    print 'OS 总进程数  : %s' % (len(pids))

    print '-' * 50



