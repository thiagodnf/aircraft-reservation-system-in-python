import datetime

class DateTimeUtils(object):

    @classmethod
    def getNow(cls):
        return datetime.datetime.now()

    @classmethod
    def format(cls, dateTime):

        format = "%Y-%m-%d %H:%M:%S"

        return dateTime.strftime(format)
