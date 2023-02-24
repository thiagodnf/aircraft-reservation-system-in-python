from thiagodnf.ars.commons.Aircraft import Aircraft
from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.features.Controller import Controller

class DisplayAirCraftController(Controller):
    """! This class displays to the user the display of the aircraft.  
    It prints the aircraft layout.
    @author Marwa Hammami 
    @since Feb 23, 2023
    """

    def display(self):

        ConsoleUtils.println("Home >> Display Aircraft")
        ConsoleUtils.printLine()

        Aircraft.print()

        ConsoleUtils.pressEnterToContinue()

        return ControllerId.MENU
