import sys
from PySide.QtGui import *
from src.CSVimport import *
from src.View import *

__author__ = 'Michael Weinberger'
__date__ = 20150112
__version__ = 0.1


class Controller(QWidget):

    """
        Initialisiert Programm
    """
    def __init__(self, parent=None):

        super().__init__(parent)

        self.Dialog = Ui_Form()
        self.Dialog.setupUi(self)

        self.Dialog.read.clicked.connect(lambda: self.action())

    """
        Klassenaufruf CSV-Import
    """
    def action(self):

        do = CSVimport("SalesJan2009.csv")
        out = do.readcsv()

        tmp = ""
        for row in out:
            tmp += str(row)
            tmp += "<br><br>"

        tmp += "Total rows: " + str(len(out))
        self.Dialog.out.setText(tmp)

"""
    Starten des Programms
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Controller()
    main_window.show()
    sys.exit(app.exec_())
