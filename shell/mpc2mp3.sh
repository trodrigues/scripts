#!/bin/sh

for i in *.mpc ; do
  mppdec "$i" "$(basename "$i" .mpc).wav"
  lame -V0 --vbr-new "$(basename "$i" .mpc).wav" -o "$(basename "$i" .mpc).mp3"
  rm -f "$(basename "$i" .mpc).wav"
 done 
