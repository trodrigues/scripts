#!/bin/sh
LDFLAGS=-L/usr/local/Cellar/openssl/0.9.8r/lib
CPPFLAGS=-I/usr/local/Cellar/openssl/0.9.8r/include
./configure --prefix=~/Code/javascript/node
make
make install
