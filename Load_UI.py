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

        self.Code_Area.setReadOnly(True)
        self.New_File_Button.clicked.connect(self.New_File)
        self.New_File_Button.setToolTip("Create New File")

        self.Open_File_Button.clicked.connect(self.Open_File)
        self.Open_File_Button.setToolTip("Oper New File")

        self.Compile_Button.clicked.connect(self.Compile)
        self.Compile_Button.setToolTip("Compile Program")

        self.Execute_Button.clicked.connect(self.Execute)
        self.Execute_Button.setToolTip("Compile and Execute Program")

        # self.Code_Area.textChanged.connect(self.Text_Change)

        Undo = QShortcut(QKeySequence("Ctrl+Q"), self)
        Redo = QShortcut(QKeySequence("Ctrl+W"), self)
        Copy = QShortcut(QKeySequence("Ctrl+E"), self)
        Cut = QShortcut(QKeySequence("Ctrl+R"), self)
        Paste = QShortcut(QKeySequence("Ctrl+T"), self)

        Undo.activated.connect(self.Undo)
        Redo.activated.connect(self.Redo)
        Copy.activated.connect(self.Copy)
        Cut.activated.connect(self.Cut)
        Paste.activated.connect(self.Paste)

    def Text_Change(self):
        self.UndoStack.text(self.Code_Area.toPlainText())
        self.Compile()

    def New_File(self):
        print("Will open a new file in the Dialog Box")
        self.Code_Area.setReadOnly(False)

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

    def Undo(self):
        print("Undid")
        self.Code_Area.undo()

    def Redo(self):
        print("Redigit")
        self.Code_Area.redo()

    def Copy(self):
        print("Copycat")
        self.Code_Area.copy()

    def Cut(self):
        print("Aray")
        self.Code_Area.cut()

    def Paste(self):
        print("Glue")
        self.Code_Area.paste()

def main():
    app = QApplication (sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()


if __name__ == "__main__":
    main()