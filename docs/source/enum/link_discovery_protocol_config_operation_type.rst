
==================================================================================================
LinkDiscoveryProtocolConfigOperationType
==================================================================================================

.. describe:: LinkDiscoveryProtocolConfigOperationType

    The Discovery Protocol operation.
    
    
    .. py:data:: LinkDiscoveryProtocolConfigOperationType.advertise
    
        Sent discovery packets for the switch, but don't listen for incoming discovery packets.
        
    
    .. py:data:: LinkDiscoveryProtocolConfigOperationType.both
    
        Sent discovery packets for the switch and listen for incoming discovery packets.
        
    
    .. py:data:: LinkDiscoveryProtocolConfigOperationType.listen
    
        Listen for incoming discovery packets but don't sent discovery packet for the switch.
        
    
    .. py:data:: LinkDiscoveryProtocolConfigOperationType.none
    
        Don't listen for incoming discovery packets and don't sent discover packets for the switch either.
        
    