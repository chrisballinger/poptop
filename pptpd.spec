%define name pptpd
%define ver 1.1.3
%define rel 2
%define prefix /usr
%define buildlibwrap 1
%define buildbsdppp 0
%define buildslirp 0
%define buildipalloc 0
%define buildpnsmode 0

Summary: A PPTP server daemon started from init (/etc/rc.d/init.d/).
Name: %{name}
Version: %{ver}
Release: %{rel}
Copyright: GPL
Group: Networking/Daemons
Packager: R. de Vroede <r.devroede@linvision.com>
Source0: %{name}-%{ver}.tar.gz
URL: http://www.poptop.org
Buildroot: %{_tmppath}/%{name}-root

%description
PPTPd, Point-to-Point Tunnelling Protocol Daemon, offers out
connections to pptp clients to become virtual members of the IP pool
owned by the pptp server.  In effect, these clients become virtual
members of the local subnet, regardless of what their real IP address
is.  A tunnel is built between the pptp server and client, and packets
from the subnet are wrapped and passed between server and client
similar to other C/S protocols.

# allow --with[out] <feature> at rpm command line build
# e.g. --with ipalloc --without libwrap
# --with overrides --without
%{?_without_libwrap: %{expand: %%define buildlibwrap 0}}
%{?_without_bsdppp: %{expand: %%define buildbsdppp 0}}
%{?_without_slirp: %{expand: %%define buildslirp 0}}
%{?_without_ipalloc: %{expand: %%define buildipalloc 0}}
%{?_without_pnsmode: %{expand: %%define buildpnsmode 0}}
%{?_with_libwrap: %{expand: %%define buildlibwrap 1}}
%{?_with_bsdppp: %{expand: %%define buildbsdppp 1}}
%{?_with_slirp: %{expand: %%define buildslirp 1}}
%{?_with_ipalloc: %{expand: %%define buildipalloc 1}}
%{?_with_pnsmode: %{expand: %%define buildpnsmode 1}}

