import uuid
from common.utilities.datetime_utils import DatetimeUtils

class ProductHistory(object):
    def __init__(self,
                 epoch_time=None,
                 date_time=None,
                 low=None,
                 high=None,
                 open=None,
                 close=None,
                 volume=None,
                 _id=None):
        epoch_time = epoch_time
        date_time = DatetimeUtils.iso_date()

    def __call__(self):
        pass

    def json(self):
        return {

        }


    #[ time, low, high, open, close, volume ]