tgtadm --lld iscsi --mode target --op new --targetname iqn.2015-04.com.jie:tstore.disk1 --tid 1
tgtadm --lld iscsi --mode logicalunit --op new --tid 1 --lun 1 --backing-store /dev/sdb
tgtadm --lld iscsi --mode target --op bind --tid 1 --initiator-address 172.16.100.0/24
tgtadm --lld iscsi --op show --mode target
