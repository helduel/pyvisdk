
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterConfigInfoEx(vim, *args, **kwargs):
    '''The ClusterConfigInfoEx data object describes a complete cluster configuration.
    For information about configuring a cluster, see ClusterConfigSpecEx.'''
    
    obj = vim.client.factory.create('ns0:ClusterConfigInfoEx')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'vmSwapPlacement', 'dasConfig', 'drsConfig' ]
    inherited = [ 'dasVmConfig', 'dpmConfigInfo', 'dpmHostConfig', 'drsVmConfig', 'group', 'rule' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    