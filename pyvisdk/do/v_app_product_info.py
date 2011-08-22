
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VAppProductInfo(vim, *args, **kwargs):
    '''Information that describes what product a vApp contains, e.g., what software
    that is installed in the contained virtual machines.'''
    
    obj = vim.client.factory.create('ns0:VAppProductInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'key' ]
    inherited = [ 'appUrl', 'classId', 'fullVersion', 'instanceId', 'name', 'productUrl',
        'vendor', 'vendorUrl', 'version' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    