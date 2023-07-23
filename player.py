import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QSlider
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QTimer

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initMediaPlayer()

    def initUI(self):
        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 400, 200)

        self.play_button = QPushButton("Play", self)
        self.play_button.setGeometry(50, 150, 75, 30)
        self.play_button.clicked.connect(self.play_music)

        self.pause_button = QPushButton("Pause", self)
        self.pause_button.setGeometry(150, 150, 75, 30)
        self.pause_button.clicked.connect(self.pause_music)

        self.forward_button = QPushButton("Forward", self)
        self.forward_button.setGeometry(250, 150, 75, 30)
        self.forward_button.clicked.connect(self.forward_music)

        self.rewind_button = QPushButton("Rewind", self)
        self.rewind_button.setGeometry(350, 150, 75, 30)
        self.rewind_button.clicked.connect(self.rewind_music)

        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setGeometry(50, 100, 375, 30)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.set_volume)

        # Create a separate slider to display the current position
        self.position_slider = QSlider(Qt.Horizontal, self)
        self.position_slider.setGeometry(50, 50, 375, 30)
        self.position_slider.setValue(0)
        self.position_slider.setEnabled(False)

        # Create a QTimer to update the position slider every 100 milliseconds
        self.slider_timer = QTimer(self)
        self.slider_timer.timeout.connect(self.update_position_slider)
        self.slider_timer.start(100)

    def initMediaPlayer(self):
        self.media_player = QMediaPlayer(self)
        self.media_player.positionChanged.connect(self.update_position)
        self.media_player.durationChanged.connect(self.update_duration)

    def play_music(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open MP3 File", "", "MP3 Files (*.mp3);;All Files (*)")
        if file_name:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.media_player.play()

    def pause_music(self):
        self.media_player.pause()

    def forward_music(self):
        self.media_player.setPosition(self.media_player.position() + 5000)  # Forward 5 seconds

    def rewind_music(self):
        self.media_player.setPosition(self.media_player.position() - 5000)  # Rewind 5 seconds

    def set_volume(self, value):
        self.media_player.setVolume(value)

    def update_position_slider(self):
        # Update the position slider with the current position of the media player
        position = self.media_player.position()
        self.position_slider.setValue(position)

    def update_position(self, position):
        self.position_slider.setValue(position)

    def update_duration(self, duration):
        self.position_slider.setMaximum(duration)

app = QApplication(sys.argv)
player = MusicPlayer()
player.show()
sys.exit(app.exec_())
