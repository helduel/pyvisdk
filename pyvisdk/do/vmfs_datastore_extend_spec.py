
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmfsDatastoreExtendSpec(vim, *args, **kwargs):
    '''Specification to increase the capacity of a VMFS datastore by adding one or
    more new extents to the datastore. All the extents to be added must be on the
    same disk. Extension is different from creation in that the VMFS creation
    specification need not be specified.'''
    
    obj = vim.client.factory.create('ns0:VmfsDatastoreExtendSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    required = [ 'extent', 'partition', 'diskUuid' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]
    
    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    