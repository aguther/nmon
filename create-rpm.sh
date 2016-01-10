#!/usr/bin/env bash

# defines
NAME=nmon

# get current version
FILENAME=$(basename $(ls lmon*.c))
VERSION=${FILENAME/lmon/}
VERSION=${VERSION/.c/}

# pack sources
tar -cvzf ${NAME}-${VERSION}.tar.gz --exclude .git --exclude *.tar.gz --transform s/./${NAME}-${VERSION}/ ./*

# run rpm build command
rpmbuild -ta ${NAME}-${VERSION}.tar.gz
