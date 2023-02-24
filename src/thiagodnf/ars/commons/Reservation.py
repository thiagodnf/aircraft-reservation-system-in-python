from thiagodnf.ars.commons.utils.DateTimeUtils import DateTimeUtils

class Reservation:
    """! This class represents a Reservation done on a flight or any other type of transportation.
    This provides the user a seat number, their name, and the date of their flight.  
    @author Marwa Hammami 
    @since Feb 23, 2023
    """


    """! This field provides the user their seatNumber"""
    seatNumber = None
    """! This provides the user their Name (passangerName)"""
    passengerName = None
    """! This provides the user when their flight (or trip) is."""
    when = None

    def __init__(self, seatNumber,  passengerName) :
        """! This method provides the user their seatNumber, their name (PassengerName), and when time of their flight.
        @param seatnumber this is the users seat number
        @param passengerName this is the passenger name
        """
        self.seatNumber = seatNumber
        self.passengerName = passengerName
        self.when = DateTimeUtils.getNow()

    def  getSeatNumber(self) :
        """! This method provides the user to get their seat number.
        @return seatNumber
        """
        return self.seatNumber

    def  getPassengerName(self) :
        """! This method provides the user their name (passangerName).
        @return passengerName
        """
        return self.passengerName

    def  getWhenFormatted(self) :
        """! This method provides the user  
        @return the users dateTime of their flight. 
        """
        return DateTimeUtils.format(self.when)

