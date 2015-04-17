#########################################################################
# File Name: mconfig.sh
# Author: Tempo
# mail: wodetempo@163.com
# Created Time: 2015年01月22日 星期四 20时39分31秒
#########################################################################
#!/bin/bash

CMD='/usr/local/eyou/mail/sbin/em_mconfig'

get_user_statu() {

	g_ua=$(sudo -u eyou $CMD get-user-config migrate_auth:user:$1)
	g_us=$(sudo -u eyou $CMD get-user-config migrate_set:user:$1)
	echo "================================================================="
	echo -e "获取用户[$1] migrate_auth 状态 :\n  $g_ua "
	echo
	echo -e "获取用户[$1] migrate_set  状态 :\n  $g_us "
	echo "================================================================="
} 


set_user_on() {

	s_uaon=$(sudo -u eyou $CMD set-user-config migrate_auth:user:$1=1)
	echo "================================================================="
	echo -e  "开启用户[$1] migrate_auth 属性 : \n $s_uaon"
	s_uson=$(sudo -u eyou $CMD set-user-config migrate_set:user:$1=1)
	echo
	echo -e "开启用户[$1] migrate_set  属性 : \n $s_uson"
	echo "================================================================="
} 

set_user_off() {

	s_uaoff=$(sudo -u eyou $CMD set-user-config migrate_auth:user:$1=0) 
	echo "================================================================="
	echo -e "关闭用户[$1] migrate_auth 属性 :\n $s_uaoff"
	echo
	s_usoff=$(sudo -u eyou $CMD set-user-config migrate_set:user:$1=0)
	echo -e "关闭用户[$1] migrate_set 属性 :\n $s_usoff"

} 

show_help() {

cat << EOT
    ----------------------------------------------------------------------
	Usage : sh `basename $0` get user@eyou.net  #获取用户的migrate状态
	        sh `basename $0` on  user@eyou.net  #打开用户的migrate状态
	        sh `basename $0` off user@eyou.net  #关闭用户的migrate状态

	migrate状态说明:
	-------------------------------------------------
	|        属性             |   值    |   状态    |
	-------------------------------------------------
	|migrate_auth|migrate_set |   0/1   | 关闭/开启 |
    ----------------------------------------------------------------------
EOT
}


[ $# != 2 ] && {
	show_help;exit 0
}

case $1 in
	"get")
	get_user_statu $2
	;;
	"on")
	set_user_on $2 
	;;
	"off")
	set_user_off $2 
	;;
	*)
	show_help
	exit 0
	;;
esac
