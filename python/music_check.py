#!/usr/bin/env python
import os
import optparse

class MusicCollectionCheck:
    diff_files = []
    
    def __init__(self, external_dir, local_dir):
        self.external_dir = external_dir
        self.local_dir = local_dir
        self.small_external = False
    
    def add_small_external(self, small_external):
        self.small_external = small_external
    
    def nav_dir(self, dirname):
        for item in os.listdir(dirname):
            if os.path.isdir(item):
                self.nav_dir(item)
            else:
                self.check_file(item)
    
    def check_file(self, item):
        if not os.path.exists(self.local_dir+item):
            self.diff_files.append(self.external_dir+item)
        if self.small_external:
            if not os.path.exists(self.small_external+item):
                self.diff_files.append(self.external_dir+item)
    
    def print_list(self):
        self.nav_dir(self.external_dir)
        self.diff_files.sort()
        for item in self.diff_files:
            print item


if __name__ == '__main__':
    p = optparse.OptionParser()
    options, arguments = p.parse_args()
    
    if len(arguments) < 2:
        print "usage: python music_check.py <external dir> <local dir> <smaller external dir - optional>"
    
    mc = MusicCollectionCheck(arguments[0], arguments[1])
    if len(arguments) == 3:
        mc.add_small_external(arguments[3])
    mc.print_list()

