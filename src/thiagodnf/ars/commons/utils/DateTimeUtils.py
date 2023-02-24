import datetime

class DateTimeUtils(object):
    """! this class is for the Date Time utilities intergrated into the app
    @author Corbin M.
    @since Feb. 2023"""
    @classmethod
    def getNow(cls):
        return datetime.datetime.now()

    @classmethod
    def format(cls, dateTime):

        format = "%Y-%m-%d %H:%M:%S"

        return dateTime.strftime(format)
