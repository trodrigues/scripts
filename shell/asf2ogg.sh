#!/bin/sh
mplayer -vo null -vc dummy -ao pcm:waveheader "$1" 
oggenc -q -1 -o "$(basename "$1" .asf).ogg" audiodump.wav
rm -f audiodump.wav
