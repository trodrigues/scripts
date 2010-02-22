#!/bin/sh
for i in *.flac; do
	flac -d "$i"
	lame -V0 --vbr-new "$(basename "$i" .flac).wav" -o "$(basename "$i" .flac).mp3"
done
rm -f *.wav
