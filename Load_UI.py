from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut, QUndoStack
from PyQt5.QtGui import QKeySequence, QGuiApplication
from PyQt5.uic import loadUi
from tkinter import *
from tkinter import filedialog
import sys


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("temp.ui", self)
        self.Code = "Empty"
        self.UndoStack = QUndoStack(self)
        self.ClipBoard = QGuiApplication.clipboard()

        self.Code_Area.setReadOnly(True)
        self.New_File_Button.clicked.connect(self.New_File)
        self.New_File_Button.setToolTip("Create New File")

        self.Open_File_Button.clicked.connect(self.Open_File)
        self.Open_File_Button.setToolTip("Oper New File")

        self.Compile_Button.clicked.connect(self.Compile)
        self.Compile_Button.setToolTip("Compile Program")

        self.Execute_Button.clicked.connect(self.Execute)
        self.Execute_Button.setToolTip("Compile and Execute Program")

        Undo = QShortcut(QKeySequence("Ctrl+Q"), self)
        Redo = QShortcut(QKeySequence("Ctrl+W"), self)
        Copy = QShortcut(QKeySequence("Ctrl+C"), self)
        Paste = QShortcut(QKeySequence("Ctrl+V"), self)

        Undo.activated.connect(self.Undo)
        Redo.activated.connect(self.Redo)
        Copy.activated.connect(self.Copy)
        Paste.activated.connect(self.Paste)


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
        self.UndoStack.undo()

    def Redo(self):
        print("Redigit")
        self.UndoStack.redo()

    def Copy(self):
        self.ClipBoard.setMimeData()

    def Paste(self):
        self.ClipBoard.mimeData()

def main():
    app = QApplication (sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()


if __name__ == "__main__":
    main()