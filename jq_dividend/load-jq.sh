#!/bin/bash
log_file=/home/www/jukuan/log/jq_`date +"%Y_%m_%d_%H"`.log
/usr/local/bin/python3 /home/www/jukuan/xt-jqdata.py >>$log_file
