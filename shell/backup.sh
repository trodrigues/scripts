#!/bin/sh

#
# trodrigues backup script v0.1
#
# A script for daily backups with rsync
#

TO_BACKUP="/home"
BACKUP_DIR="/media/exthd2"
ECHO=1

date > $BACKUP_DIR/last_backup.txt

for i in $TO_BACKUP ; do
	if [ $ECHO -eq 1 ] ; then echo "Backing up $i:\n" ; fi
	if [ $ECHO -eq 1 ] ; then
		rsync -avz $i $BACKUP_DIR
	else
		rsync -avz $i $BACKUP_DIR > /dev/null 2>&1
	fi
	if [ $ECHO -eq 1 ] ; then echo "\tdone.\n\n" ; fi
done
#!/bin/sh

backupdir=/media/exthd2

rsync -avz / --exclude /media/exthd2 --exclude /media/exthd1 --exclude /tmp/ --exclude /dev/ --exclude /proc/ --exclude  /sys --exclude /windows $backupdir


mkdir $backupdir/media/exthd1
mkdir $backupdir/media/exthd2
mkdir $backupdir/tmp
mkdir $backupdir/dev
mkdir $backupdir/proc
mkdir $backupdir/sys
mkdir $backupdir/windows
