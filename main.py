import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from calki import Ui_MainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = Ui_MainWindow()
        self.ui1.setupUi(self)
        self.ui1.guzik.clicked.connect(self.liczenie)

    def liczenie(self):
        p = int(self.ui1.lineEditPoczatek.text())
        q = int(self.ui1.lineEditKoniec.text())
        n = int(self.ui1.lineEditIle.text())
        podstawaProstokata = (q-p)/n
        poleCale = 0
        for i in range(n):
            wysokosc = abs(self.funkcja(p + (podstawaProstokata * i) - (podstawaProstokata/2)))
            poleProstokata = wysokosc * podstawaProstokata
            poleCale += poleProstokata
        self.ui1.labelResult.setText("Pole = " + str(poleCale))

    def funkcja(self, x):
        return pow(x,3) -4*(pow(x, 2)) + x + 3

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())