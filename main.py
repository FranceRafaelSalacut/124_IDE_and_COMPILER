from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QVBoxLayout, QFrame
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
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
    def __init__(self):
        super(WelcomeDialog, self).__init__()
        
        self.resize(500, 500)
        video_widget = QVideoWidget()       
        self.setCentralWidget(video_widget)
        self.player = QMediaPlayer(self, QMediaPlayer.VideoSurface)
        self.player.setVideoOutput(video_widget)
        self.player.stop()
        path = "pebertdey.wmv"
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.player.play()
        self.player.mediaStatusChanged.connect(self.on_media_status_changed)

    def on_media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeDialog()
    window.show()
    sys.exit(app.exec_())