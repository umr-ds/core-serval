''' serval service.
'''

import os

from core.service import CoreService, addservice
from core.misc.ipaddr import IPv4Prefix, IPv6Prefix

class ServalMonService(CoreService):
    ''' servald as a service.
    '''
    # a unique name is required, without spaces
    _name = "ServalMonService"
    # you can create your own group here
    _group = "Mesh"
    # list of other services this service depends on
    _depends = ()
    # per-node directories
    _dirs = ()
    # generated files (without a full path this file goes in the node's dir,
    #  e.g. /tmp/pycore.12345/n1.conf/)
    _configs = ()
    # this controls the starting order vs other enabled services
    _startindex = 50
    # list of startup commands, also may be generated during startup
    #_startup = ('/home/meshadmin/serval-dna/servald start',)
    _startup = ('nohup /home/meshadmin/serval-tests/monitor start',)
    # list of shutdown commands
    _shutdown = ('nohup /home/meshadmin/serval-tests/monitor stop', )

# this line is required to add the above class to the list of available services
addservice(ServalMonService)

