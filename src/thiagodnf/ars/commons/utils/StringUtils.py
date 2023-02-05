class StringUtils(object):

    @classmethod
    def isBlank(cls, str_):

        return str_ == None or len(str_.strip()) == 0
