from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Signal
from auth.license_manager import Licensor

class LicenseWindow(QWidget):
    validated = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("License Activation")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        self.licensor = Licensor()

        layout = QVBoxLayout()
        self.label = QLabel("Enter your license key:")
        self.input = QLineEdit()
        self.activate_btn = QPushButton("Activate")

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.activate_btn)
        self.setLayout(layout)

        self.activate_btn.clicked.connect(self._on_activate_clicked)

    def _on_activate_clicked(self):
        license_key = self.input.text().strip()
        if self.licensor.validate_license(license_key):
            self.licensor.encrypt_license_key(license_key)
            QMessageBox.information(self, "Success", "License validated.")
            self.validated.emit()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Invalid license key.")
