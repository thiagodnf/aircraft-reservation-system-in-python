import platform

class OSUtils:

     #/**
#      * Verify if the operational system used is Windows
#      *
#      * @return true if is Windows. False otherwise
#      */
    @classmethod
    def isWindows(cls):
        return platform.system() == "Windows"

    @classmethod
    def isMac(cls):
        return platform.system() == "Darwin"

    @classmethod
    def isUnix(cls):
        return platform.system() == "Linux"
