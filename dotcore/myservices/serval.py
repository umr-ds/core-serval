''' serval service.
'''

import os

from core.service import CoreService, addservice
from core.misc.ipaddr import IPv4Prefix, IPv6Prefix

class ServalService(CoreService):
    ''' servald as a service.
    '''
    # a unique name is required, without spaces
    _name = "ServalService"
    # you can create your own group here
    _group = "Mesh"
    # list of other services this service depends on
    _depends = ()
    # per-node directories
    _dirs = ("/home/meshadmin/serval-conf/etc/serval","/home/meshadmin/serval-conf/var/log", "/home/meshadmin/serval-conf/var/log/serval", "/home/meshadmin/serval-conf/var/run/serval", "/home/meshadmin/serval-conf/var/cache/serval","/home/meshadmin/serval-conf/var/cache/serval/sqlite3tmp","/home/meshadmin/serval-conf/var/cache/serval/blob")
    # generated files (without a full path this file goes in the node's dir,
    #  e.g. /tmp/pycore.12345/n1.conf/)
    _configs = ('/home/meshadmin/serval-conf/etc/serval/serval.conf', "mesh-start.sh", )
    # this controls the starting order vs other enabled services
    _startindex = 50
    # list of startup commands, also may be generated during startup
    #_startup = ('/home/meshadmin/serval-dna/servald start',)
    _startup = ('bash mesh-start.sh',)
    # list of shutdown commands
    _shutdown = ('servald stop', )

    @classmethod
    def generateconfig(cls, node, filename, services):
        ''' Return a string that will be written to filename, or sent to the
            GUI for user customization.
        '''
        if filename == "/home/meshadmin/serval-conf/etc/serval/serval.conf":
            cfg = '''
debug.rhizome=true
debug.verbose=true
interfaces.0.match=*
interfaces.0.socket_type=dgram
interfaces.0.type=ethernet'''
        elif filename == "mesh-start.sh":
            cfg = '''#!/bin/sh
servald start
sleep $[ ( $RANDOM % 10 )  + 1 ]s
for i in `ifconfig | grep \"inet addr:10.\" | cut -d\":\" -f 2 | cut -d\".\" -f1,2,3`; do
    servald scan $i.255
done'''
        else:
            cfg = ""
        return cfg

# this line is required to add the above class to the list of available services
addservice(ServalService)
