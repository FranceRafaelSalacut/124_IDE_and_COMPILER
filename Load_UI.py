from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut, QMessageBox
from PyQt5.QtGui import QKeySequence
from PyQt5.uic import loadUi
from tkinter import *
from tkinter import filedialog
import sys

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('124-Brainrot-Language.ui', self)
        
        self.Code = "Empty"
        self.Current_File: str = ""

        # check text changes
        self.Modified = False
        self.Code_Area.textChanged.connect(self.Text_Change)
        
        # check if file saved
        self.Unsaved_Label = " (unsaved)"
        self.Is_Saved = True

        # editor states
        self.Code_Area.setReadOnly(True)
        self.CurrentFileName.setReadOnly(True)

        # placeholders
        self.Code_Area.setText("Create or open a file to get started")
        self.CurrentFileName.setText("Welcome")

        # button clicks and tool tips
        self.New_File_Button.clicked.connect(self.New_File)
        self.New_File_Button.setToolTip("Create New File")

        self.Open_File_Button.clicked.connect(self.Open_File)
        self.Open_File_Button.setToolTip("Open New File")

        self.Compile_Button.clicked.connect(self.Compile)
        self.Compile_Button.setToolTip("Compile Program")

        self.Execute_Button.clicked.connect(self.Execute)
        self.Execute_Button.setToolTip("Compile and Execute Program")

        self.Save_Button.clicked.connect(self.Save)
        self.Save_Button.setToolTip("Save Current File")

        self.Save_As_Button.clicked.connect(self.Save_As)
        self.Save_As_Button.setToolTip("Save File As")

        self.Undo_Button.clicked.connect(self.Undo)
        self.Undo_Button.setToolTip("Undo")

        self.Redo_Button.clicked.connect(self.Redo)
        self.Redo_Button.setToolTip("Redo")

        self.Copy_Button.clicked.connect(self.Copy)
        self.Copy_Button.setToolTip("Copy")

        self.Cut_Button.clicked.connect(self.Cut)
        self.Cut_Button.setToolTip("Cut")

        self.Paste_Button.clicked.connect(self.Paste)
        self.Paste_Button.setToolTip("Paste")
        
        # button shortcuts
        New_File_Shortcut = QShortcut(QKeySequence("Ctrl+N"), self)
        Open_File_Shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        Save_Shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        Save_As_Shortcut = QShortcut(QKeySequence("Ctrl+Shift+S"), self)

        Undo = QShortcut(QKeySequence("Ctrl+Q"), self)
        Redo = QShortcut(QKeySequence("Ctrl+W"), self)
        Copy = QShortcut(QKeySequence("Ctrl+E"), self)
        Cut = QShortcut(QKeySequence("Ctrl+R"), self)
        Paste = QShortcut(QKeySequence("Ctrl+T"), self)

        New_File_Shortcut.activated.connect(self.New_File)
        Open_File_Shortcut.activated.connect(self.Open_File)
        Save_Shortcut.activated.connect(self.Save)
        Save_As_Shortcut.activated.connect(self.Save_As)

        Undo.activated.connect(self.Undo)
        Redo.activated.connect(self.Redo)
        Copy.activated.connect(self.Copy)
        Cut.activated.connect(self.Cut)
        Paste.activated.connect(self.Paste)

    def SetActiveEditor(self, fileName: str = "Untitled"):
        self.Code_Area.setReadOnly(False)
        self.Code_Area.setText("")
        self.CurrentFileName.setReadOnly(False)
        self.CurrentFileName.setText(fileName)

    def Text_Change(self):
        if self.Code_Area.isReadOnly():
            return
        self.Modified = True

        # if self.Is_Saved:
        #     self.CurrentFileName.setText("Unsaved changes")
        #     self.Is_Saved = False

    def New_File(self):
        if not self.Prompt_Save_Changes():
            return
        print("Will open a new file in the Dialog Box")
        self.Current_File = ""
        self.SetActiveEditor()

    def Open_File(self):
        if not self.Prompt_Save_Changes():
            return
        file = filedialog.askopenfile()
        if(file):
            self.Current_File = file.name
            self.SetActiveEditor(file.name.split('/')[-1])
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
                                            ]
                                        )
        if(file):
            file.write(text)
            file.close()
            self.Current_File = file.name
            self.CurrentFileName = file.name.split('/')[-1]

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

    def Prompt_Save_Changes(self):
        if self.Modified:
            reply = QMessageBox.question(
                self, "Unsaved Changes",
                "You have unsaved changes. Would you like to save them?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            if reply == QMessageBox.Yes:
                self.save_file()
                return True  # Proceed with the action
            elif reply == QMessageBox.No:
                return True  # Proceed without saving
            else:
                return False  # Cancel the action
        return True  # No unsaved changes, proceed

    def closeEvent(self, event):
        # Prompt to save changes when closing the application.
        if self.Prompt_Save_Changes():
            event.accept()  # Close the window
        else:
            event.ignore()  # Cancel the close

def main():
    app = QApplication (sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()


if __name__ == "__main__":
    main()