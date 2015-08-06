#!/usr/bin/expect
set timeout 10
set USERNAME root
set PASSWORD eqwrfds
spawn su - root
expect {
            "password:" {send "acdde-052%\r"}
}
expect "]*"
send "passwd ${USERNAME}\r"
expect "password:"
send "${PASSWORD}\r"
expect "password:"
send "${PASSWORD}\r"
expect "]*"
send "exit\r"

