#!/usr/bin/perl
# By Jason Collins-Webb (jason@rbaltd.co.uk)
# usage: vpnwho
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
#

$TDateM = substr(`/bin/date +"%b"`, 0, -1);
$TDateD = substr(`/bin/date +"%e"`, 0, -1);
$whoson = `/bin/ps -eo pid,bsdstart,cmd|/bin/grep "pptpd \\["`;
if ($whoson ne "") {
@logons = split(/\n/, $whoson);
foreach $l (@logons) {
  if ($l =~ /(\d+)\s+(\d+:\d+).*\[(\d+\.\d+\.\d+\.\d+)\]/) {
    $PID = $1+1;
    $IP = $3;
    $STIME = $2;
    open MESSAGES, "</var/log/messages";
    while(<MESSAGES>){
      if ($_ =~ /.*\spppd\[$PID\]:\s+MSCHAP-v2\s.*\s(.+\\)*(.+)$/i) {
          $User = lc($2);
          }
     }
     close MESSAGES;
  print "Current VPN connection from $User ($IP), started at $STIME\n";
  }
}
} else {
print "There are no current VPN connections.\n";
}
