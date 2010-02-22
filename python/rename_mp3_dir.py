#!/usr/bin/env python
import os
import sys
import optparse
import re
import eyeD3
import shutil

def rename_dir(dir):
    dir_contents = os.listdir(dir)
    newname = ''
    for file in dir_contents:
        f = os.popen('file '+re.escape(dir+'/'+file), 'r')
        ftype = f.read()
        if ftype.find('ID3') > 0 and ftype.find('MP3') > 0:
            tag = eyeD3.Tag()
            tag.link(dir+'/'+file, eyeD3.ID3_V2)
            if tag.getYear() != '' and tag.getAlbum() != '':
                newname = tag.getYear()+" - "+tag.getAlbum()
                break
    if newname != '':
        os.rename(dir, newname)
        try:
            os.mkdir(tag.getArtist())
        except OSError:
            pass
        os.system("mv "+re.escape(newname)+" "+re.escape(tag.getArtist()))
        print "directory renamed to "+newname+" and moved to "+tag.getArtist()
        print os.listdir(tag.getArtist()+"/"+newname)

if __name__ == '__main__':
    p = optparse.OptionParser()
    options, arguments = p.parse_args()
    
    if len(arguments) < 1:
        print "usage: python rename_mp3_dir.py <dir>"
    
    rename_dir(arguments[0])

