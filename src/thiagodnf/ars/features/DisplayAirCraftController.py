from thiagodnf.ars.commons.Aircraft import Aircraft
from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.features.Controller import Controller

class DisplayAirCraftController(Controller):
    """! This class displays the aircraft seats and shows which ones are reserved and which ones are still available.
    The user can return to the main menu when finished reviewing the seats.
    """

    def display(self):
        """! This method displays the aircraft. It prints the aircraft to the screen
        @return ControllerID.MENU   returns the user to the main menu
        """

        ConsoleUtils.println("Home >> Display Aircraft")
        ConsoleUtils.printLine()

        Aircraft.print()

        ConsoleUtils.pressEnterToContinue()

        return ControllerId.MENU
