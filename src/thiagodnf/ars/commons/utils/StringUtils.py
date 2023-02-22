class StringUtils(object):
    """! checks whether string is blank or not
    """
    @classmethod
    def isBlank(cls, str_):

        return str_ == None or len(str_.strip()) == 0
