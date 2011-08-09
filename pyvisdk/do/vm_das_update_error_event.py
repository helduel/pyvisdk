
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmDasUpdateErrorEvent(VmEvent):
    '''The event records that an error occured when updating the HA agents with the
        current state of the virtual machine. If this occurs during a powerOn
        operation, the virtual machine will not be failed over in the event of a
        host failure. If it occurs during a powerOff, the virtual machine will be
        automatically powered on if the host it was last running on crashes.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VmDasUpdateErrorEvent, self).__init__()
    

    
    
