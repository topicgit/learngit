#!/bin/bash
PING() {

	if ping -c 1 -W 1 $1 &> /dev/null;then
		return 0
	else
		return 1
	fi
}


for i in {100..124};
do
	PING 172.16.100.$i
	if [ $? -eq 0 ];then
		echo -e "\033[32;1m 172.16.100.$i is up.\033[0m"
	else
		echo -e "\033[31;1m 172.16.100.$i is down.\033[0m"
	fi

done
