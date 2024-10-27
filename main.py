from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
import sys
import os

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("124-Brainrot-Language.ui", self)

class WelcomeDialog(QMainWindow):
    def __init__(self, main_ui):
        super(WelcomeDialog, self).__init__()

        # Reference to the MainUI window
        self.main_ui = main_ui

        # Configure the WelcomeDialog video window
        # self.resize(500, 500)
        # self.resize(1920, 1080)
        original_width = 1920
        original_height = 1080
        scale_factor = 0.4  # Adjust this to make it larger or smaller

        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        self.resize(new_width, new_height)

        video_widget = QVideoWidget()
        self.setCentralWidget(video_widget)
        self.player = QMediaPlayer(self, QMediaPlayer.VideoSurface)
        self.player.setVideoOutput(video_widget)
        
        # Set video file path
        path = "welcome-video.avi"
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))

        # Set the dialog to be always on top and modal
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # Connect signals
        self.player.mediaStatusChanged.connect(self.on_media_status_changed)
        
        # Play video
        self.player.play()

    def on_media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.close()  # Close the video dialog when the video ends

    def closeEvent(self, event):
        # Close the video dialog and allow access to MainUI
        self.main_ui.activateWindow()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Show MainUI in the background
    main_window = MainUI()
    main_window.show()

    # Show WelcomeDialog in front of MainUI
    welcome_dialog = WelcomeDialog(main_window)
    welcome_dialog.show()

    sys.exit(app.exec_())



# from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QVBoxLayout, QFrame
# from PyQt5.uic import loadUi
# from PyQt5.QtCore import QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtCore import QUrl
# import sys
# import os

# class MainUI(QMainWindow):
#     def __init__(self):
#         super(MainUI, self).__init__()
#         loadUi("124-Brainrot-Language.ui", self)


# class WelcomeDialog(QMainWindow):
#     def __init__(self):
#         super(WelcomeDialog, self).__init__()
        
#         self.resize(500, 500)
#         video_widget = QVideoWidget()       
#         self.setCentralWidget(video_widget)
#         self.player = QMediaPlayer(self, QMediaPlayer.VideoSurface)
#         self.player.setVideoOutput(video_widget)
#         self.player.stop()
#         path = "welcome-video.avi"
#         self.player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
#         self.player.play()
#         self.player.mediaStatusChanged.connect(self.on_media_status_changed)

#     def on_media_status_changed(self, status):
#         if status == QMediaPlayer.EndOfMedia:
#             self.close()
#             self.MainUI = MainUI()
#             self.MainUI.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = WelcomeDialog()
#     window.show()
#     sys.exit(app.exec_())

