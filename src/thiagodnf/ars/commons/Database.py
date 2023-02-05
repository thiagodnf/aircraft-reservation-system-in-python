from thiagodnf.ars.commons.Reservation import Reservation

class Database:

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

    def isAvailable(self, seatNumber):

        reservation = self.getReservationBySeatNumber(seatNumber)

        return reservation == None

   #
    #      * Save into the database the seat number and passenger name
    #      *
    #      * @param seatNumber The seat number to be saved
    #      * @param passengerName the passenger name to be saved
    #
    def reserve(self, seatNumber, passengerName):
        self.reservations.append(Reservation(seatNumber, passengerName))

    def getReservationBySeatNumber(self, seatNumber):

        for reservation in self.reservations:

            if reservation.getSeatNumber() == seatNumber:
                return reservation

        return None
