from thiagodnf.ars.commons.Aircraft import Aircraft
from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.commons.Database import Database
from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.commons.utils.StringUtils import StringUtils
from thiagodnf.ars.features.Controller import Controller

class ReserveASeatController(Controller):
    """! This class prompts the user to reserve a seat by first displaying the menu for them to choose a seat then asking them to provide their name.
    The user will be asked to provide the seat they wish to have and their name in order to reserve a seat.
    @author Marwa Hammami 
    @since Feb 23, 2023
    """


    def display(self):

        ConsoleUtils.println("Home >> Reserve Seat")
        ConsoleUtils.printLine()

        Aircraft.print()

        seatNumber = self.askSeatNumber()
        passengerName = self.askPassengerName()

        Database.getInstance().reserve(seatNumber, passengerName)

        return ControllerId.MENU

    def askPassengerName(self):
        """! Ask the passenger name. If the user provides a blank string
        a RuntimeError still be raised.
        @return the passenger name
        """

        passengerName = ConsoleUtils.askString("Passenger Name: ")

        if StringUtils.isBlank(passengerName):
            raise RuntimeError("The passenger name should not be empty")

        return passengerName

    def askSeatNumber(self):

        seatNumber = ConsoleUtils.askString("Seat Number: ")

        if StringUtils.isBlank(seatNumber):
            raise RuntimeError("The seat number should not be empty")

        #  we need to make all letter capitalized to have consistency
        seatNumber = seatNumber.upper()

        if not Aircraft.isValidSeatNumberFormat(seatNumber):
            raise RuntimeError("The seat number is in the wrong format")

        if not Aircraft.isValidSeatNumber(seatNumber):
            raise RuntimeError("The airplane does not have this seat")

        if not Database.getInstance().isAvailable(seatNumber):
            raise RuntimeError("The seat number is not available. Try another one")

        return seatNumber
