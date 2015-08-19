#!/bin/bash
# File : sysinfo.sh
# Date : 2015-08-07
# print system infomation , [ cpu , mem , disk , product name ..]


get_cpu() {

    product=$(dmidecode -t system|grep 'Product Name'|awk -F: '{print $2}')
    Ma=$(dmidecode -t system|grep 'Manufacturer'|awk -F: '{print $2}')
    cpu_mo=$(awk -F: '$0~/name/ && !a[$2]++ {print $2}' /proc/cpuinfo)
    cpu_vn=$(grep "$cpu_mo" /proc/cpuinfo |wc -l)
    cpu_pn=$(grep 'physical id' /proc/cpuinfo |sort|uniq|wc -l)
    
    echo "==================================================================="
    echo
    echo "服务器生产厂商 : $Ma "
    echo "服务器型号     : $product"
    echo "服务器CPU型号  : $cpu_mo"
    echo "逻辑CPU个数    : $cpu_vn"
    echo "物理CPU个数    : $cpu_pn"
    echo
}

get_mem() {

    tot=$(free -m|grep Mem|awk '{print $2}')
    
    if [[ $tot -gt 1024 ]] ; then
        g_tot=$(echo $tot/1024|bc)
        echo -e "服务器内存     : \033[32;1m$g_tot G\033[0m"
        echo
    else
        echo -e "服务器内存     : \033[32;1m$tot M\033[0m"
        echo
    fi

}

get_disk() {
    echo 
    echo "分区挂载信息: "
    df -h
    echo "==================================================================="
}

get_os() {
    kernel=$(uname -r)
    osver=$(head -1 /etc/issue)
    echo "操作系统       : $osver"
    echo "内核版本       : $kernel"

}


get_cpu
get_mem
get_os
get_disk
