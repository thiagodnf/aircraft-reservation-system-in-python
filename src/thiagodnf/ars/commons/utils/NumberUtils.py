import re

from thiagodnf.ars.commons.utils.StringUtils import StringUtils

class NumberUtils:
    """! Verifies if the string is an integer
    and if the string is blank, user gets an error.
    """
    @classmethod
    def isInt(cls, str_):
        """! Verify if a given string is an integer
        @param str_ string to be verified
        @return True if it is a string, False, otherwise.
        """

        p = re.compile(r'-?\d+')

        if StringUtils.isBlank(str_):
            return False

        return bool(p.match(str_))

    @classmethod
    def toInt(cls, str_):
        """! this function determines if the string is blank 
        or not.
        If string is blank alert user that it shoulf not be
        @param cls Clears screen
        @param str_ returns object to string
        @return integer from str_
        """
        if StringUtils.isBlank(str_):
            raise RuntimeError("The string should not be blank")

        return int(str_)
