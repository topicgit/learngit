#!/bin/bash


stamp=`date +%Y%m%d%H%M`
year=`echo $stamp|cut -c 1-4`
month=`echo $stamp|cut -c 5-6`
day=`echo $stamp|cut -c 7-8`
hour=`echo $stamp|cut -c 9-10`
min=`echo $stamp|cut -c 11-12`


echo '-------------------------'
echo  -n "$year年"
echo  -n "$month月"
echo  -n "$day日"
echo  -n " $hour时"
echo "$min分"
echo '-------------------------'
