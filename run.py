# run.py

import sys
from PySide6.QtWidgets import QApplication
from gui.splash_screen import SplashScreen
from gui.license_window import LicenseWindow
from gui.main_window import MainWindow
from auth.license_manager import Licensor

class AppController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.splash = SplashScreen()
        self.license_window = None
        self.main_window = None

        self.splash.done.connect(self.on_splash_done)

    def on_splash_done(self):
        self.splash.close()
        licensor = Licensor()

        if licensor.check_license():
            print("✅ License valid, launching main window.")
            self.main_window = MainWindow()
            self.main_window.show()
        else:
            print("🔐 No valid license found, showing license window.")
            self.license_window = LicenseWindow()
            self.license_window.validated.connect(self.on_license_validated)
            self.license_window.show()

    def on_license_validated(self):
        self.license_window.close()
        self.main_window = MainWindow()
        self.main_window.show()

    def run(self):
        self.splash.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    controller = AppController()
    controller.run()
