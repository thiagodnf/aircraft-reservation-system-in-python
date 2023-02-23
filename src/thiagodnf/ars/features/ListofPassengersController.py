from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.features.Controller import Controller
from thiagodnf.ars.commons.Database import Database
from thiagodnf.ars.commons.Aircraft import Aircraft

class ListofPassengersController(Controller):
    """! This class lists all of the passengers on the aircraft.
    """

    db = Database.getInstance()

    def display(self):
        """! This method prints the list of passengers based off of information contained in the passenger database.
        The user can press enter after reviewing the information to return to the main menu.
        If there is no reservation, then nothing is displayed. Otherwise, all of the existing reservations will be displayed.
        @return controllerID.MENU   Returns the user to the menu
        """

        ConsoleUtils.println("Home >> List of Passengers")
        ConsoleUtils.printLine()

        for seatNumber in Aircraft.getValidSeatNumbers():

            output = seatNumber + "\t"

            reservation = self.db.getReservationBySeatNumber(seatNumber)

            if reservation == None:
                output += ConsoleUtils.setGreenColor("Empty")
            else:
                output += ConsoleUtils.setRedColor(self.getWhen(reservation)) + "\t"
                output += ConsoleUtils.setRedColor(self.getPassengerName(reservation)) + "\t"

            ConsoleUtils.println(output)

        ConsoleUtils.println("")
        ConsoleUtils.pressEnterToContinue()

        return ControllerId.MENU

    @classmethod
    def getPassengerName(cls, reservation):
        """! This method pulls the names of passengers from the data database. If there are no reservations, then nothing will be returned.
        @param cls  Clears screen
        @param reservation   The list of reservations from the DB
        @return reservation  Returns the reservations from the DB
        """

        if reservation == None:
            return ""

        return reservation.getPassengerName()

    @classmethod
    def getWhen(cls, reservation):
        """! This method displays a reservation when it is properly formatted. If there are no reservations, then nothing will be returned.
        @param cls   Clears the screen
        @param reservation   The list of reservations from the DB
        @return reservation   Returns the formatted reservation
        """

        if reservation == None:
            return ""

        return reservation.getWhenFormatted()
