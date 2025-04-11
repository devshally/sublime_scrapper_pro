import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QTabWidget
from auth.license_manager import Licensor
from gui.splash_screen import SplashScreen
from gui.license_window import LicenseWindow

class MainWindow(QMainWindow):
    main_window = None
    license_window = None
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sublime Scrapper Pro")
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        self.setFixedSize(1024, 768)

        tabs = QTabWidget()
        tabs.setStyleSheet("QTabBar::tab { padding: 10px; }")
        tabs.addTab(self._home_tab(), "Home")
        tabs.addTab(self._jobs_tab(), "Jobs")
        tabs.addTab(self._logs_tab(), "Logs")
        tabs.addTab(self._settings_tab(), "Settings")
        self.setCentralWidget(tabs)

    def _home_tab(self):
        w = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to Sublime Scrapper Pro"))
        w.setLayout(layout)
        return w

    def _jobs_tab(self):
        w = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Job management coming soon."))
        w.setLayout(layout)
        return w

    def _logs_tab(self):
        w = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Log view and filters."))
        w.setLayout(layout)
        return w

    def _settings_tab(self):
        w = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Settings UI coming soon."))
        w.setLayout(layout)
        return w
    
main_window = None
license_window = None

def launch_app():
    global main_window, license_window

    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()

    def on_splash_done():
        splash.close()

        if Licensor().check_license():
            print("✅ License valid, launching main window.")
            main_window = MainWindow()
            main_window.show()
        else:
            print("🔐 License invalid, showing license window.")
            license_window = LicenseWindow()

            def on_validated():
                global main_window
                main_window = MainWindow()
                main_window.show()

            license_window.validated.connect(on_validated)
            license_window.show()

    splash.done.connect(on_splash_done)

    sys.exit(app.exec())
