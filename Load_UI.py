from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("temp.ui", self)

        self.New_File_Button.clicked.connect(self.Fclickhandler)
        self.Open_File_Button.clicked.connect(self.Oclickhandler)


    def Fclickhandler(self):
        print("NEW FILE")

    def Oclickhandler(self):
        print("OPEN FILE")


def main():
    app = QApplication (sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()


if __name__ == "__main__":
    main()