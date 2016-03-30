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

class ServalNoStartService(CoreService):
    ''' This is a sample user-defined service.
    '''
    # a unique name is required, without spaces
    _name = "ServalNoStartService"
    # you can create your own group here
    _group = "Mesh"
    # list of other services this service depends on
    _depends = ("BroadcastFixService", )
    # per-node directories
    _dirs = ("/home/meshadmin/serval-conf/etc/serval","/home/meshadmin/serval-conf/var/log", "/home/meshadmin/serval-conf/var/log/serval", "/home/meshadmin/serval-conf/var/run/serval", "/home/meshadmin/serval-conf/var/cache/serval","/home/meshadmin/serval-conf/var/cache/serval/sqlite3tmp","/home/meshadmin/serval-conf/var/cache/serval/blob")
    # generated files (without a full path this file goes in the node's dir,
    #  e.g. /tmp/pycore.12345/n1.conf/)
    _configs = ('/home/meshadmin/serval-conf/etc/serval/serval.conf', "mesh-start.sh", )
    # this controls the starting order vs other enabled services
    _startindex = 50
    # list of startup commands, also may be generated during startup
    #_startup = ('/home/meshadmin/serval-dna/servald start',)
    _startup = ('',)
    # list of shutdown commands
    _shutdown = ('')

    @classmethod
    def generateconfig(cls, node, filename, services):
        ''' Return a string that will be written to filename, or sent to the
            GUI for user customization.
        '''
	if filename == "/home/meshadmin/serval-conf/etc/serval/serval.conf":
	        cfg = "debug.rhizome=true\n"
        	cfg += "debug.verbose=true\n"
		cfg += "interfaces.0.match=eth*\n"
		cfg += "interfaces.0.socket_type=dgram\n"
		cfg += "interfaces.0.type=ethernet\n"
	elif filename == "mesh-start.sh":
		cfg ="#!/bin/sh\n"
		cfg +="ulimit -c unlimited\n"
		cfg +="/home/meshadmin/serval-dna/servald start\n"		
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
addservice(ServalNoStartService)
