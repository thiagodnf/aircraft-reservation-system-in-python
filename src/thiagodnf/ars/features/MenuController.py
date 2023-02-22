from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.features.Controller import Controller

class MenuController(Controller):
    """! This class displays the menu when the program is first run. Users can choose various options that relate to managing their reservation.
    @param Controller   The menu that gets displayed
    """

    def display(self):

        """! This method is for displaying the main menu of the program. When running, a user can choose between reserving a seat, cancelling a reservation,
        displaying the aircraft and available seats, and displaying a list of passengers. An option to exit is also provided. The user can choose the corresponding option
        to access the sub-feature. If an invalid option is entered, an exception is thrown.
        """

        ConsoleUtils.println("Home")
        ConsoleUtils.printLine()
        ConsoleUtils.println("1 - Reserve Seat")
        ConsoleUtils.println("2 - Cancel Reservation")
        ConsoleUtils.println("3 - Display Aircraft")
        ConsoleUtils.println("4 - List of Passengers")
        ConsoleUtils.println("5 - Exit")
        ConsoleUtils.printLine()

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
