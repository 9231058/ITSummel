#!/bin/bash
# In The Name Of God
# ========================================
# [] File Name : raspbian.sh
#
# [] Creation Date : 16-07-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
echo "Downloading raspbian ..."
curl --progress-bar --location https://downloads.raspberrypi.org/raspbian_lite_latest -o raspbian-jessie-lite.zip
if [[ $? -eq 0 ]]; then
	echo "Download has been successful"
else
	echo "Download has been failed"
	exit
fi
