from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.features.Controller import Controller

class AlertController(Controller):

    """! This class represents an alert cor the main controller
@author Corbin M.
@since feb. 2023"""
    message = str()

    def __init__(self, message):
        self.message = message

    def display(self):

        ConsoleUtils.println("")
        ConsoleUtils.showError(self.message)

        return 0
