
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVMotionSystem(ExtensibleManagedObject):
    '''The VMotionSystem managed object describes the VMotion configuration of the
    host.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostVMotionSystem):
        super(HostVMotionSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def ipConfig(self):
        '''IP configuration of the VMotion VirtualNic.'''
        return self.update('ipConfig')
    @property
    def netConfig(self):
        '''VMotion network configuration.'''
        return self.update('netConfig')
    
    
    
    def DeselectVnic(self):
        '''Indicate that no VirtualNic should be used for VMotion.
        :rtype: None
        :returns: 
        '''
        return self.delegate("DeselectVnic")()
    
    def SelectVnic(self):
        '''Select the VirtualNic to be used for VMotion.
        :rtype: None
        :returns: 
        '''
        return self.delegate("SelectVnic")()
    
    def UpdateIpConfig(self):
        '''Update the IP configuration of VMotion VirtualNic.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateIpConfig")()