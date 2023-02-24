import platform

class OSUtils:
    """! This class represents the OS utilites used by the application.
    @autor Corbin M.
    @Since feb.2023"""
    @classmethod
    def isWindows(cls):
        """! Verify if the operational system used is Windows
        @return True if it is Windows, False, otherwise.
        """

        return platform.system() == "Windows"

    @classmethod
    def isMac(cls):
        return platform.system() == "Darwin"

    @classmethod
    def isUnix(cls):
        return platform.system() == "Linux"
