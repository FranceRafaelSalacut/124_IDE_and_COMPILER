from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QVBoxLayout, QFrame
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys
import os

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("124-Brainrot_Language.ui")

class WelcomeDialog(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('124-Brainrot_Language-Welcome.ui', self)  

        # Retrieve the QFrame by its object name
        self.video_frame = self.findChild(QFrame, 'videoframe')  # Use the actual object name

        # Create a QVideoWidget and set it as the child of the video frame
        self.video_widget = QVideoWidget(self.video_frame)
        layout = QVBoxLayout(self.video_frame)
        layout.addWidget(self.video_widget)

        # Create a media player
        self.media_player = QMediaPlayer(self)
        video_path = "/Users/christinebagazin/Downloads/124-folder/welcome-box-vid.mp4"  # Update this with your video path
        self.media_player.setMedia(QMediaContent(video_path))
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.play()

        # Set a timer to close the dialog automatically after 30 seconds
        QTimer.singleShot(30000, self.accept)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())