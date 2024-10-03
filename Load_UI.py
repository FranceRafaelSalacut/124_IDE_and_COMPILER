from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.uic import loadUi
from tkinter import *
from tkinter import filedialog
import sys


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("temp.ui", self)
        self.Code = "Empty"
        self.Current_File: str = ""

        # button clicks
        self.New_File_Button.clicked.connect(self.New_File)
        self.Open_File_Button.clicked.connect(self.Open_File)
        self.Compile_Button.clicked.connect(self.Compile)
        self.Execute_Button.clicked.connect(self.Execute)
        self.Save_Button.clicked.connect(self.Save)
        self.Save_As_Button.clicked.connect(self.Save_As)

        # button shortcuts
        New_File_Shortcut = QShortcut(QKeySequence("Ctrl+N"), self)
        Open_File_Shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        Save_Shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        Save_As_Shortcut = QShortcut(QKeySequence("Ctrl+Shift+S"), self)

        New_File_Shortcut.activated.connect(self.New_File)
        Open_File_Shortcut.activated.connect(self.Open_File)
        Save_Shortcut.activated.connect(self.Save)
        Save_As_Shortcut.activated.connect(self.Save_As)

    def New_File(self):
        print("Will open a new file in the Dialog Box")

    def Open_File(self):
        file = filedialog.askopenfile()
        if(file):
            self.Current_File = file.name
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
    
    def Save(self):
        if(self.Current_File):
            file = open(self.Current_File, "w")
            if(file):
                text = self.Code_Area.toPlainText()
                file.write(text)
                file.close()
        else:
            self.Save_As()
        
    
    def Save_As(self):
        text = self.Code_Area.toPlainText()
        file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text", ".txt"),
                                        ("All files", ".*")
                                        ])
        if(file):
            file.write(text)
            file.close()
            self.Current_File = file.name



def main():
    app = QApplication (sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()


if __name__ == "__main__":
    main()