
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineRuntimeInfo(vim, *args, **kwargs):
    '''The RuntimeInfo data object type provides information about the execution state
    and history of a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineRuntimeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))
        
    signature = [ 'connectionState', 'faultToleranceState', 'numMksConnections', 'powerState',
        'recordReplayState', 'toolsInstallerMounted' ]
    inherited = [ 'bootTime', 'cleanPowerOff', 'device', 'host', 'maxCpuUsage', 'maxMemoryUsage',
        'memoryOverhead', 'minRequiredEVCModeKey', 'needSecondaryReason', 'question',
        'suspendInterval', 'suspendTime' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    