#!/bin/sh
# use with sh jscompactor.sh file.js

# backup our file
cp $1 `basename $1 .js`-orig.js

# remove double space tabs
sed -i "s/\ \ //g" $1

# remove /* */ comments
sed -i 's/\/\*.*\*\///g' $1

# remove line breaks
awk '{printf("%s", $0 "")}' $1 > ctmp.js
cat ctmp.js > $1
rm -f ctmp.js
reset
