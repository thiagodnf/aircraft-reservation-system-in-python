from thiagodnf.ars.commons.ControllerManager import ControllerManager

class MainClass(object):
    """! Everything starts in this class.
       @author Thiago Ferreira
       @since 2022-02-25
    """

    @classmethod
    def main(self):
        """! When the user runs this app, the menu will be displayed
        """

        ControllerManager().run()

main = MainClass()

main.main()
