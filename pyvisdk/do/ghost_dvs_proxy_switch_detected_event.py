
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def GhostDvsProxySwitchDetectedEvent(vim, *args, **kwargs):
    '''This event records when Virtual Center server found DVS proxy switches on the
    host that don't match any DVS defined in Virtual Center.'''
    
    obj = vim.client.factory.create('ns0:GhostDvsProxySwitchDetectedEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))
        
    signature = [ 'chainId', 'createdTime', 'key', 'userName', 'switchUuid' ]
    inherited = [ 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    