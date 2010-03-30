#!/bin/sh

echo "your vm name ?"; read vmname

echo "Service name ? (ssh, www, etc)"; read service

echo "host port ?"; read hostport

echo "guest port ?"; read guestport

echo "Protocol ? (default: TCP)"; read protocol

if [ $protocol == "" ] ; then
    protocol="TCP"
fi

VBoxManage setextradata "$vmname" \
    "VBoxInternal/Devices/e1000/0/LUN#0/Config/$service/Protocol" TCP
VBoxManage setextradata "$vmname" \
    "VBoxInternal/Devices/e1000/0/LUN#0/Config/$service/HostPort" $hostport
VBoxManage setextradata "$vmname" \
    "VBoxInternal/Devices/e1000/0/LUN#0/Config/$service/GuestPort" $guestport

VBoxManage getextradata "$vmname" enumerate
