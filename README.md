# ITSummEL
## Introduction
Story of our works in IoT Academy in [ITRC](http://itrc.ac.ir) at Summer 2016.
## Steps
### RPi Configuration
For installing Lamp-RPi on RPi (Automated):
- Donwload Raspbian [here](https://www.raspberrypi.org/downloads/raspbian/)
- Install Raspbian on SDcard with `unzip -p 2016-03-18-raspbian-jessie.zip | sudo dd of=/dev/mmcblk0 bs=32M`
After installation if you want you can grow your partition size:
- Run `fdisk /dev/mmcblk0p2`
- Check the partition number you wish to delete with the p.
- Use the option d to delete a partition. If there is more than one, **fdisk** will prompt for which one to delete.
-
