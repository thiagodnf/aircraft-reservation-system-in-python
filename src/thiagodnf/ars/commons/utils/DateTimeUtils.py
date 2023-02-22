import datetime

class DateTimeUtils(object):
    """! deals with getting the date and time 
    on request and formats it.
    """
    @classmethod
    def getNow(cls):
        """! this function returns the date and 
        time of current.
        @param cls Clears screen
        """
        return datetime.datetime.now()

    @classmethod
    def format(cls, dateTime):
        """! deals with formatting the date and 
        time, while putting it into a string.
        @param cls Clears screen
        @param dateTime recieves dateTime info
        """
        format = "%Y-%m-%d %H:%M:%S"

        return dateTime.strftime(format)
