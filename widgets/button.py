from PySide6.QtWidgets import QPushButton

class Button:
    def __init__(self, text, on_click=None):
        self.text = text
        self.on_click = on_click

    def render(self):
        btn = QPushButton(self.text)
        if self.on_click:
            btn.clicked.connect(self.on_click)
        return btn