%prep
topdir=`env | grep OLDPWD | cut -d "=" -f2`
RPM_BUILD_DIR=%{_tmppath}
RPM_SOURCE_DIR=%{_tmppath}
RPM_RPM_DIR=$topdir/../
RPM_SRPM_DIR=$topdir/../
mkdir -p $RPM_BUILD_DIR
rm -rf $RPM_BUILD_DIR/%{name}-%{ver}
mkdir -p $RPM_BUILD_DIR/%{name}-%{ver}
cp -a $topdir/* $RPM_BUILD_DIR/%{name}-%{ver}
cd $topdir
tar -czf $RPM_SOURCE_DIR/%{name}-%{ver}.tar.gz .

%setup -D -T -n $RPM_BUILD_DIR/%{name}-%{ver}

%build
buildopts=""
%if %{buildlibwrap}
buildopts="$buildopts --with-libwrap"
%endif
%if %{buildbsdppp}
buildopts="$buildopts --with-bsdppp"
%endif
%if %{buildslirp}
buildopts="$buildopts --with-slirp"
%endif
%if %{buildipalloc}
buildopts="$buildopts --with-pppd-ip-alloc"
%endif
%if %{buildpnsmode}
buildopts="$buildopts --with-pns-mode"
%endif
./configure --prefix=%{prefix} $buildopts
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/ppp
mkdir -p $RPM_BUILD_ROOT/usr/bin/
make prefix=$RPM_BUILD_ROOT%{prefix} install
install -m 0755 pptpd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/pptpd
install -m 0644 samples/pptpd.conf $RPM_BUILD_ROOT/etc/pptpd.conf
install -m 0644 samples/options.pptpd $RPM_BUILD_ROOT/etc/ppp/options.pptpd
install -m 0755 tools/vpnuser $RPM_BUILD_ROOT/usr/bin/vpnuser
install -m 0755 tools/vpnstats $RPM_BUILD_ROOT/usr/bin/vpnstats
install -m 0755 tools/vpnstats.pl $RPM_BUILD_ROOT/usr/bin/vpnstats.pl
mkdir -p $RPM_BUILD_ROOT/usr/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
install -m 0644 pptpd.conf.5 $RPM_BUILD_ROOT/usr/man/man5/pptpd.conf.5
install -m 0644 pptpd.8 $RPM_BUILD_ROOT/usr/man/man8/pptpd.8
install -m 0644 pptpctrl.8 $RPM_BUILD_ROOT/usr/man/man8/pptpctrl.8
strip $RPM_BUILD_ROOT/%{prefix}/sbin/* || :
make maintainer-clean

%post
TEMP=$(locate /etc/modules.conf)
if [ -z "$TEMP" ]; then ln -s /etc/conf.modules /etc/modules.conf; fi
TEMP=$(cat /etc/modules.conf | grep "alias ppp ppp_generic")
if [ -z "$TEMP" ]; then
        grep -v "alias ppp ppp_generic" /etc/modules.conf > /etc/modules.conf1;
        mv -f /etc/modules.conf1 /etc/modules.conf
fi
TEMP=$(cat /etc/modules.conf | grep "alias char-major-108 off")
if [ -n "$TEMP" ]; then
        grep -v "alias char-major-108 off" /etc/modules.conf > /etc/modules.conf1;
        mv -f /etc/modules.conf1 /etc/modules.conf
fi
TEMP=$(cat /etc/modules.conf | grep "alias char-major-108 ppp_generic")
if [ -z "$TEMP" ]; then echo "alias char-major-108 ppp_generic" >> /etc/modules.conf; fi
TEMP=$(cat /etc/modules.conf | grep "alias ppp-compress-18 ppp_mppe")
if [ -z "$TEMP" ]; then echo "alias ppp-compress-18 ppp_mppe" >> /etc/modules.conf; fi
TEMP=$(cat /etc/modules.conf | grep "alias ppp-compress-21 bsd_comp")
if [ -z "$TEMP" ]; then echo "alias ppp-compress-21 bsd_comp" >> /etc/modules.conf; fi
TEMP=$(cat /etc/modules.conf | grep "alias ppp-compress-24 ppp_deflate")
if [ -z "$TEMP" ]; then echo "alias ppp-compress-24 ppp_deflate" >> /etc/modules.conf; fi
TEMP=$(cat /etc/modules.conf | grep "alias ppp-compress-26 ppp_deflate")
if [ -z "$TEMP" ]; then echo "alias ppp-compress-26 ppp_deflate" >> /etc/modules.conf; fi
TEMP=$(cat /etc/modules.conf | grep "alias tty-ldisc-3 ppp_async")
if [ "$TEMP" = "" ]; then echo "alias tty-ldisc-3 ppp_async" >> /etc/modules.conf; fi
TEMP=$(cat /etc/modules.conf | grep "alias tty-ldisc-14 ppp_synctty")
if [ -z "$TEMP" ]; then echo "alias tty-ldisc-14 ppp_synctty" >> /etc/modules.conf; fi
depmod -a
OUTD="" ; for i in d manager ctrl ; do
    test -x /sbin/pptp$i && OUTD="$OUTD /sbin/pptp$i" ;
done
test -z "$OUTD" || \
{ echo "possible outdated executable detected; you should do run the following command:"; echo "rm -i $OUTD" ;}
/sbin/chkconfig --add pptpd
/sbin/chkconfig --level 345 pptpd on
rm -f $RPM_SOURCE_DIR/%{name}-%{ver}.tar.gz
%preun
/sbin/chkconfig --del pptpd

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README* TODO html samples
/usr/sbin/pptpd
/usr/sbin/pptpctrl
/usr/bin/vpnuser
/usr/bin/vpnstats
/usr/bin/vpnstats.pl
/usr/man/man5/pptpd.conf.5*
/usr/man/man8/pptpd.8*
/usr/man/man8/pptpctrl.8*
/etc/rc.d/init.d/pptpd
%config(noreplace) /etc/pptpd.conf
%config(noreplace) /etc/ppp/options.pptpd

%changelog
* Thu Aug 22 2002 Richard de Vroede <richard@linvision.com>
- added stimeout option to pptpd.conf manpage
- updated the Changelog file ;-)

* Tue Aug 20 2002 Richard de Vroede <richard@linvision.com>
- removed debug commandline option from pptpd.init

* Thu Aug  1 2002 Richard de Vroede <richard@linvision.com>
- added config(noreplace) so old configs don't get replaced
- fixed postscriptlet
- adapted spec to cvs tree

* Wed Jun 26 2002 Richard de Vroede <richard@linvision.com>
- specfile now supports --with[out] options
- updated to 1.1.3

* Tue Feb 19 2002 Richard de Vroede <richard@linvision.com>
- added check for ip_gre alias in /etc/modules.conf
- tweaked the config some

* Fri Feb 8 2002 Richard de Vroede <richard@linvision.com>
- added check for important aliases in /etc/modules.conf
- added support for older /etc/conf.modules (by ln-ing it)
- added vpnuser script to simplify managing vpnusers
- added vpnstats script to send nice comma-separated stats to admin

* Mon Jan 14 2002 Richard de Vroede <richard@linvision.com>
- changed the BuildRoot
- added * after the manfiles in the "%files" section to fix build
- updated to 1.1.2

* Mon Oct 9 2000 Andy Worthington <christopherandrew@ou.edu>
- changed url and source to new website
- added man pages to files
- removed startup via inittab
- added startup via init (/etc/rc.d/init.d)
- updated to 1.0.1

* Tue Nov 23 1999 Tim Powers <timp@redhat.com>
- added "%config /etc/pptpd.conf" back to spec
- updated to 1.0.0

* Mon Aug 30 1999 Tim Powers <timp@redhat.com>
- changed group

* Wed Aug 4 1999 Tim Powers <timp@redhat.com>
- started changelog
- quiet setup
- changed prefix to be /usr instead of /usr/local
- added buildroot
- fixed %install section so that it uses buildroot
- updated source to 0.9.10
- built to be included into Powertools
- spec based heavily on spec by "Allan's Package-O-Matic Blenderfier"
