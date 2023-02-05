import re

from thiagodnf.ars.commons.utils.StringUtils import StringUtils

class NumberUtils:
    #
    #      * Verify if a given string is an integer
    #      * @param str string to be verified
    #      * @return True if it is a string, False, otherwise.
    #
    @classmethod
    def isInt(cls, str_):

        p = re.compile(r'-?\d+')

        if StringUtils.isBlank(str_):
            return False

        return bool(p.match(str_))

    @classmethod
    def toInt(cls, str_):

        if StringUtils.isBlank(str_):
            raise RuntimeError("The string should not be blank")

        return int(str_)
