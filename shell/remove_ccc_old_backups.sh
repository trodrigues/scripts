#!/bin/bash

BACKUP_PATH="/Volumes/OSX Backup"
CCC_ARCHIVE_PATH="$BACKUP_PATH/_CCC Archives"
PWD=`pwd`

if [ -d "$BACKUP_PATH" ] ; then
    if [ -d "$CCC_ARCHIVE_PATH" ] ; then
        lines=`ls -l "$CCC_ARCHIVE_PATH/"|wc -l`
        if [ $lines -gt 10 ] ; then
            dir_to_remove=`ls -l "$CCC_ARCHIVE_PATH/"|head -n 2|tail -n 1|cut -c 46-`
            if [ "$dir_to_remove" != "" ] ; then
                echo "removing $CCC_ARCHIVE_PATH/$dir_to_remove"
                rm -rf "$CCC_ARCHIVE_PATH/$dir_to_remove"
            fi
        fi
    fi
fi

cd $PWD
exit 0
