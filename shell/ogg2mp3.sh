#!/bin/sh
for i in *.ogg; do
	ogg123 -d wav -f audiodump.wav "$i"
	lame -V0 --vbr-new audiodump.wav -o "$(basename "$i" .ogg).mp3"
done
rm -f audiodump.wav
