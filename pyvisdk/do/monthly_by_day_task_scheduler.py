
from pyvisdk.do.monthly_task_scheduler import MonthlyTaskScheduler
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MonthlyByDayTaskScheduler(MonthlyTaskScheduler):
    '''The MonthlyByDayTaskScheduler data object sets the time for monthly task
        execution. You can set the schedule for task execution on one day during
        the month, and you complete the schedule by setting the inherited
        properties for the hour and minute.By default the scheduler executes the
        task on the specified day every month. If you set the interval to a value
        greater than 1, the task will execute at the specified monthly interval.
        (For example, an interval of 2 will cause the task to execute on the
        specified day, hour, and minute every 2 months.)
    '''
    
    def __init__(self, day):
        # MUST define these
        super(MonthlyByDayTaskScheduler, self).__init__()
    
        self.data['day'] = day
    
    
    @property
    def day(self):
        '''The day in every month to run the scheduled task. Valid values are 1 to 31.
        '''
        return self.data['day']

