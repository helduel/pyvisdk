
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VMwareDVSConfigInfo(vim, *args, **kwargs):
    '''This class defines the VMware specific configuration for
    DistributedVirtualSwitch.'''
    
    obj = vim.client.factory.create('ns0:VMwareDVSConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 13:
        raise IndexError('Expected at least 14 arguments got: %d' % len(args))
        
    signature = [ 'configVersion', 'contact', 'createTime', 'defaultPortConfig', 'maxPorts',
        'name', 'networkResourceManagementEnabled', 'numPorts', 'numStandalonePorts',
        'productInfo', 'uplinkPortPolicy', 'uuid', 'maxMtu' ]
    inherited = [ 'description', 'extensionKey', 'host', 'policy', 'targetInfo',
        'uplinkPortgroup', 'vendorSpecificConfig', 'linkDiscoveryProtocolConfig',
        'pvlanConfig' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    