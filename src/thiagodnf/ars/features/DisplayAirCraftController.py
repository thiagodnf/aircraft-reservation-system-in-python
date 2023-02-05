from thiagodnf.ars.commons.Aircraft import Aircraft
from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.features.Controller import Controller

class DisplayAirCraftController(Controller):

    def display(self):

        ConsoleUtils.println("Home >> Display Aircraft")
        ConsoleUtils.printLine()

        Aircraft.print()

        ConsoleUtils.pressEnterToContinue()

        return ControllerId.MENU
