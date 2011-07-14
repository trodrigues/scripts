#!/bin/bash
# 
# This script facilitates usage of JsTestDriver
#
# For even easier results, add this to your shell profile file:
#   alias jstd="$HOME/path/to/js_test_driver.sh"
# and then just run `jstd start` on the directory where the .jar file is
# present

JSTESTDRIVER_VERSION="1.3.0"

JSTD_EXEC="JsTestDriver-$JSTESTDRIVER_VERSION.jar"

killTestDriver() {
    pids=`ps aux|grep JsTestDriver|grep -v grep|awk '{ print $2 }'`

    for i in $pids ; do
        kill -9 $i
    done

    screen -wipe
}

config=""
if [ "$2" != "" ] ; then
    config="--config $2 "
fi

case "$1" in
    "start")
        killTestDriver

        if [ -f  $JSTD_EXEC ] ; then
            screen -dm -S jstestdriver java -jar $JSTD_EXEC $config--port 9876
        else
            echo "JsTestDriver jar cannot be found"
        fi
        sleep 2
        screen -ls
    ;;

    "stop")
        killTestDriver
    ;;

    "run")
        java -jar $JSTD_EXEC $config--tests all
    ;;

    *)
        echo "Usage: $0 {start|stop|run}"
    ;;
esac
