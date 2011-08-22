
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineUsbInfo(vim, *args, **kwargs):
    '''This data object contains information about a physical USB device on the host.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineUsbInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))
        
    signature = [ 'name', 'description', 'physicalPath', 'product', 'vendor' ]
    inherited = [ 'configurationTag', 'family', 'speed', 'summary' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    