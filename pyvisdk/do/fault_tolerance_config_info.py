
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FaultToleranceConfigInfo(vim, *args, **kwargs):
    '''FaultToleranceConfigInfo is a data object type containing Fault Tolerance
    settings for this virtual machine. role, instanceUuids and configPaths contain
    information about the whole fault tolerance group.'''
    
    obj = vim.client.factory.create('ns0:FaultToleranceConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'configPaths', 'instanceUuids', 'role' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    