import datetime
import time
def this_moment(fmt = '%Y-%m-%d %H-%M-%S'):
    return datetime.datetime.fromtimestamp(time.time()).strftime(fmt)