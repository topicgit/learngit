#########################################################################
# File Name: innobak.sh
# Author: Tempo
# mail: wodetempo@163.com
# Created Time: 2015年01月27日 星期二 22时30分14秒
#########################################################################
#!/bin/bash

# 脚本使用innobackupex导出三个数据库，必须定义导出的目录
# 定义导出目录
EXP_DIR=/data/db

EXP_LOG=$EXP_DIR/expdb.log
CMD='/usr/local/eyou/mail/opt/xtrabackup/bin/innobackupex'
Eyou_sql_etc='/usr/local/eyou/mail/etc/mysql'

exp_mysql() {
	$CMD --user=eyou --password=eyou \
	--defaults-file=$Eyou_sql_etc/my.cnf \
	--slave-info --no-timestamp $EXP_DIR/mysql 
}

exp_mysql_index() {
	$CMD --user=eyou --password=eyou \
	--defaults-file=$Eyou_sql_etc/my_index.cnf \
	--slave-info --no-timestamp $EXP_DIR/mysql_index 
}

exp_mysql_log() {
	$CMD --user=eyou --password=eyou \
	--defaults-file=$Eyou_sql_etc/my_log.cnf \
	--slave-info --no-timestamp $EXP_DIR/mysql_log 
}

apply_log() {
	$CMD --apply-log $EXP_DIR/mysql
	$CMD --apply-log $EXP_DIR/mysql_index
	$CMD --apply-log $EXP_DIR/mysql_log
}


run_exp() {
	echo
	echo -e " >>> logfile: $EXP_DIR/expdb.log"
	echo
	echo " >>> $(date '+%F %-H:%-M:%-S') Start  Export   Mysql_DB ..."
	exp_mysql  >> $EXP_LOG 2>&1
	echo " >>> $(date '+%F %-H:%-M:%-S') Export Mysql_DB Success ..."

	echo
	echo " >>> $(date '+%F %-H:%-M:%-S') Start  Export   Index_DB ..."
	exp_mysql_index  >> $EXP_LOG 2>&1
	echo " >>> $(date '+%F %-H:%-M:%-S') Export Index_DB Success ..."

	echo
	echo " >>> $(date '+%F %-H:%-M:%-S') Start  Export   Log_DB ..."
	exp_mysql_log  >> $EXP_LOG 2>&1
	echo " >>> $(date '+%F %-H:%-M:%-S') Export Log_DB   Success ..."
	echo

}

show_pos() {

	[ -f $EXP_DIR/mysql/xtrabackup_binlog_info ] && {
		m1=`awk '{printf ("%-20s %-19s",$1"  |",$2)}' $EXP_DIR/mysql/xtrabackup_binlog_info`
		I1=`awk '{printf ("%-20s %-19s",$1"  |",$2)}' $EXP_DIR/mysql_index/xtrabackup_binlog_info`
		L1=`awk '{printf ("%-20s %-19s",$1"  |",$2)}' $EXP_DIR/mysql_log/xtrabackup_binlog_info`
		echo -e "----------------------------------------------------"
		echo -e "|   DB   |       BINLOG      |      POS            |"
		echo -e "----------------------------------------------------"
		echo -e "| Mysql  | $m1|"
		echo -e "----------------------------------------------------"
		echo -e "| Index  | $I1|"
		echo -e "----------------------------------------------------"
		echo -e "| Logdb  | $L1|"
		echo -e "----------------------------------------------------"
		} || echo -e  " >>> 未发现文件 xtrabackup_binlog_info ,请您先使用exp进行导出."
}


show_help() {

	cat << EOT
	
	-----------------------------------------------------
	Usage : sh `basename $0` exp     # 导出所有数据库
	        sh `basename $0` spos    # 查看binlog/POS值
	        sh `basename $0` alog    # 回滚日志至数据文件
	-----------------------------------------------------

EOT
}

[ $# != 1 ] && {
    show_help;exit 0
}

case $1 in 
	"exp")
	run_exp
	;;
	"alog")
	apply_log
	;;
	"spos")
	show_pos
	;;
	*)
    show_help;exit 0
	;;
esac

