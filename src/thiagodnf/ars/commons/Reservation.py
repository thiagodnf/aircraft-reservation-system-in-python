from thiagodnf.ars.commons.utils.DateTimeUtils import DateTimeUtils

class Reservation:

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
