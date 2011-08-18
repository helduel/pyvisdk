
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmConfigSpec(DynamicData):
    '''vApp related configuration of a VM.
    '''
    
    def __init__(self, eula, installBootRequired, installBootStopDelay, ipAssignment, ovfEnvironmentTransport, ovfSection, product, property):
        # MUST define these
        super(VmConfigSpec, self).__init__()
    
        self.data['eula'] = eula
        self.data['installBootRequired'] = installBootRequired
        self.data['installBootStopDelay'] = installBootStopDelay
        self.data['ipAssignment'] = ipAssignment
        self.data['ovfEnvironmentTransport'] = ovfEnvironmentTransport
        self.data['ovfSection'] = ovfSection
        self.data['product'] = product
        self.data['property'] = property
    
    
    @property
    def eula(self):
        '''End User Liceses Agreements.
        '''
        return self.data['eula']

    @property
    def installBootRequired(self):
        '''If this is on a VirtualMachine object, it specifies whether the VM needs an
        initial boot before the deployment is complete. If this is on a vApp
        object, it indicates than one or more VMs needs an initial reboot. This
        flag is automatically reset once the reboot has happened.
        '''
        return self.data['installBootRequired']

    @property
    def installBootStopDelay(self):
        '''Specifies the delay in seconds to wait for the VM to power off after the initial
        boot (used only if installBootRequired is true). A value of 0 means wait
        forever.
        '''
        return self.data['installBootStopDelay']

    @property
    def ipAssignment(self):
        '''IP assignment policy and DHCP support configuration.
        '''
        return self.data['ipAssignment']

    @property
    def ovfEnvironmentTransport(self):
        '''List the transports to use for properties. Supported values are: iso and
        com.vmware.guestInfo.
        '''
        return self.data['ovfEnvironmentTransport']

    @property
    def ovfSection(self):
        '''List of uninterpreted OVF meta-data sections.
        '''
        return self.data['ovfSection']

    @property
    def product(self):
        '''Information about the product.
        '''
        return self.data['product']

    @property
    def property_(self):
        '''List of properties.
        '''
        return self.data['property']
