from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QProgressBar
from PySide6.QtCore import Qt, QTimer, Signal

class SplashScreen(QWidget):
    done = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sublime Scrapper Pro - Loading")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        
        layout = QVBoxLayout()
        self.label = QLabel("Checking for updates...")
        self.label.setAlignment(Qt.AlignCenter)
        self.progress = QProgressBar()
        self.progress.setValue(0)
        layout.addWidget(self.label)
        layout.addWidget(self.progress)
        self.setLayout(layout)

        QTimer.singleShot(1000, self.check_for_updates)

    def check_for_updates(self):
        from updater.update import check_and_update
        self.label.setText("Updating if necessary...")
        self.progress.setValue(25)
        updated = check_and_update()
        self.progress.setValue(100)
        QTimer.singleShot(1500, self.done.emit)
