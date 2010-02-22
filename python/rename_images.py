#!/usr/bin/env python
#
# Renames all files in a directory changing certain character sequences:
# " (" to "_"
# ")" to ""
import optparse
import os

def main():
  p = optparse.OptionParser()
  options, arguments = p.parse_args()
  
  directory = arguments[0]
  files = os.listdir(directory)
  
  for item in files:
    oldfile = open(directory+'/'+item, mode='r')
    newfilename = item.replace(' (', '_')
    newfilename = newfilename.replace(')', '')
    os.rename(directory+'/'+item, directory+'/'+newfilename)
    print newfilename

if __name__ == '__main__':
  main()
