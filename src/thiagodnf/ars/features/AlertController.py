from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.features.Controller import Controller

class AlertController(Controller):
    """! This is responsible for error handling. If the user enters the wrong input, an error will be thrown.
    """

    message = str()
    def __init__(self, message):
        self.message = message

    def display(self):

        ConsoleUtils.println("")
        ConsoleUtils.showError(self.message)

        return 0
