from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils

from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.features.ListofPassengersController import ListofPassengersController
from thiagodnf.ars.features.DisplayAirCraftController import DisplayAirCraftController
from thiagodnf.ars.features.MenuController import MenuController
from thiagodnf.ars.features.AlertController import AlertController
from thiagodnf.ars.features.ReserveASeatController import ReserveASeatController

class ControllerManager(object):
    """! This class represents the overall controller manager. 
    The controller is the set of options you have and what it returns.
    @author Justin Wareham
    """

    def getControllerById(self, id):
        """! This method allows for the controller to recognize
        numbers for actions.
        @param id   the id is the number the user inputs in
        @author Justin Wareham
        """
        if id == ControllerId.MENU:
            return MenuController()
        elif id == ControllerId.LIST_OF_PASSENGERS:
            return ListofPassengersController()
        elif id == ControllerId.DISPLAY_AIRCRAFT:
            return DisplayAirCraftController()
        elif id == ControllerId.RESERVE_A_SEAT:
            return ReserveASeatController()
        else:
            raise RuntimeError("Controller id not found")

    def run(self):
        """! This method allows for the input to be recognized as the id.
            @author Justin Wareham
        """
        currentId = ControllerId.MENU

        while True:

            ConsoleUtils.clearScreen()

            try:

                current = self.getControllerById(currentId)

                currentId = current.display()

            except Exception as ex:
                ConsoleUtils.clearScreen()
                AlertController(str(ex)).display()
