
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostServiceTicket(DynamicData):
    '''Return value for ticketable host services. The server has the option to provide a
        hostname and port for a future ticket-authenticated connection to a
        service on a host. If the service provider does not return a host the
        client must connect to the same host it used to request the ticket. In
        case the service provider does not return a port, except in the case of
        connecting to CIM interfaces, the client must connect using the same port
        it used to request the ticket. In the case of connecting to a CIM
        interface the standard well known port number for the particular service
        will be used for the connection.For example, when a client requests a
        ticket from an ESX Server, the returned ticket may omit the optional host
        and port. In such a case, the client establishes an out-of-band ticketed
        connection to the same server host and on the same port on which it made
        the connection to request the ticket. If this request is made to the
        VirtualCenter server, but the server does not provide the required service
        directly, then the server provides a hostname and port for a server that
        accepts the ticketed connection and provides the service.
    '''
    
    def __init__(self, host, port, service, serviceVersion, sessionId, sslThumbprint):
        # MUST define these
        super(HostServiceTicket, self).__init__()
    
        self.data['host'] = host
        self.data['port'] = port
        self.data['service'] = service
        self.data['serviceVersion'] = serviceVersion
        self.data['sessionId'] = sessionId
        self.data['sslThumbprint'] = sslThumbprint
    
    
    @property
    def host(self):
        '''The name of the host providing the service for which the ticket applies. If
        omitted, then the client uses the host name for the server that issued the
        ticket.
        '''
        return self.data['host']

    @property
    def port(self):
        '''Access to some services is made possible by connecting to a port on a server. If
        the service for which a ticket is issued is available on a particular
        port, that port number is specified with this property. If omitted, except
        in the case of connecting to CIM interfaces, the port number for the
        service that issued the ticket is used. In the case of connecting to a CIM
        interface the standard well known port for the particular service will be
        used for the connection.
        '''
        return self.data['port']

    @property
    def service(self):
        '''The name of the service to which to connect.
        '''
        return self.data['service']

    @property
    def serviceVersion(self):
        '''A dot-separated string identifying the service protocol version. For example, 1.0
        is used for NFC hosted by vpxa on ESX 2.5, and 1.1 is used for NFC hosted
        by hostd on ESX 3.0.
        '''
        return self.data['serviceVersion']

    @property
    def sessionId(self):
        '''An identifying string for the session created for the ticketed connection. This is
        used by the host service to identify the operations permitted within the
        session.
        '''
        return self.data['sessionId']

    @property
    def sslThumbprint(self):
        '''The expected thumbprint of the SSL cert of the host to which we are connecting.
        '''
        return self.data['sslThumbprint']

