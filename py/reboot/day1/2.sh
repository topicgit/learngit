DATE=`date -I|sed 's/-//'`

mkdir -p /home/hf/data_bak_${DATE}

if [[ -d /home/hf/data_bak_${DATE} ]];then
    echo "数据库备份目录创建成功！"
else
    echo "数据库备份目录创建失败！"
    exit
fi
find /home/hf -name "hf_S*" -type d >/home/hf/file

if [[ -f /home/hf/file ]];then
    echo "合服目录读取成功！"
else
    echo "合服目录读取失败！"
    exit
fi

NAME=`cat /home/hf/file |cut -d "/" -f4 |cut -d "_" -f3|sed 's/-//'`

if [[ ${DATE} -eq ${NAME} ]];then
   echo "合服目录正确！"
else
   echo "合服目录错误！"
   exit
fi
