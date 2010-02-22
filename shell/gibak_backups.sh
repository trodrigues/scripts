#!/bin/bash

backupdir="/media/backups"

if [ `whoami` != "root" ] ; then
	echo "You gotta be root !"
	exit
fi

if [ `mount|grep $backupdir|wc -l` -eq 0 ] ; then
    mount $backupdir
fi

if [ `mount|grep $backupdir|wc -l` -eq 0 ] ; then
    notify-send -t 36000000 -u critical "Backup warning" "Your external hardrive is not mounted. Please mount it and rerun this script"
    exit 0
fi

notify-send -t 30000 "Backups are being made" "Do not turn off your external hard drive"

apt-get clean

#cd /
#ln -s $backupdir/system .git
#gibak commit
#rm -f /root/.git

cd /home/trodrigues
ln -s $backupdir/homedir /home/trodrigues/.git
if [ "$1" = "commit" ] ; then
		su trodrigues -c "gibak commit"
else
    git $1
fi
rm -f /home/trodrigues/.git

for i in $backupdir/media/maxtor1 $backupdir/media/maxtor2 $backupdir/media/hitachi $backupdir/media/nokia ; do
    if [ ! -d $i ] ; then
				echo "making dirs"
        #mkdir $i
    fi
done

umount $backupdir

notify-send -t 30000 "Backups finished" "Remember that virtual machines are not backed up automatically"
