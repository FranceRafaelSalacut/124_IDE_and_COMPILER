from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from tkinter import *
from tkinter import filedialog
import sys


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("temp.ui", self)
        self.Code = "Empty"

        self.New_File_Button.clicked.connect(self.New_File)
        self.Open_File_Button.clicked.connect(self.Open_File)
        self.Compile_Button.clicked.connect(self.Compile)
        self.Execute_Button.clicked.connect(self.Execute)


    def New_File(self):
        print("Will open a new file in the Dialog Box")

    def Open_File(self):
        file = filedialog.askopenfile()
        if(file):
            Txt = ""
            for line in file:
                Txt = Txt + line
                
            print(Txt)   
            self.Code_Area.setPlainText(Txt)

    def Compile(self):
        self.Code =  self.Code_Area.toPlainText()
        print(self.Code)

    def Execute(self):
        print(self.Code)


def main():
    app = QApplication (sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()


if __name__ == "__main__":
    main()