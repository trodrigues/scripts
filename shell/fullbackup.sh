#!/bin/sh

if [ `whoami` != "root" ] ; then
	echo "You gotta be root !"
	exit
fi

backupdir=/media/backups
backuppath=$backupdir/system/

if [ `mount | grep $backupdir | wc -l` -eq 0  ] ; then
	mount $backupdir
fi

if [ `mount | grep $backupdir | wc -l` -eq 0  ] ; then
  exit
fi

rsync -avzh --force --ignore-errors \
	--exclude /media \
	--exclude /tmp \
	--exclude /dev \
	--exclude /proc \
	--exclude /sys \
	--exclude /var/tmp \
	--exclude /home/trodrigues/music \
	--exclude /home/trodrigues/.gvfs \
	--exclude /home/trodrigues/newmusic \
	/ $backuppath


mkdir $backuppath/tmp
chmod 777 $backuppath/tmp
mkdir $backuppath/dev
chmod 755 $backuppath/dev
mkdir $backuppath/proc
chmod 555 $backuppath/proc
mkdir $backuppath/sys
chmod 755 $backuppath/sys
mkdir $backuppath/var/tmp
chmod 755 $backuppath/var/tmp
mkdir $backuppath/media
chmod 755 $backuppath/media

umount $backupdir
