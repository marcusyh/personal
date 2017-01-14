title: "/dev学习笔记"
date: 2017-01-14 05-15-00
tags:
---

The difference between /proc and /sys
[The difference between procfs and sysfs](http://unix.stackexchange.com/questions/4884/what-is-the-difference-between-procfs-and-sysfs) ![/proc and /sys](/img/devfs/sysfs_vs_procfs.jpg)
[/dev, /proc, /sys](http://unix.stackexchange.com/questions/188886/what-is-in-dev-proc-and-sys) ![/proc and /sys and /dev](/img/devfs/devfs_procfs_sysfs.jpg)
[wikipedia: Device file](https://en.wikipedia.org/wiki/Device_file)
[wikipedia: procfs](https://en.wikipedia.org/wiki/Procfs)
[wikipedia: tmpfs](https://en.wikipedia.org/wiki/Tmpfs)
[wikipedia: sysfs](https://en.wikipedia.org/wiki/Sysfs)

What are those /dev/ Files?
[What are those /dev/ Files?](http://www.linux.org/threads/what-are-those-dev-files.4713/)


A device file or special file is **an interface for a device driver** that appears in a file system **as if it were an ordinary file**, it allow software to interact with a device driver using standard input/output system calls, which simplifies many tasks and unifies user-space I/O mechanisms.

**Linux Device List** [16 commands to check hardware information on Linux](http://www.binarytides.com/linux-commands-hardware-info/)
udev [wikipedia](https://en.wikipedia.org/wiki/Udev) [archlinux](https://wiki.archlinux.org/index.php/udev)


tty, pty, pts, ptmx, console, xconsole
man 4 pts
[wikipedia: devpts](https://en.wikipedia.org/wiki/Devpts)
[Pseudoterminal](https://en.wikipedia.org/wiki/Pseudoterminal)
[tty/pty/pts/ptmx详解](http://www.51testing.com/html/44/175444-81943.html)
[Linux Containers, /dev/pts/ptmx, and Gentoo](https://www.preney.ca/paul/archives/212)

ls --ignore={sda,tty,vbox,vcs,loop}*
