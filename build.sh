#!/bin/sh
POPTOPVERSION=`./version`
CURRENTDIR=`pwd`
THISDIR=${CURRENTDIR##*/}
if [ -f /etc/redhat-release ]; then
   tar -czf /usr/src/redhat/SOURCES/pptpd-${POPTOPVERSION}.tar.gz .
   rpmbuild -ta /usr/src/redhat/SOURCES/pptpd-${POPTOPVERSION}.tar.gz
fi
