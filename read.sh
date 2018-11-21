#!/bin/bash
cat a.txt |while read line
do
	url_s=$line
	echo $url_s
	curl $url_s >> content.txt
done