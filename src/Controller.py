import sys
from PySide.QtGui import *

__author__ = 'Michael Weinberger'
__date__ = 20150112
__version__ = 0.1


class Controller(QWidget):

    """
        Initialisiert Programm
    """
    def __init__(self, parent=None):

        super().__init__(parent)

        self.Dialog = View.Ui_Dialog()
        self.Dialog.setupUi(self)

        self.Dialog.read.clicked.connect(lambda: self.action())

    """
        CSV-Import Klassenaufruf
    """
    def action(self):

        print("Action!")

"""
    Starten des Programms
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Controller()
    main_window.show()
    sys.exit(app.exec_())
