#!/usr/bin/python

cfile = open("Dropbox/blist.xml")

account_types = {
    "msn": {
        "address": "tmcrodrigues@gmail.com",
        "type": "prpl-msn-pecan"
    },
    "sapo": {
        "address": "tmcrodrigues@sapo.pt/Home",
        "type": "prpl-jabber"
    },
    "gmail": {
        "address": "tmcrodrigues@gmail.com/Home",
        "type": "prpl-jabber"
    },
    "facebook": {
        "address": "tmcrodrigues@gmail.com",
        "type": "prpl-bigbrownchunx-facebookim"
    }
}

def get_account(line, type):
    if line.find("<buddy account='"+account_types[type]["address"]+"'") >= 0 and line.find("proto='"+account_types[type]["type"]+"'>") >= 0:
        return True
    else:
        return False


def is_contact(line):
    if line.find("<buddy") >= 0:
        raise Exception("fail at \n"+line)
    name_start = line.find("<name>")
    name_end = line.find("</name>")
    if name_start >= 0 and name_end >=0:
        return True
    else:
        return False

def get_contact(line):
    name_start = line.find("<name>")
    name_end = line.find("</name>")
    if name_start >= 0 and name_end >=0:
        return line[name_start+6:name_end]

def get_contact_list(type):
    mode = 'account'

    for line in cfile:
        if mode == 'account':
            if get_account(line, type):
                mode = 'contact'
                continue
        if mode == 'contact':
            if is_contact(line):
                print get_contact(line)
                mode = 'account'

get_contact_list('msn')
