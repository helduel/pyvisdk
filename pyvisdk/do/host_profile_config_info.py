
from pyvisdk.do.profile_config_info import ProfileConfigInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfileConfigInfo(ProfileConfigInfo):
    '''
    '''
    
    def __init__(self, applyProfile, customComplyProfile, defaultComplyLocator, defaultComplyProfile, disabledExpressionList):
        # MUST define these
        super(HostProfileConfigInfo, self).__init__()
    
        self.data['applyProfile'] = applyProfile
        self.data['customComplyProfile'] = customComplyProfile
        self.data['defaultComplyLocator'] = defaultComplyLocator
        self.data['defaultComplyProfile'] = defaultComplyProfile
        self.data['disabledExpressionList'] = disabledExpressionList
    
    
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
    def defaultComplyLocator(self):
        '''Association between applyProfile and defaultComplyProfile. This field contains the
        link between which expression was generated by which part of the
        applyProfile. This can be used by the User Interfaces to provide
        contextual information to the user.
        '''
        return self.data['defaultComplyLocator']

    @property
    def defaultComplyProfile(self):
        '''Default compliance profile that is generated from the applyProfile. If the
        applyProfile is modified, defaultComplyProfile will be automatically
        modified to match it.
        '''
        return self.data['defaultComplyProfile']

    @property
    def disabledExpressionList(self):
        '''DefaultComplyProfile is automatically generated by the system. User can control
        which of the expressions are disabled by using this field. All expressions
        are enabled by default.
        '''
        return self.data['disabledExpressionList']

