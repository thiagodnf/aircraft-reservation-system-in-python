from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.features.Controller import Controller

class MenuController(Controller):
    """!The MenuController class displays the controller 
    and its sub menus for a userto do inputs for a reservation """
    def display(self):

        ConsoleUtils.println("Home")
        ConsoleUtils.printLine()
        ConsoleUtils.println("1 - Reserve Seat")
        ConsoleUtils.println("2 - Cancel Reservation")
        ConsoleUtils.println("3 - Display Aircraft")
        ConsoleUtils.println("4 - List of Passengers")
        ConsoleUtils.println("5 - Exit")
        ConsoleUtils.printLine()
        """!When the display is defined, it prints the sub menus"""

        option = ConsoleUtils.askInteger("Option: ")

        if option == 1:
            return ControllerId.RESERVE_A_SEAT
        elif option == 2:
            return -1
        elif option == 3:
            return ControllerId.DISPLAY_AIRCRAFT
        elif option == 4:
            return ControllerId.LIST_OF_PASSENGERS
        elif option == 5:
            ConsoleUtils.printFooter()
            quit()
        else:
            raise RuntimeError("Invalid option. Type a number between 1 to 5")
        """!When different numbers are used they return the user to the main page
        Initiates a error when a number is less than 1 or greater then 5"""
