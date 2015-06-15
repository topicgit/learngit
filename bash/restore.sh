#!/bin/bash

MYSQL='/usr/local/eyou/mail/opt/mysql/bin/mysql -h 127.1  -D eyou_mail'

$MYSQL -s -e "select concat(acct_name,'@',domain_name) from acct_key,domain_key where acct_key.domain_id=domain_key.domain_id and acct_key.acct_type=0 and domain_key.domain_id in (select domain_id from domain_key); " > /tmp/userlist

echo "---------------------------------------------------"

[[ $?  -eq 0 ]] && echo -e  ">>> \033[32;1mExport userlist successd .\033[0m" || echo " >>> Export userlist Fail, exit."

echo
echo ">>> Start restore user [ File: /tmp/userlist ] "
echo

[ -f /tmp/userlist ] &&  while read line;

do

echo -e ">>> restore \033[34;1m$line \033[0m: "
echo -n ">>> result: ";sudo -u eyou /usr/local/eyou/mail/sbin/em_member_restore user $line

done  < /tmp/userlist

echo
echo -e  ">>> \033[32;1mAll user restore Done ...\033[0m"
echo "---------------------------------------------------"
