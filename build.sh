#!/bin/sh
echo "build.sh: superceded by makepackage"
exit 1

POPTOPVERSION=`./version`
CURRENTDIR=`pwd`
THISDIR=${CURRENTDIR##*/}
if [ -f /etc/redhat-release ]; then
   tar -czf /usr/src/redhat/SOURCES/pptpd-${POPTOPVERSION}.tar.gz .
   rpmbuild -ta /usr/src/redhat/SOURCES/pptpd-${POPTOPVERSION}.tar.gz
fi
