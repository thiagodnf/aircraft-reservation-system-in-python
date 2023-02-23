from thiagodnf.ars.commons.utils.DateTimeUtils import DateTimeUtils

class Reservation:
    """! This class is for making aircraft reservations 
    It contains the seatnumber, passenger name, and when the reservation is for. 
    """

    seatNumber = None
    passengerName = None
    when = None

    def __init__(self, seatNumber,  passengerName) :
        """! This assigns the variables types to the name of the object. 
        @param seatNumber the seatnumber name to the variable.
        @param passengerName the passengerName name to the variable.
        @param when, the time of the reservation to the date variable. """
        self.seatNumber = seatNumber
        self.passengerName = passengerName
        self.when = DateTimeUtils.getNow()

    def  getSeatNumber(self) :
        """! This gets the passengers seat number from the reservation.
        @return passenger's seat number."""
        return self.seatNumber

    def  getPassengerName(self) :
        """! This gets the passenger's name from the reservation.
        @return passenger's name. """
        return self.passengerName

    def  getWhenFormatted(self) :
        """! This gets the format for the passenger's reservation time. 
        @return the time and date of the passenger's reservation."""
        return DateTimeUtils.format(self.when)
