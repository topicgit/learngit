#!/usr/bin/env bash

ps="/usr/local/eyou/mail/bin/em_imapd"
log="/var/log/mon_imap.log"

num=$( ps -eo cmd= | grep -E -o -x "${ps}" | wc -l | grep -E -o "[0-9]+")
if [ ${num} -lt 1 ]  ; then
	eyou_mail start imap
        echo "$(date +%F_%T) : ${ps} not running . restart imap." | tee -a "$log"
else
        echo "$(date +%F_%T) : ${ps} running proces number: $num ... OK" | tee -a "${log}"
fi


retstr=$(telnet localhost 143 | grep -E -o "OK" )
if [ "${retstr}" == "" ]; then
        echo "$(date +%F_%T) : ${ps} running, but service zombie. restart imap." | tee -a "$log"
	ipcs -m | awk '($0~/^0x/ && $6==0) {printf "ipcrm -m %s\n",$2}' | sh 
	ps -ef | grep "em_imapd$" | grep -v grep  | awk '{print $2}'  | xargs kill -9
	eyou_mail start imap
else
        echo "$(date +%F_%T) : ${ps} running. and service return OK ... OK"  | tee -a "${log}"
fi

