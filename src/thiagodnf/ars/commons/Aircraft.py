import re

from thiagodnf.ars.commons.Database import Database
from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.commons.utils.StringUtils import StringUtils

class Aircraft:

    numberOfRows = 7

    numberOfColumns = 2

    @staticmethod
    def print():

        reservations = Database.getInstance().getReservations()

        seats = """
                                      @@@@@@
                                     @@@@@@@@
                                    @@@@@@@@@@
                                   @----||----@
                                   @ 1A || 1B @
              =====================@----||----@=====================
             @@@@@@@@@@@@@@@@@@@@@@@ 2A || 2B @@@@@@@@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@@@@@@@@@@----||----@@@@@@@@@@@@@@@@@@@@@@@@
             @@@@@@@@@@@@@@@@@@@@@@@ 3A || 3B @@@@@@@@@@@@@@@@@@@@@@@
              =====================@----||----@=====================
                                   @ 4A || 4B @
                                   @----||----@
                                   @ 5A || 5B @
                                   @----||----@
                                   @ 6A || 6B @
                                   @----||----@
                                   @ 7A || 7B @
                                   @----||----@
                        ===========@@@@@@@@@@@@===========
                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        ===========@@@@@@@@@@@@===========
                                     @@@@@@@@
            """;

        for reservation in reservations:
            seats = seats.replace(reservation.getSeatNumber(), ConsoleUtils.setRedColor("XX"));

        ConsoleUtils.println(seats)

    @staticmethod
    def getValidSeatNumbers():

        validSeats = []

        for i in range(1, Aircraft.numberOfRows+1):

            for j in range(0, Aircraft.numberOfColumns):
                validSeats.append(str(i) + "" + chr(j + 65))

        return validSeats

    @staticmethod
    def isValidSeatNumber(seatNumber):
        """! This method provides the user if the seat number provided is valid or invalid. 
        @param seatNumber provide seatNumber.
        @return True if seat is valid.
        @return False if seat in not valid.
        """

        validSeats = Aircraft.getValidSeatNumbers()

        if seatNumber in validSeats:
            return True
        else:
            return False

    @staticmethod
    def isValidSeatNumberFormat(seatNumber):

        if StringUtils.isBlank(seatNumber):
            return False

        p = re.compile(r'\d+[a-zA-Z]')

        # It is valid if the format is NUMBER+LETTER
        return bool(p.match(seatNumber))
