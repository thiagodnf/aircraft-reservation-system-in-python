import datetime

class DateTimeUtils(object):
    """! deals with getting the date and time 
    on request and formats it.
    """
    @classmethod
    def getNow(cls):
        """! this function clears the screen 
        and returns the date and time of current.
        @param cls Clears screen
        @return date and time currently
        """
        return datetime.datetime.now()

    @classmethod
    def format(cls, dateTime):
        """! deals with formatting the date and 
        time, while putting it into a string.
        @param cls Clears screen
        @param dateTime recieves dateTime info
        @return date and time in the format given
        """
        format = "%Y-%m-%d %H:%M:%S"

        return dateTime.strftime(format)
