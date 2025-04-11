import sys
from PySide6.QtWidgets import QApplication
from gui.splash_screen import SplashScreen
from gui.license_window import LicenseWindow
from gui.main_window import MainWindow

app = QApplication(sys.argv)

splash = SplashScreen()
license_window = LicenseWindow()
main_window = MainWindow()

def on_splash_done():
    splash.close()
    license_window.show()

def on_license_validated():
    license_window.close()
    main_window.show()

splash.done.connect(on_splash_done)
license_window.validated.connect(on_license_validated)

splash.show()
sys.exit(app.exec())
