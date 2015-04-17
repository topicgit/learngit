#!/usr/bin/env bash

# File : mon_imap.sh
# Date : 2015/03/06

#根据系统修改PATH变量
export PATH="/usr/lib64/qt-3.3/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin"

#载入系统环境变量
. /etc/bashrc
. /root/.bashrc
. /root/.bash_profile


#根据版本修改imap程序路径
ps="/usr/local/eyou/mail/app/bin/em_imapd"

log="/var/log/mon_imap.log"

num=$( ps -eo cmd= | grep -E -o -x "${ps}" | wc -l | grep -E -o "[0-9]+")

if [ ${num} -lt 1 ]  ; then
	eyou_mail start imap
    echo "$(date +%F_%T) : ${ps} not running . restart imap." | tee -a "$log"
else
    echo "$(date +%F_%T) : ${ps} running proces number: $num ... OK" | tee -a "${log}"
fi


retstr=$(nc -w 3 localhost 143 | grep -E -o "OK" )

if [ "${retstr}" == "" ]; then
    echo "$(date +%F_%T) : ${ps} running, but service zombie. restart imap." | tee -a "$log"
	ipcs -m | awk '($0~/^0x/ && $6==0) {printf "ipcrm -m %s\n",$2}' | sh 
	ps -ef | grep "em_imapd$" | grep -v grep  | awk '{print $2}'  | xargs kill -9
	eyou_mail start imap
else
    echo "$(date +%F_%T) : ${ps} running. and service return OK ... OK"  | tee -a "${log}"
fi

