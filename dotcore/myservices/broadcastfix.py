#
# CORE
# Copyright (c)2010-2012 the Boeing Company.
# See the LICENSE file included in this distribution.
#
''' serval service.
'''

import os

from core.service import CoreService, addservice
from core.misc.ipaddr import IPv4Prefix, IPv6Prefix

class BroadcastFixService(CoreService):
    ''' This is a sample user-defined service.
    '''
    # a unique name is required, without spaces
    _name = "BroadcastFixService"
    # you can create your own group here
    _group = "Mesh"
    # list of other services this service depends on
    _depends = ()
    # per-node directories
    _dirs = ()
    # generated files (without a full path this file goes in the node's dir,
    #  e.g. /tmp/pycore.12345/n1.conf/)
    _configs = ("bcastset.sh", "setall.sh", )
    # this controls the starting order vs other enabled services
    _startindex = 10
    # list of startup commands, also may be generated during startup
    #_startup = ('/home/meshadmin/serval-dna/servald start',)
    #_startup = ('bash -c "for i in $(ls -1 /sys/class/net \| grep eth); do bcastset.sh $i ; done"',)
    _startup = ('bash setall.sh',)
    # list of shutdown commands
    _shutdown = ()

    @classmethod
    def generateconfig(cls, node, filename, services):
        ''' Return a string that will be written to filename, or sent to the
            GUI for user customization.
        '''
        if filename == "bcastset.sh":
            cfg = """#!/bin/bash
if [ -z $1 ]; then
 echo "Usage: $0 <interface>"
 echo "set the broadcast address according to netmask"
 exit 1
fi

ip2int()
{
    local a b c d
    { IFS=. read a b c d; } <<< $1
    echo $(((((((a << 8) | b) << 8) | c) << 8) | d))
}

int2ip()
{
    local ui32=$1; shift
    local ip n
    for n in 1 2 3 4; do
        ip=$((ui32 & 0xff))${ip:+.}$ip
        ui32=$((ui32 >> 8))
    done
    echo $ip
}

netmask()
{
    local mask=$((0xffffffff << (32 - $1))); shift
    int2ip $mask
}

broadcast()
{
    local addr=$(ip2int $1); shift
    local mask=$((0xffffffff << (32 - $1))); shift
    int2ip $((addr | ~mask))
}

network()
{
    local addr=$(ip2int $1); shift
    local mask=$((0xffffffff << (32 -$1))); shift
    int2ip $((addr & mask))
}

IPADDR=$(ip addr show dev $1 | grep "inet " | cut -d " " -f 6 | cut -d "/" -f 1)
SUBNET=$(ip addr show dev $1 | grep "inet " | cut -d " " -f 6 | cut -d "/" -f 2)

BCAST=$(broadcast $IPADDR $SUBNET)


if [ -z $2 ]; then
 ifconfig $1 broadcast $BCAST
else
 echo $BCAST
fi"""
        elif filename == "setall.sh":
            cfg = """#!/bin/bash
for i in $(ls -1 /sys/class/net | grep eth); do bash bcastset.sh $i ; done"""

        else:
            cfg = ""
#        for ifc in node.netifs():
#            cfg += 'echo "Node %s has interface %s"\n' % (node.name, ifc.name)
#            # here we do something interesting
#            cfg += "\n".join(map(cls.subnetentry, ifc.addrlist))
#            break
        return cfg

    @staticmethod
    def subnetentry(x):
        ''' Generate a subnet declaration block given an IPv4 prefix string
            for inclusion in the config file.
        '''
        if x.find(":") >= 0:
            # this is an IPv6 address
            return ""
        else:
            net = IPv4Prefix(x)
            return 'echo "  network %s"' % (net)

# this line is required to add the above class to the list of available services
addservice(BroadcastFixService)
