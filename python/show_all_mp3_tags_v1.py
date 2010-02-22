#!/usr/bin/env python
import os
import sys
import optparse
import re
import eyeD3
import locale
locale.setlocale(locale.LC_NUMERIC, "")

def format_num(num):
    """Format a number according to given places.
    Adds commas, etc. Will truncate floats into ints!"""

    try:
        inum = int(num)
        return locale.format("%.*f", (0, inum), True)

    except (ValueError, TypeError):
        return str(num)

def get_max_width(table, index):
    """Get the maximum width of the given column index"""
    return max([len(format_num(row[index])) for row in table])

def pprint_table(out, table):
    """Prints out a table of data, padded for alignment
    @param out: Output stream (file-like object)
    @param table: The table to print. A list of lists.
    Each row must have the same number of columns. """

    col_paddings = []

    for i in range(len(table[0])):
        col_paddings.append(get_max_width(table, i))

    for row in table:
        # left col
        print >> out, row[0].ljust(col_paddings[0] + 1),
        # rest of the cols
        for i in range(1, len(row)):
            col = format_num(row[i]).rjust(col_paddings[i] + 2)
            print >> out, col,
        print >> out


def print_tag(tag1, tag2):
    table = [
        [tag1.getArtist(), tag2.getArtist()],
        [tag1.getTitle(), tag2.getTitle()],
        [tag1.getAlbum(), tag2.getAlbum()],
        [tag1.getYear(), tag2.getYear()],
        [str(tag1.getTrackNum()), str(tag2.getTrackNum())]
    ]
    pprint_table(sys.stdout, table)
    print "\n-----\n"


def show_tags(dirpath, dirs, files):
    print dirpath
    for file in files:
        f = os.popen('file '+re.escape(dirpath+'/'+file), 'r')
        ftype = f.read()
        if ftype.find('ID3') > 0 and ftype.find('MP3') > 0:
            tag1 = eyeD3.Tag()
            tag1.link(dirpath+'/'+file, eyeD3.ID3_V1)
            tag2 = eyeD3.Tag()
            tag2.link(dirpath+'/'+file, eyeD3.ID3_V2)
            print_tag(tag1, tag2)
    print "\n*********************************\n\n"


def show_dir(dir):
    for dirpath, dirs, files in os.walk(dir):
        show_tags(dirpath, dirs, files)

if __name__ == '__main__':
    p = optparse.OptionParser()
    options, arguments = p.parse_args()
    
    if len(arguments) < 1:
        print "usage: python show_all_mp3_tags.py <dir>"
    
    show_dir(arguments[0])

