#!/bin/bash
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
# Your copy is available at: http://www.gnu.org/licenses/gpl.html

TEMP=$(locate /etc/conf.modules); if [ -n "$TEMP" ]; then ln -s /etc/conf.modules /etc/modules.conf; fi
TEMP=$(cat /etc/modules.conf | grep "alias ppp ppp_generic")
if [ -n "$TEMP" ]; then
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
