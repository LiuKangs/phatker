


import sys

from GUI import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.logic()
        

        self.show()

    


if __name__ == "__main__":



    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())