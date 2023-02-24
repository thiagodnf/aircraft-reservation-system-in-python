from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.features.Controller import Controller
from thiagodnf.ars.commons.Database import Database
from thiagodnf.ars.commons.Aircraft import Aircraft

class ListofPassengersController(Controller):
    """! This class portrays the list of passengers on the aircraft.
    It prints the seat number, reservation status, reservation time, and passenger name for the seat.
    @author Marwa Hammami 
    @since Feb 23, 2023
    """

    db = Database.getInstance()

    def display(self):

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

        if reservation == None:
            return ""

        return reservation.getPassengerName()

    @classmethod
    def getWhen(cls, reservation):

        if reservation == None:
            return ""

        return reservation.getWhenFormatted()
