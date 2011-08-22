
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostActiveDirectoryInfo(vim, *args, **kwargs):
    '''The HostActiveDirectoryInfo data object describes ESX host membership in an
    Active Directory domain. If the HostAuthenticationStoreInfo.enabled property is
    , the host is a member of a domain and the ESX Server will set the domain
    information properties.'''
    
    obj = vim.client.factory.create('ns0:HostActiveDirectoryInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'enabled' ]
    inherited = [ 'domainMembershipStatus', 'joinedDomain', 'trustedDomain' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    