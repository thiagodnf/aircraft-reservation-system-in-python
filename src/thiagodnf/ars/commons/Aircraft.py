import re

from thiagodnf.ars.commons.Database import Database
from thiagodnf.ars.commons.utils.ConsoleUtils import ConsoleUtils
from thiagodnf.ars.commons.utils.StringUtils import StringUtils

class Aircraft:
    """! This class represents the layout of the aircraft the program is using.
        @author Justin Wareham
        @since 2023-2-24
    """

    numberOfRows = 7

    numberOfColumns = 2

    @staticmethod
    def print():
        """! This method prints the aircraft on screen with the amount
            of remaining reservations.
            @author Justin Wareham
            @since 2023-2-24
        """
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

        validSeats = Aircraft.getValidSeatNumbers()

        if seatNumber in validSeats:
            return True
        else:
            return False

    @staticmethod
    def isValidSeatNumberFormat(seatNumber):
        """! Checks if the seat number format is correct
        @param ValidSeatNumber"""
        
        if StringUtils.isBlank(seatNumber):
            return False

        p = re.compile(r'\d+[a-zA-Z]')

        # It is valid if the format is NUMBER+LETTER
        return bool(p.match(seatNumber))
