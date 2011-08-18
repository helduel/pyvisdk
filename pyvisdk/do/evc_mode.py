
from pyvisdk.do.element_description import ElementDescription
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EVCMode(ElementDescription):
    '''The EVCMode data object describes an Enhanced vMotion Compatibility mode. An EVC
        mode is associated with a set of CPU features. A vCenter Server defines
        the available EVC modes. You use them to establish a common set of
        features for compatibility between hosts in a cluster. An EVC-enabled
        cluster supports safe vMotion of virtual machines across a range of CPU
        generations. You must use the vSphere Client to configure EVC.When you add
        a host to an EVC-enabled cluster, the vCenter Server determines the CPU
        compatibility to preserve vMotion compatibility within the cluster. If the
        host CPU is compatible with those already in the cluster, the Server adds
        the host to the cluster and configures it for compatible operation. Hosts
        that are not compatible are not allowed to join the cluster.The inherited
        key property is a string value that uniquely identifies an EVC mode. The
        vCenter Server assigns the key value; the vSphere API uses the key to
        identify modes in summary and information objects:*
        ClusterComputeResourceSummary.currentEVCModeKey *
        HostListSummary.currentEVCModeKey * HostListSummary.maxEVCModeKey *
        VirtualMachineRuntimeInfo.minRequiredEVCModeKeyThe inherited label and
        summary properties are human-readable strings.You can use the track and
        vendorTier properties to determine feature-superset relationships between
        modes without examining the individual feature bits in
        guaranteedCPUFeatures. The CPU feature baseline of mode A is a superset of
        mode B's baseline if and only if:* modeA.track is the same as or a
        superset of modeB.track * modeA.vendorTier is equal to or greater than
        modeB.vendorTierUse the track and vendorTier properties only for the
        purpose of feature-superset calculations as described above. Do not use
        them to infer the presence or absence of specific features. The property
        values for a given mode may change across releases as the set of available
        EVC modes changes, to better represent mode relationships.
    '''
    
    def __init__(self, guaranteedCPUFeatures, track, vendor, vendorTier):
        # MUST define these
        super(EVCMode, self).__init__()
    
        self.data['guaranteedCPUFeatures'] = guaranteedCPUFeatures
        self.data['track'] = track
        self.data['vendor'] = vendor
        self.data['vendorTier'] = vendorTier
    
    
    @property
    def guaranteedCPUFeatures(self):
        '''Describes the CPU feature baseline associated with the EVC mode. On the cluster
        where a particular EVC mode is configured, those CPU features are
        guaranteed, either because the host hardware naturally matches those
        features or because CPU feature override is used to mask out differences
        and enforce a match.
        '''
        return self.data['guaranteedCPUFeatures']

    @property
    def track(self):
        '''Identifiers for feature groups that are at least partially present in the
        guaranteedCPUFeatures array for this mode. Use this property to compare
        track values from two modes. Do not use this property to determine the
        presence or absence of specific features.
        '''
        return self.data['track']

    @property
    def vendor(self):
        '''CPU hardware vendor required for this mode.
        '''
        return self.data['vendor']

    @property
    def vendorTier(self):
        '''Index for ordering the set of modes that apply to a given CPU vendor. Use this
        property to compare vendor tier values from two modes. Do not use this
        property to determine the presence or absence of specific features.
        '''
        return self.data['vendorTier']
