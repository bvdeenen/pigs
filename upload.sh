#!/bin/bash


set -x

FTP_HOST=192.168.1.$1
FTP_LOGIN=micro
FTP_PASSWORD=python

ftp -i -n <<EOF
open $FTP_HOST
user $FTP_LOGIN $FTP_PASSWORD
passive
cd /flash/lib
put $2
ls 
quit
EOF
