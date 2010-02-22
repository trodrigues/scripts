#!/usr/bin/env python
import os
import sys
import optparse
import re
import eyeD3

import cStringIO,operator

def indent(rows, hasHeader=False, headerChar='-', delim=' | ', justify='left',
           separateRows=False, prefix='', postfix='', wrapfunc=lambda x:x):
    """Indents a table by column.
       - rows: A sequence of sequences of items, one sequence per row.
       - hasHeader: True if the first row consists of the columns' names.
       - headerChar: Character to be used for the row separator line
         (if hasHeader==True or separateRows==True).
       - delim: The column delimiter.
       - justify: Determines how are data justified in their column. 
         Valid values are 'left','right' and 'center'.
       - separateRows: True if rows are to be separated by a line
         of 'headerChar's.
       - prefix: A string prepended to each printed row.
       - postfix: A string appended to each printed row.
       - wrapfunc: A function f(text) for wrapping text; each element in
         the table is first wrapped by this function."""
    # closure for breaking logical rows to physical, using wrapfunc
    def rowWrapper(row):
        newRows = [wrapfunc(item).split('\n') for item in row]
        return [[substr or '' for substr in item] for item in map(None,*newRows)]
    # break each logical row into one or more physical ones
    logicalRows = [rowWrapper(row) for row in rows]
    # columns of physical rows
    columns = map(None,*reduce(operator.add,logicalRows))
    # get the maximum of each column by the string length of its items
    maxWidths = [max([len(str(item)) for item in column]) for column in columns]
    rowSeparator = headerChar * (len(prefix) + len(postfix) + sum(maxWidths) + \
                                 len(delim)*(len(maxWidths)-1))
    # select the appropriate justify method
    justify = {'center':str.center, 'right':str.rjust, 'left':str.ljust}[justify.lower()]
    output=cStringIO.StringIO()
    if separateRows: print >> output, rowSeparator
    for physicalRows in logicalRows:
        for row in physicalRows:
            print >> output, \
                prefix \
                + delim.join([justify(str(item),width) for (item,width) in zip(row,maxWidths)]) \
                + postfix
        if separateRows or hasHeader: print >> output, rowSeparator; hasHeader=False
    return output.getvalue()

# written by Mike Brown
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/148061
def wrap_onspace(text, width):
    """
    A word-wrap function that preserves existing line breaks
    and most spaces in the text. Expects that existing line
    breaks are posix newlines (\n).
    """
    return reduce(lambda line, word, width=width: '%s%s%s' %
                  (line,
                   ' \n'[(len(line[line.rfind('\n')+1:])
                         + len(word.split('\n',1)[0]
                              ) >= width)],
                   word),
                  text.split(' ')
                 )

def wrap_onspace_strict(text, width):
    """Similar to wrap_onspace, but enforces the width constraint:
       words longer than width are split."""
    wordRegex = re.compile(r'\S{'+str(width)+r',}')
    return wrap_onspace(wordRegex.sub(lambda m: wrap_always(m.group(),width),text),width)

import math
def wrap_always(text, width):
    """A simple word-wrap function that wraps text on exactly width characters.
       It doesn't split the text in words."""
    return '\n'.join([ text[width*i:width*(i+1)] \
                       for i in xrange(int(math.ceil(1.*len(text)/width))) ])


def print_tag(tag1, tag2):
    table = [
        ['ID3 v1', 'ID3 v2'],
        [str(tag1.getArtist()), str(tag2.getArtist())],
        [str(tag1.getTitle()), str(tag2.getTitle())],
        [str(tag1.getAlbum()), str(tag2.getAlbum())],
        [str(tag1.getYear()), str(tag2.getYear())],
        [str(tag1.getTrackNum()), str(tag2.getTrackNum())]
    ]
    width=10
    print indent(table, hasHeader=True, separateRows=True, prefix='| ', postfix=' |')
    #print "\n-----\n"


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

