
from pyvisdk.do.cluster_das_admission_control_policy import ClusterDasAdmissionControlPolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterFailoverLevelAdmissionControlPolicy(ClusterDasAdmissionControlPolicy):
    '''The ClusterFailoverLevelAdmissionControlPolicy defines the number of host failures
        that should be tolerated and still guarantee enough unfragmented resources
        to failover all powered on virtual machines on those failed hosts.When you
        use the failover level policy, VMware HA partitions resources into slots.
        A slot represents the minimum CPU and memory resources that are required
        to support any powered-on virtual machine in the cluster.With the failover
        level policy in place, HA uses the following slot calculations to control
        virtual machine migration within the cluster:If your cluster contains any
        virtual machines that have much larger reservations than the others, they
        will distort slot size calculation. To avoid this, you can specify an
        upper bound for slot sizes; use the configuration editor in the vSphere
        Client to set the das.slotCpuInMHz and das.slotMemInMB attributes. When
        you use these attributes, there is a risk that resource fragmentation will
        cause virtual machines with resource requirements larger than the slot
        size to be assigned multiple slots. In a cluster that is close to
        capacity, there might be enough slots in aggregate for HA to successfully
        failover a virtual machine. However, if those slots are located on
        multiple hosts, a virtual machine assigned multiple slots cannot use them
        because a virtual machine can run on only a single host at a time.The CPU
        slot resource is the host CPU resource amount divided by the CPU component
        of the slot size; the result is rounded down. HA makes the same
        calculation for host memory resource amount. HA compares the results; the
        lower of the two numbers is the host slot capacity.
    '''
    
    def __init__(self, failoverLevel):
        # MUST define these
        super(ClusterFailoverLevelAdmissionControlPolicy, self).__init__()
    
        self.data['failoverLevel'] = failoverLevel
    
    
    @property
    def failoverLevel(self):
        '''Number of host failures that should be tolerated, still guaranteeing sufficient
        resources to migrate virtual machines to available hosts.
        '''
        return self.data['failoverLevel']

