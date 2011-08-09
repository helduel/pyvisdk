
from pyvisdk.do.virtual_device_file_backing_option import VirtualDeviceFileBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskFlatVer1BackingOption(VirtualDeviceFileBackingOption):
    '''This data object type contains the available options when backing a virtual disk
        using a host file with the flat file format from GSX Server 2.x. Flat
        disks are pre-allocated, whereas sparse disks are grown as needed.
    '''
    
    def __init__(self, diskMode, growable, split, writeThrough):
        # MUST define these
        super(VirtualDiskFlatVer1BackingOption, self).__init__()
    
        self.data['diskMode'] = diskMode
        self.data['growable'] = growable
        self.data['split'] = split
        self.data['writeThrough'] = writeThrough
    
    
    @property
    def diskMode(self):
        '''The disk mode. Valid disk modes are: * persistent * nonpersistent * undoable *
        independent_persistent * independent_nonpersistent * append
        '''
        return self.data['diskMode']

    @property
    def growable(self):
        '''Flag to indicate whether this backing can have its size changed.
        '''
        return self.data['growable']

    @property
    def split(self):
        '''Flag to indicate whether or not the host supports allowing the client to select
        whether or not a disk should be split.
        '''
        return self.data['split']

    @property
    def writeThrough(self):
        '''Flag to indicate whether or not the host supports allowing the client to select
        "writethrough" as a mode for virtual disks. Typically, this is available
        only for GSX Server Linux hosts.
        '''
        return self.data['writeThrough']

