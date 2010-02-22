#!/bin/sh
for i in *.wma; do mplayer -vo null -vc dummy -ao pcm:waveheader "$i" 
	lame -V0 --vbr-new audiodump.wav -o "$(basename "$i" .wma).mp3"
done
rm -f audiodump.wav
