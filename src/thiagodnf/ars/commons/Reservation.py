from thiagodnf.ars.commons.utils.DateTimeUtils import DateTimeUtils

class Reservation:
    """! This class is for making aircraft reservations 
    It contains the seatnumber, passenger name, and when the reservation is for. 
    """

    seatNumber = None
    passengerName = None
    when = None

    def __init__(self, seatNumber,  passengerName) :
        self.seatNumber = seatNumber
        self.passengerName = passengerName
        self.when = DateTimeUtils.getNow()

    def  getSeatNumber(self) :
        """! This gets the passengers seat number from the reservation.
        @return passenger's seat number."""
        return self.seatNumber

    def  getPassengerName(self) :
        return self.passengerName

    def  getWhenFormatted(self) :
        return DateTimeUtils.format(self.when)
