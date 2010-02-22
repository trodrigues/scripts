#!/usr/bin/env python
#
# Goes through all the library pages of last.fm and returns all artists
# 
from os import system
from time import sleep
import re, simplejson, csv

class Lastfm():
    def __init__(self, page):
        self.page = page
        system('wget http://www.last.fm/user/s3phiroth/library?page='+str(page)+'&sortOrder=desc&sortBy=plays&ajax=1')
        
    
    def dump_artists(self, artist_list):
        page = open('library?page='+str(self.page))
        content = page.read()
        r = re.compile(r'<strong class=\"name\">.*<\/strong>')
        strong_strs = r.findall(content)
        artists = [i[21:len(i)-9] for i in strong_strs]
        artist_list.extend(artists)
        return artist_list


if __name__ == '__main__':
    system('wget http://www.last.fm/user/s3phiroth/library')
    sleep(5)
    page = open('library')
    content = page.read()
    r = re.compile(r'Page <span class=\"pagenumber\">1<\/span> of [0-9]{2}')
    pagenums = r.findall(content)
    pagenumstr = pagenums[0]
    pagenum = pagenumstr[len(pagenumstr)-2:len(pagenumstr)]
    system('rm -f library')
    
    artist_list = []
    for i in xrange(1,int(pagenum)):
        l = Lastfm(i)
        sleep(10)
        artist_list = l.dump_artists(artist_list)
        system('rm -f library?page='+str(i))
    
    f = open('../httpdocs/artists', 'w')
    for i in artist_list:
        f.write(i+'\n')
    f.close()

