#!/bin/sh

for i in *.m4a ; do
	faad "$i"
	lame -V0 --vbr-new "$(basename "$i" .m4a).wav" -o "$(basename "$i" .m4a).mp3"
	rm -f "$(basename "$i" .m4a).wav"
done 
