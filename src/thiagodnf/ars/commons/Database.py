from thiagodnf.ars.commons.Reservation import Reservation

class Database:
    """!Database is the starting class for a function"""
    instance_ = None
    reservations = []

    @classmethod
    def getInstance(cls):
        if cls.instance_ is None:
            cls.instance_ = cls.__new__(cls)
            # Put any initialization here.
        return cls.instance_
   
    def getReservations(self):
        return self.reservations
    """!When the getReservations are defined, it will return with the reservations"""
    def isAvailable(self, seatNumber):

        reservation = self.getReservationBySeatNumber(seatNumber)

        return reservation == None
    """!The Availability will be given by seat number
        The reservation will be saved 
        The availability of a seat will be displayed 
       """
    def reserve(self, seatNumber, passengerName):

        """! Save into the database the seat number and passenger name
        @param seatNumber The seat number to be saved
        @param passengerName the passenger name to be saved
        """

        self.reservations.append(Reservation(seatNumber, passengerName))

    def getReservationBySeatNumber(self, seatNumber):

        for reservation in self.reservations:

            if reservation.getSeatNumber() == seatNumber:
                return reservation

        return None
    """!The reservation will be given by seat number and self 
    Will be returned as none if a seat number is not available
    Will return with reservation if seat number is available
    """