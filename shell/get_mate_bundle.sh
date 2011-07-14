#!/bin/sh

cd /Library/Application\ Support/TextMate/Bundles

case "$1" in
    install)
        echo "Choose a bundle:"
        echo "http://svn.textmate.org/trunk/Bundles/"
        echo "and type the bundle name to install."
        read name
        svn co http://svn.textmate.org/trunk/Bundles/"$name".tmbundle
    ;;
    
    update)
        svn up *.tmbundle
    ;;
esac

osascript -e 'tell app "TextMate" to reload bundles'