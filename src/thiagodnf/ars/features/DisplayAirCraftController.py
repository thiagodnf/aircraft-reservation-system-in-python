from thiagodnf.ars.commons.Aircraft import Aircraft
from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.features.Controller import Controller

class DisplayAirCraftController(Controller):
    """! This class displays the picture of the aircraft after the user enters the 'Display Aircraft' menu."""

    def display(self):

        ConsoleUtils.println("Home >> Display Aircraft")
        ConsoleUtils.printLine()

        Aircraft.print()

        ConsoleUtils.pressEnterToContinue()

        return ControllerId.MENU
