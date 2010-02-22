#!/bin/sh
# add a package key on ubuntu

gpg --no-default-keyring --keyring /tmp/awn.keyring --keyserver keyserver.ubuntu.com --recv $1 && gpg --no-default-keyring --keyring /tmp/awn.keyring --export --armor $1 | sudo apt-key add - && rm /tmp/awn.keyring
