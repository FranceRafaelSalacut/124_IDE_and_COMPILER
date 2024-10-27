from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut, QMessageBox, QVBoxLayout, QWidget
from PyQt5.QtGui import QKeySequence
from PyQt5.uic import loadUi
from tkinter import *
from tkinter import filedialog
import sys

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('124-Brainrot-Language.ui', self)
        
        # disable certain buttons at start
        self.Enable_Buttons = True
        self.ToggleButtons()

        self.Code = "Empty"
        self.Current_File: str = ""

        # check text changes
        self.Code_Area.textChanged.connect(self.Text_Change)
        
        # check if file saved
        self.Is_Saved = True
        self.Unsaved_Label = " (Unsaved changes)"

        # editor states
        self.Code_Area.setReadOnly(True)
        self.CurrentFileName.setReadOnly(True)

        # placeholders
        self.Code_Area.setText("Create or open a file to get started")
        self.CurrentFileName.setText("Welcome")

        # button clicks and tool tips
        self.CurrentFileName.setReadOnly(True)

        # placeholders
        self.Code_Area.setText("Create or open a file to get started")
        self.CurrentFileName.setText("Welcome")

        # button clicks and tool tips
        self.New_File_Button.clicked.connect(self.New_File)
        self.New_File_Button.setToolTip("Create New File")

        self.Open_File_Button.clicked.connect(self.Open_File)
        self.Open_File_Button.setToolTip("Open New File")

        self.Close_File_Button.clicked.connect(self.Close_File)
        self.Close_File_Button.setToolTip("Close File")

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
        Close_File_ShortCut = QShortcut(QKeySequence("Ctrl+K"), self)

        Undo = QShortcut(QKeySequence("Ctrl+Q"), self)
        Redo = QShortcut(QKeySequence("Ctrl+W"), self)
        Copy = QShortcut(QKeySequence("Ctrl+E"), self)
        Cut = QShortcut(QKeySequence("Ctrl+R"), self)
        Paste = QShortcut(QKeySequence("Ctrl+T"), self)

        New_File_Shortcut.activated.connect(self.New_File)
        Open_File_Shortcut.activated.connect(self.Open_File)
        Save_Shortcut.activated.connect(self.Save)
        Save_As_Shortcut.activated.connect(self.Save_As)
        Close_File_ShortCut.activated.connect(self.Close_File)

        Undo.activated.connect(self.Undo)
        Redo.activated.connect(self.Redo)
        Copy.activated.connect(self.Copy)
        Cut.activated.connect(self.Cut)
        Paste.activated.connect(self.Paste)

    def ToggleButtons(self):
        self.Enable_Buttons = not self.Enable_Buttons
        
        self.Compile_Button.setEnabled(self.Enable_Buttons)
        self.Execute_Button.setEnabled(self.Enable_Buttons)
        self.Close_File_Button.setEnabled(self.Enable_Buttons)
        self.Save_Button.setEnabled(self.Enable_Buttons)
        self.Save_As_Button.setEnabled(self.Enable_Buttons)
        self.Undo_Button.setEnabled(self.Enable_Buttons)
        self.Redo_Button.setEnabled(self.Enable_Buttons)
        self.Copy_Button.setEnabled(self.Enable_Buttons)
        self.Cut_Button.setEnabled(self.Enable_Buttons)
        self.Paste_Button.setEnabled(self.Enable_Buttons)

    def SetActiveEditor(self, fileName: str = "Untitled"):
        self.Code_Area.setReadOnly(False)
        self.Code_Area.setText("")
        self.CurrentFileName.setReadOnly(False)
        self.CurrentFileName.setText(fileName + self.Unsaved_Label)

    def Text_Change(self):
        if self.Code_Area.isReadOnly():
            return

        if self.Is_Saved:
            prompt: str = self.CurrentFileName.text() + self.Unsaved_Label
            self.CurrentFileName.setText(prompt)
            self.Is_Saved = False

    def New_File(self):
        if not self.Prompt_Save_Changes():
            return
        print("Will open a new file in the Dialog Box")
        self.Current_File = ""
        self.SetActiveEditor()
        if not self.Enable_Buttons:
            self.ToggleButtons()

    def Open_File(self):
        if not self.Prompt_Save_Changes():
            return
        file = filedialog.askopenfile()
        if(file):
            self.Current_File = file.name
            self.SetActiveEditor()
            Txt = ""
            for line in file:
                Txt = Txt + line
                
            print(Txt)   
            self.Code_Area.setPlainText(Txt)
            self.CurrentFileName.setText(file.name.split('/')[-1])
            self.Is_Saved = True
            
            if not self.Enable_Buttons:
                self.ToggleButtons()

    def Close_File(self):
        if not self.Prompt_Save_Changes():
            return
        self.Code_Area.setReadOnly(True)
        self.CurrentFileName.setReadOnly(True)
        self.Current_File = ""
        self.Code_Area.setText("Create or open a file to get started")
        self.CurrentFileName.setText("Welcome")
        self.ToggleButtons()
        self.Is_Saved = True

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
                self.Is_Saved = True
                currentFileName: str = self.Current_File.split('/')[-1]
                self.CurrentFileName.setText(currentFileName)
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
            currentFileName = file.name.split('/')[-1]
            currentFileName: str = self.Current_File.split('/')[-1]
            self.CurrentFileName.setText(currentFileName)
            self.Is_Saved = True

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

    def closeEvent(self, event):
        # Prompt to save changes when closing the application.
        if self.Prompt_Save_Changes():
            event.accept()  # Close the window
        else:
            event.ignore()  # Cancel the close

    def Prompt_Save_Changes(self):
        if not self.Is_Saved:
            reply = QMessageBox.question(
                self, "Unsaved Changes",
                "You have unsaved changes. Would you like to save them?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            if reply == QMessageBox.Yes:
                self.Save()
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