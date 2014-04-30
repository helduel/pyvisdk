
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def StorageDrsIoLoadBalanceConfig(vim, *args, **kwargs):
    '''Storage DRS configuration for I/O load balancing.NOTE: This data object type
    and all of its methods are experimental and subject to change in future
    releases.'''
    
    obj = vim.client.factory.create('ns0:StorageDrsIoLoadBalanceConfig')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'ioLatencyThreshold', 'ioLoadImbalanceThreshold', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in list(kwargs.items()):
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    