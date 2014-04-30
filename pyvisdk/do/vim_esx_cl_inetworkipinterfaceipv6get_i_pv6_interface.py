
import logging
from pyvisdk.exceptions import InvalidArgumentError

# This module is NOT auto-generated
# Inspired by decompiled Java classes from vCenter's internalvim25stubs.jar
# Unless states otherside, the methods and attributes were not used by esxcli,
# and thus not tested

log = logging.getLogger(__name__)

def VimEsxCLInetworkipinterfaceipv6getIPv6Interface(vim, *args, **kwargs):
    obj = vim.client.factory.create('ns0:VimEsxCLInetworkipinterfaceipv6getIPv6Interface')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'DHCPDNS', 'DHCPv6Enabled', 'Name', 'RouterAdvEnabled' ]

    for name, arg in zip(required + optional, args):
        setattr(obj, name, arg)

    for name, value in list(kwargs.items()):
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj