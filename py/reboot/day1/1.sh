DATE=`date -I`
mkdir -p /home/hf/hf_S10_`date -I`

NAME=`cat /home/hf/file |cut -d "/" -f4 |cut -d "_" -f3`
echo $NAME

check() {
if [[ ${DATE} -eq ${NAME} ]];then
        echo "合服目录正确！"
else
        echo "合服目录错误！"
        exit
fi
}

[ -f /home/hf/file ] && check || echo "No file /home/hf/file"
