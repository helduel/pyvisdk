
from pyvisdk.do.alarm_expression import AlarmExpression
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StateAlarmExpression(AlarmExpression):
    '''An alarm expression that uses the running state of either a virtual machine or a
        host as the condition that triggers the alarm. Base type.There are two
        alarm operands: yellow and red. At least one of them must be set. The
        value of the alarm expression is determined as follows:* If the red state
        is set but the yellow state is not: the expression is red when the state
        operand matches (isEqual operator) or does not match (isUnequal operator)
        the state of the managed entity. The expression is green otherwise. * If
        yellow is set but red is not: the expression is yellow when the state
        operand matches (isEqual) or does not match (isUnequal) the state of the
        managed entity. The expression is green otherwise. * If both yellow and
        red are set, the value of the expression is red when the red state operand
        matches (isEqual) or does not match (isUnequal) the state of the managed
        entity. Otherwise, the expression is yellow when the yellow state operand
        matches (isEqual) or does not match (isUnequal) the state of the managed
        entity. Otherwise, the expression is green.
    '''
    
    def __init__(self, operator, red, statePath, type, yellow):
        # MUST define these
        super(StateAlarmExpression, self).__init__()
    
        self.data['operator'] = operator
        self.data['red'] = red
        self.data['statePath'] = statePath
        self.data['type'] = type
        self.data['yellow'] = yellow
    
    
    @property
    def operator(self):
        '''The operation to be tested on the target state.
        '''
        return self.data['operator']

    @property
    def red(self):
        '''Whether or not to test for a red condition. If this property is not set, do not
        calculate red status.
        '''
        return self.data['red']

    @property
    def statePath(self):
        '''Path of the state property.
        '''
        return self.data['statePath']

    @property
    def type(self):
        '''Name of the object type containing the property.
        '''
        return self.data['type']

    @property
    def yellow(self):
        '''Whether or not to test for a yellow condition. If this property is not set, do not
        calculate yellow status.
        '''
        return self.data['yellow']

