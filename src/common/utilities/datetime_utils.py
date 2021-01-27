import dateutil.parser
from datetime import datetime

class DatetimeUtils:

    @staticmethod
    def get_iso_date_from_datetime_string(date_string):
        return dateutil.parser.parse(date_string)

    @staticmethod
    def get_iso_date_from_epoch(epoch):
        return datetime.fromtimestamp(epoch).isoformat()