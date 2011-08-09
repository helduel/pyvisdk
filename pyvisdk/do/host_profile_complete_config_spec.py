
from pyvisdk.do.host_profile_config_spec import HostProfileConfigSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfileCompleteConfigSpec(HostProfileConfigSpec):
    '''DataObject which specifies the complete configuration of the Profile to be
        created.
    '''
    
    def __init__(self, applyProfile, customComplyProfile, disabledExpressionList, disabledExpressionListChanged):
        # MUST define these
        super(HostProfileCompleteConfigSpec, self).__init__()
    
        self.data['applyProfile'] = applyProfile
        self.data['customComplyProfile'] = customComplyProfile
        self.data['disabledExpressionList'] = disabledExpressionList
        self.data['disabledExpressionListChanged'] = disabledExpressionListChanged
    
    
    @property
    def applyProfile(self):
        '''Profile that contains information about how the host should be configured.
        '''
        return self.data['applyProfile']

    @property
    def customComplyProfile(self):
        '''User defined compliance profile. Reserved for future use.
        '''
        return self.data['customComplyProfile']

    @property
    def disabledExpressionList(self):
        '''DefaultComplyProfile is automatically generated by the system. User can control
        which of the expressions are disabled by using this field. All expressions
        are enabled by default.
        '''
        return self.data['disabledExpressionList']

    @property
    def disabledExpressionListChanged(self):
        '''Flag indicating if this configSpec has changes for the disabledExpressionList If
        False, contents of disabledExpressionList will be ignored.
        '''
        return self.data['disabledExpressionListChanged']

