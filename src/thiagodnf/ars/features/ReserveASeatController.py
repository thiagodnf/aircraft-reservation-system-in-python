from thiagodnf.ars.commons.Aircraft import Aircraft
from thiagodnf.ars.commons.ControllerId import ControllerId
from thiagodnf.ars.commons.Database import Database
from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.commons.utils.StringUtils import StringUtils
from thiagodnf.ars.features.Controller import Controller

class ReserveASeatController(Controller):
        """! This class is used to reserve a seat. It begins by displaying the aircraft in the terminal, then asks the user what seat they want.
        After selecting a seat, the program prompts for the name.
        """

def display(self):

    """! This method displays the available seats on the plane. The user can select whatever seat they want.
    There is exception handling for data that is entered incorrectly, or for when seats are already occupied.
    @param seatNumber   The seat number that the user inputs
    @param passengerName   The passenger name that the user inputs
    @return controllerID.MENU   This returns the user to the main menu
    """

    ConsoleUtils.println("Home >> Reserve Seat")
    ConsoleUtils.printLine()

    ## Calls the aircraft class and displays the seats on the plane
    Aircraft.print()

    ## Calls the askSeatNumber method
    seatNumber = self.askSeatNumber()
    ## Calls the askPassengerName method
    passengerName = self.askPassengerName()

    ## Reserves the seat using data from the askPassengerName and seatNumber methods
    Database.getInstance().reserve(seatNumber, passengerName)

    return ControllerId.MENU

def askPassengerName(self):
    """! Ask the passenger name. If the user provides a blank string
    a RuntimeError still be raised.
    @param passengerName   The name of the passenger
    @return the passenger name
    """

    ## Asks for the passenger name
    passengerName = ConsoleUtils.askString("Passenger Name: ")

    ## Exception handling for a blank name
    if StringUtils.isBlank(passengerName):
        raise RuntimeError("The passenger name should not be empty")

    return passengerName

def askSeatNumber(self):
    """"! Asks for the seat number that the passenger wants. If the user does not supply an input, an error is thrown.
    If an invalid input is entered, an error is thrown. If the wrong format is entered, an error is thrown. If a seat is already reserved, an error is thrown.
    Each time an error occurs, the user gets to re-enter the information until a valid entry is entered.
    This program also converts the entered seat number to uppercase.
    @param seatNumber   The seat number of the passenger, converted into uppercase
    @return seatNumber     This is the seat number that is entered into the database
    """

    seatNumber = ConsoleUtils.askString("Seat Number: ")

    ## Exception handling if statements

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
