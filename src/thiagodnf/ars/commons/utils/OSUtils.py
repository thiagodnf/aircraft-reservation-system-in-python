import platform

class OSUtils:
    """! Identifies what operating system 
    user is on and returns it.
    """
    @classmethod
    def isWindows(cls):
        """! Verify if the operational system used is Windows
        @param cls clears screen
        @return True if it is Windows, False, otherwise.
        """

        return platform.system() == "Windows"

    @classmethod
    def isMac(cls):
        """! Verifies if the operating system used is Mac
        @param cls clears screen
        @return True if it is Mac, False, otherwise.
        """
        return platform.system() == "Darwin"

    @classmethod
    def isUnix(cls):
        """! Verifies if the operating system used is Linux
        @param cls clears screen
        @return True if it is Linux, False, otherwise.
        """
        return platform.system() == "Linux"
