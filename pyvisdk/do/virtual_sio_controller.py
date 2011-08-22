
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSIOController(vim, *args, **kwargs):
    '''This data object type defines a Super IO Controller for floppy drives, parallel
    ports, and serial ports.'''
    
    obj = vim.client.factory.create('ns0:VirtualSIOController')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'key', 'busNumber' ]
    inherited = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'unitNumber', 'device' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    