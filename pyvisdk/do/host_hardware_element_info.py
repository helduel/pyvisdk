
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostHardwareElementInfo(vim, *args, **kwargs):
    '''Data object describing the operational status of a physical element.'''
    
    obj = vim.client.factory.create('ns0:HostHardwareElementInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'name', 'status' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in list(kwargs.items()):
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    