#!/bin/bash
# In The Name Of God
# ========================================
# [] File Name : raspbian.sh
#
# [] Creation Date : 16-07-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
download=true
if [ -f raspbian-jessie-lite.zip ]; then
	read -p "Do you want to redownload raspbian ?[Y/n] " -n 1 redownload; echo
	if [[ $redownload == "Y" ]]; then
		download=true
		rm rasbian-jessie-lite.zip
	else
		download=false
	fi
fi
if $download ; then
	echo "Downloading raspbian ..."
	curl --progress-bar --location https://downloads.raspberrypi.org/raspbian_lite_latest -o raspbian-jessie-lite.zip
	if [[ $? -eq 0 ]]; then
		echo "Download has been successful"
	else
		echo "Download has been failed"
		exit
	fi
fi
oPS3=$PS3
PS3="Please select a device [ENTER to list devices]:"
select dev in `ls /dev/mmcblk[0-9]`; do
	if [ ! -z "$dev" ]; then
		echo "you select $dev"
		break
	else
		echo "$REPLY is not valid option"
	fi
done
PS3="What do you want to do with $dev [ENTER to list options]:"
select option in "fdisk" "install-raspbian" "quit"; do
	if [ ! -z "$option" ]; then
		case $REPLY in
			1)
				sudo fdisk -l $dev
				;;
			2)
				sudo unzip -p raspbian-jessie-lite.zip | sudo dd of=$dev bs=32M
				break
				;;
			3)
				break
				;;
		esac
	else
		echo "$REPLY is not valid option"
	fi
done
PS3=$oPS3
