from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils

from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.features.ListofPassengersController import ListofPassengersController
from thiagodnf.ars.features.DisplayAirCraftController import DisplayAirCraftController
from thiagodnf.ars.features.MenuController import MenuController
from thiagodnf.ars.features.AlertController import AlertController
from thiagodnf.ars.features.ReserveASeatController import ReserveASeatController

class ControllerManager(object):

    def getControllerById(self, id):

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

        currentId = ControllerId.MENU

        while True:

            ConsoleUtils.clearScreen()

            try:

                current = self.getControllerById(currentId)

                currentId = current.display()

            except Exception as ex:
                ConsoleUtils.clearScreen()
                AlertController(str(ex)).display()
