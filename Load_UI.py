from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("temp.ui", self)

        self.New_File_Button.clicked.connect(self.clickhandler)
        self.Open_File_Button.clicked.connect(self.clickhandler)


    def clickhandler(self):
        print("Testingignign")


def main():
    app = QApplication (sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()


if __name__ == "__main__":
    main()