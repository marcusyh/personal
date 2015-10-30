title: "Debian"
date: 2015-05-27 18:46:06
tags:
---
##Debian Jessie Wireless on Thinkpad X86s 
[remove linux-wlan-ng and linux-wlan-ng-firmware packages](http://www.funtoo.org/Zero_Configuration_Networking)

[Install iwlegacy by apt-get install firmware-iwlwifi](https://wiki.debian.org/iwlegacy)

[make sure the protocol is correct, it maybe wpa or wpa2](http://linux.hd-wireless.se/bin/view/Linux/WPASupplicant)

Notes:
Also a knowledge that [avahi-autoipd](http://linux.die.net/man/8/avahi-autoipd), [Avahi](https://wiki.archlinux.org/index.php/Avahi), [Zero-configuration networking](http://en.wikipedia.org/wiki/Zero-configuration_networking)

##Brightness for Hasee K650D i5 D2 (Clevo W650SJ infact):
[Backlight](https://wiki.archlinux.org/index.php/Backlight)

##Ethernet Card for Hasee K650D i5 D2 (Clevo W650SJ infact):

1) Check to see if the r8169 module is loaded
-> lsmod | grep r816
r8168 41104 0
-> lspci -v
01:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168B PCI Express Gigabit Ethernet controller (rev 03)
Subsystem: ASRock Incorporation Device 8168
Kernel driver in use: r8169
Kernel modules: r8169

2) Download the official Realtek driver [Realtek RTL8111/RTL8168i Driver](http://www.realtek.com.tw/downloads/downloadsView.aspx?Langid=1&PNid=13&PFid=5&Level=5&Conn=4&DownTypeID=3&GetDown=false#2)

3) Remove the r8169 module
-> rmmod r8169
-> mv /lib/modules/`uname -r`/kernel/drivers/net/r8169.ko ~/r8169.ko.backup
( the ` is a backtick, it is not an apostrophe or single quote )

4) Build the new r8168 module for the kernel
-> bzip2 -d r8168-8.009.00.tar.bz2
-> tar -xf r8168-8.009.00.tar
-> cd r8168-8.009.00
-> make clean modules
-> make install

5) Rebuild the kernel module dependencies
-> depmod -a
-> insmod ./src/r8168.ko

6) Remove the r8169 module from initrd
-> mv /initrd.img ~/initrd.img.backup
-> mkinitramfs -o /boot/initrd.img-`uname -r` `uname -r`

7) Add r8168 module to /etc/modules
-> echo "r8168" >> /etc/modules

8) Reboot, You are done!

9) Examine that ONLY the r8168 module is loaded for the interface
-> lspci -v
01:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168B PCI Express Gigabit Ethernet controller (rev 03)
Subsystem: ASRock Incorporation Device 8168
Kernel driver in use: r8168
Kernel modules: r8168

If you need to, configure your /etc/network/interfaces for dhcp or static address then `sudo ifup eth0`

Reference Links:
[SOLVED: Realtek r8168/r8169 no Ethernet!](http://forums.debian.net/viewtopic.php?f=5&t=104167)
[The pain of an Realtek (RTL8111/RTL8168) ethernet card](https://unixblogger.wordpress.com/2011/10/18/the-pain-of-an-realtek-rtl8111rtl8168-ethernet-card/)
[RTL8111/RTL8168 Network Connection Fix](http://ubuntuforums.org/archive/index.php/t-1022411.html)
[Jessie Realtek ethernet driver install](http://www.debianuserforums.org/viewtopic.php?f=56&t=3356)


## Debian Jessie on other machines:
[Debian Jessie on Thinkpad X240](http://www.gnusosa.net/article/x240-debian-jessie.html)
[Installing Debian Jessie On Thinkpad T450s](https://wiki.debian.org/InstallingDebianOn/Thinkpad/T450s/jessie)


