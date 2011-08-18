
from pyvisdk.do.option_type import OptionType
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LongOption(OptionType):
    '''The LongOption data object type is used to define the minimum, maximum, and
        default values for a 64-bit long option.
    '''
    
    def __init__(self, defaultValue, max, min):
        # MUST define these
        super(LongOption, self).__init__()
    
        self.data['defaultValue'] = defaultValue
        self.data['max'] = max
        self.data['min'] = min
    
    
    @property
    def defaultValue(self):
        '''The default value.
        '''
        return self.data['defaultValue']

    @property
    def max(self):
        '''The maximum value.
        '''
        return self.data['max']

    @property
    def min(self):
        '''The minimum value.
        '''
        return self.data['min']
