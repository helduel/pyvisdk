
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NetworkProfile(vim, *args, **kwargs):
    '''DataObject represents a profile for network configuration.'''
    
    obj = vim.client.factory.create('ns0:NetworkProfile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    required = [ 'enabled' ]
    optional = [ 'consoleIpRouteConfig', 'dnsConfig', 'dvsHostNic', 'dvsServiceConsoleNic',
        'dvswitch', 'hostPortGroup', 'ipRouteConfig', 'pnic',
        'serviceConsolePortGroup', 'vmPortGroup', 'vswitch', 'policy',
        'dynamicProperty', 'dynamicType' ]
    
    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    