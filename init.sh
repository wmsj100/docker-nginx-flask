#! /bin/sh
#
# init.sh
# Copyright (C) 2020 wmsj100 <wmsj100@ArchLinux>
#
# Distributed under terms of the MIT license.
#

if [ -d webapp ];then
	mkdir -p webapp/log
	touch webapp/log/app.log
	echo "Init success!!!"
else
	echo "error path, please exec init.sh in the root path"
fi
