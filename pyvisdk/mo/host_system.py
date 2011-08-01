
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSystem(ManagedEntity):
    '''The HostSystem managed object type provides access to a virtualization host
        platform.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostSystem):
        # MUST define these
        super(HostSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def ShutdownHost_Task(self, force):
        '''Shuts down a host. If the command is successful, then the host has been shut down.
        Thus, the client never receives an indicator of success in the returned
        task if connected directly to the host.This command is not supported on
        all hosts. Check the host capability shutdownSupported.

        :param force: Flag to specify whether or not the host should be shut down regardless of whether it is in maintenance mode. If true, the host is shut down, even if there are virtual machines running or other operations in progress.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ShutdownHost_Task")(force)
        

    def UpdateSystemResources(self, resourceInfo):
        '''Update the configuration of the system resource hierarchy.

        :param resourceInfo: 

        '''
        
        return self.delegate("UpdateSystemResources")(resourceInfo)
        

    def ExitLockdownMode(self):
        '''Restores Administrator permission for the local administrative account for the
        host that was removed by prior call to EnterLockdownMode. If the operation
        is successful, adminDisabled will be set to false. This API is not
        supported on the host. If invoked directly on a host, a NotSupported fault
        will be thrown. See AuthorizationManager
        '''
        
        return self.delegate("ExitLockdownMode")()
        

    def AcquireCimServicesTicket(self):
        '''Creates and returns a one-time credential used to establish a remote connection to
        a CIM interface. The port to connect to is the standard well known port
        for the service.

        :rtype: HostServiceTicket 

        '''
        
        return self.delegate("AcquireCimServicesTicket")()
        

    def RetrieveHardwareUptime(self):
        '''Return the hardware uptime of the host in seconds. The harware uptime of a host is
        not affected by NTP and changes to its wall clock time and can be used by
        clients to provide a common time reference for all hosts.

        :rtype: xsd:long 

        '''
        
        return self.delegate("RetrieveHardwareUptime")()
        

    def EnterMaintenanceMode_Task(self, timeout):
        '''Puts the host in maintenance mode. While this task is running and when the host is
        in maintenance mode, no virtual machines can be powered on and no
        provisioning operations can be performed on the host. Once the call
        completes, it is safe to turn off a host without disrupting any virtual
        machines.The task completes once there are no powered-on virtual machines
        on the host and no provisioning operations in progress on the host. The
        operation does not directly initiate any operations to evacuate or power-
        down powered-on virtual machines. However, if the host is part of a
        cluster with VMware DRS enabled, DRS provides migration recommendations to
        evacuate the powered-on virtual machines. If DRS is in fully-automatic
        mode, these are automatically scheduled.If the host is part of a cluster
        and the task is issued through VirtualCenter with evacuatePoweredOffVms
        set to true, the task will not succeed unless all the powered-off virtual
        machines are reregistered to other hosts. If VMware DRS is enabled, VC
        will automatically evacuate powered-off virtual machines. The task is
        cancellable.

        :param timeout: The task completes when the host successfully enters maintenance mode or the timeout expires, and in the latter case the task contains a Timeout fault. If the timeout is less than or equal to zero, there is no timeout. The timeout is specified in seconds.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("EnterMaintenanceMode_Task")(timeout)
        

    def PowerDownHostToStandBy_Task(self, timeoutSec):
        '''Puts the host in standby mode, a mode in which the host is in a standby state from
        which it can be powered up remotely. While this task is running, no
        virtual machines can be powered on and no provisioning operations can be
        performed on the host.The task completes only if there are no powered-on
        virtual machines on the host, no provisioning operations in progress on
        the host, and the host stopped responding. The operation does not directly
        initiate any operations to evacuate or power-down powered-on virtual
        machines. However, if a dynamic recommendation generation module is
        running, if possible, it will provide, and depending on the automation
        level, it will execute migrations of powered-on virtual machine.
        Furthermore, VMware power management module may evacute and put a host in
        standby mode to save power. If the host is part of a cluster and the task
        is issued through VirtualCenter with evacuatePoweredOffVms set to true,
        the task will not succeed unless all the powered-off virtual machines are
        reregistered to other hosts. If VMware DRS is enabled, VC will
        automatically evacuate powered-off virtual machines.The task is
        cancellable.This command is not supported on all hosts. Check the host
        capability standbySupported.

        :param timeoutSec: The task completes when the host successfully enters standby mode and stops sending heartbeat signals. If heartbeats are still coming after timeoutSecs seconds, the host is declared timedout, and the task is assumed failed.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("PowerDownHostToStandBy_Task")(timeoutSec)
        

    def UpdateFlags(self, flagInfo):
        '''Update flags that are part of the HostFlagInfo object.

        :param flagInfo: 

        '''
        
        return self.delegate("UpdateFlags")(flagInfo)
        

    def QueryMemoryOverheadEx(self, vmConfigInfo):
        '''Determines the amount of memory overhead necessary to power on a virtual machine
        with the specified characteristics.

        :param vmConfigInfo: The configuration of the virtual machine.


        :rtype: xsd:long 

        '''
        
        return self.delegate("QueryMemoryOverheadEx")(vmConfigInfo)
        

    def RebootHost_Task(self, force):
        '''Reboots a host. If the command is successful, then the host has been rebooted. If
        connected directly to the host, the client never receives an indicator of
        success in the returned task but simply loses connection to the host, upon
        success.This command is not supported on all hosts. Check the host
        capability vim.host.Capability.rebootSupported.

        :param force: Flag to specify whether or not the host should be rebooted regardless of whether it is in maintenance mode. If true, the host is rebooted, even if there are virtual machines running or other operations in progress.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RebootHost_Task")(force)
        

    def PowerUpHostFromStandBy_Task(self, timeoutSec):
        '''Takes the host out of standby mode. If the command is successful, the host wakes
        up and starts sending heartbeats. This method may be called automatically
        by a dynamic recommendation generation module to add capacity to a
        cluster, if the host is not in maintenance mode.Note that, depending on
        the implementation of the wakeup method, the client may never receive an
        indicator of success in the returned task. In some cases, it is not even
        possible to ensure that the wakeup request has made it to the host.The
        task is cancellable.

        :param timeoutSec: The task completes when the host successfully exits standby state and sends a heartbeat signal. If nothing is received from the host for timeoutSec seconds, the host is declared timedout, and the task is assumed failed.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("PowerUpHostFromStandBy_Task")(timeoutSec)
        

    def ReconnectHost_Task(self):
        '''Reconnects to a host. This process reinstalls agents and reconfigures the host, if
        it has gotten out of date with VirtualCenter. The reconnection process
        goes through many of the same steps as addHost: ensuring the correct set
        of licenses for the number of CPUs on the host, ensuring the correct set
        of agents is installed, and ensuring that networks and datastores are
        discovered and registered with VirtualCenter.The client can change the IP
        address and port of the host when doing a reconnect operation. This can be
        useful if the client wants to preserve existing metadata, even though the
        host is changing its IP address. For example, clients could preserve
        existing statistics, alarms, and privileges.This method can also be used
        to change the SSL thumbprint of a connected host without disconnecting
        it.This method is only supported through VirtualCenter.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ReconnectHost_Task")()
        

    def DisconnectHost_Task(self):
        '''Disconnects from a host and instructs the server to stop sending heartbeats.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("DisconnectHost_Task")()
        

    def ReconfigureHostForDAS_Task(self):
        '''Reconfigures the host for VMware HA.If the host is part of a HA cluster, this
        operation reconfigures the host for HA. For example, this operation may be
        used if a host is added to a HA enabled cluster and the automatic HA
        configuration system task fails. Automatic HA configuration may fail for a
        variety of reasons. For example, the host is configured incorrectly.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ReconfigureHostForDAS_Task")()
        

    def QueryHostConnectionInfo(self):
        '''Connection-oriented information about a host.

        :rtype: HostConnectInfo 

        '''
        
        return self.delegate("QueryHostConnectionInfo")()
        

    def ExitMaintenanceMode_Task(self, timeout):
        '''Takes the host out of maintenance mode. This blocks if any concurrent running
        maintenance-only host configurations operations are being performed. For
        example, if VMFS volumes are being upgraded.The task is cancellable.

        :param timeout: Number of seconds to wait for the exit maintenance mode to succeed. If the timeout is less than or equal to zero, there is no timeout.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ExitMaintenanceMode_Task")(timeout)
        

    def QueryMemoryOverhead(self, memorySize, numVcpus):
        '''Deprecated. As of VI API 2.5, use QueryMemoryOverheadEx. Determines the amount of
        memory overhead necessary to power on a virtual machine with the specified
        characteristics.

        :param memorySize: The amount of virtual system RAM, in bytes. For an existing virtual machine, this value can be found (in megabytes) as the memoryMB property of the VirtualHardware.

        :param numVcpus: The number of virtual CPUs. For an existing virtual machine, this value can be found as the numCPU property of the VirtualHardware.


        :rtype: xsd:long 

        '''
        
        return self.delegate("QueryMemoryOverhead")(memorySize,numVcpus)
        

    def EnterLockdownMode(self):
        '''Modifies the permissions on the host, so that it will only be accessible through
        local console or an authorized centralized management application. Any
        user defined permissions found on the host are lost.Access via a VI client
        connected to the host is blocked. Access though other services running on
        the host is also blocked.If the operation is successful, adminDisabled
        will be set to true. This API is not supported on the host, If invoked
        directly on a host, a NotSupported fault will be thrown. See
        AuthorizationManager
        '''
        
        return self.delegate("EnterLockdownMode")()
        

    def UpdateIpmi(self, ipmiInfo):
        '''Update fields that are part of the HostIpmiInfo object.

        :param ipmiInfo: 

        '''
        
        return self.delegate("UpdateIpmi")(ipmiInfo)
        