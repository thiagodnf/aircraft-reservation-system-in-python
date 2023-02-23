import os

from thiagodnf.ars.commons.utils.NumberUtils import NumberUtils
from thiagodnf.ars.commons.utils.OSUtils import OSUtils

class ConsoleUtils(object):
    """! The ConsoleUtils class.
    Deals with a wide range of outputs specific
    to each method, as well as clearing the screen.
    """
    ANSI_RED = "\033[0;31m"
    ANSI_GREEN = "\033[0;32m"
    ANSI_RESET = "\u001B[0m"

    @classmethod
    def printLine(cls):
        """! Prints a dashed line.
        @param cls Clears screen
        """
        ConsoleUtils.println("------------------------------------------------------------")

    @classmethod
    def clearScreen(cls):
        """! Clears screen based on operating system 
        and prints header.
        If OS is Windows use 'cls'
        Else If OS is Mac use '\033c'
        Else OS is different use 'clear'
        @param cls Clears screen
        """
        if OSUtils.isWindows():
            os.system('cls')
        elif OSUtils.isMac():
            print("\033c")
        else:
            os.system('clear')

        ConsoleUtils.printHeader()

    @classmethod
    def println(cls, str_):
        """! prints ConsoleUtils.ANSI_RESET 
        in string format.
        @param cls Clears screen
        @param str_ returns string of an object
        """
        print(str_ + ConsoleUtils.ANSI_RESET)

    @classmethod
    def printHeader(cls):
        """! Returns a string in between the printLine 
        function.
        @param cls Clears screen
        """
        ConsoleUtils.printLine()
        ConsoleUtils.println("Aircraft Reservation System - v0.0.1")
        ConsoleUtils.printLine()

    @classmethod
    def printFooter(cls):
        """! returns a string in the color green.
        @param cls Clears screen
        """
        ConsoleUtils.println(ConsoleUtils.setGreenColor("Bye! =)"))

    @classmethod
    def showError(cls, text):

        ConsoleUtils.println(ConsoleUtils.setRedColor("> Oops! " + text))
        ConsoleUtils.println("")
        ConsoleUtils.pressEnterToContinue()

    @classmethod
    def askString(cls, prefix):
        ConsoleUtils.println(prefix)
        #  Ask the user for any string
        text = input()
        if text == None:
            return None
        #  A good approach would be removing all leading and trailing spaces before returning it
        return text.strip()

    @classmethod
    def askInteger(cls, field):

        text = ConsoleUtils.askString(field)

        if not NumberUtils.isInt(text):
            raise RuntimeError("This is not an integer number. Please try again.")

        return NumberUtils.toInt(text)

    @classmethod
    def pressEnterToContinue(cls):
        """ generated source for method pressEnterToContinue """
        cls.askString("Press \"ENTER\" to continue...")

    @classmethod
    def setRedColor(cls, str_):

        return cls.ANSI_RED + str_ + cls.ANSI_RESET

    @classmethod
    def setGreenColor(cls, str_):

        return cls.ANSI_GREEN + str_ + cls.ANSI_RESET
