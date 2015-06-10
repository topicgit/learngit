#!/bin/bash

show_usage() {

	cat << EOF
--------------------------------
Usages:
	d|D) show disk usages
	m|M) show memory usages
	s|S) show swap usages
	q|Q) quit
--------------------------------
EOF

}

show_usage
read -p "You choice : " CHOICE

until [ $CHOICE == 'q' -o $CHOICE == 'Q' ];
do
	case $CHOICE in 
		d|D) df -h ;;
		m|M) free -m|grep '^Mem' ;;
		s|S) free -m|grep '^Swap' ;;
		  *) echo "Input Error , again !";
			 show_usage
             read -p "You choice : " CHOICE
	esac

	show_usage
	read -p "You choice : " CHOICE
done
