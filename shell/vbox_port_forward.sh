#!/bin/sh

if [ $# -ge 4 ] ; then
    vmname=$1
    service=$2
    hostport=$3
    guestport=$4
    if [ $# -eq 5 ] ; then
        protocol=$5
    else
        protocol=""
    fi
else
    echo "your vm name ?"; read vmname
    echo "Service name ? (ssh, www, etc)"; read service
    echo "host port ?"; read hostport
    echo "guest port ?"; read guestport
    echo "Protocol ? (default: TCP)"; read protocol
fi

if [ "$protocol" = "" ] ; then
    protocol="TCP"
fi

VBoxManage setextradata "$vmname" \
    "VBoxInternal/Devices/e1000/0/LUN#0/Config/$service/Protocol" $protocol
VBoxManage setextradata "$vmname" \
    "VBoxInternal/Devices/e1000/0/LUN#0/Config/$service/HostPort" $hostport
VBoxManage setextradata "$vmname" \
    "VBoxInternal/Devices/e1000/0/LUN#0/Config/$service/GuestPort" $guestport

VBoxManage getextradata "$vmname" enumerate
