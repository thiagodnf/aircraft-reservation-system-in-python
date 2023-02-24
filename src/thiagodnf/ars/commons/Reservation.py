from thiagodnf.ars.commons.utils.DateTimeUtils import DateTimeUtils

class Reservation:
    """! This class represents a Reservation done on a flight or any other type of transportation.
    This provides the user a seat number, their name, and the date of their flight.  
    @author Marwa Hammami 
    @since Feb 23, 2023
    """


    
    seatNumber = None
   
    passengerName = None

    when = None

    def __init__(self, seatNumber,  passengerName) :
        self.seatNumber = seatNumber
        self.passengerName = passengerName
        self.when = DateTimeUtils.getNow()

    def  getSeatNumber(self) :
        return self.seatNumber

    def  getPassengerName(self) :
        return self.passengerName

    def  getWhenFormatted(self) :
        return DateTimeUtils.format(self.when)
