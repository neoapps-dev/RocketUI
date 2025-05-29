from PyQt6.QtWidgets import QApplication, QWidget
import sys
import importlib
import inspect

class App:
    def __init__(self, content):
        self.content_fn = content

    def rocketize(self):
        app = QApplication(sys.argv)
        ui_widget = self.content_fn().rocketize().render()
        ui_widget.setWindowTitle("RocketUI")
        ui_widget.resize(400, 300)
        ui_widget.show()
        sys.exit(app.exec())
