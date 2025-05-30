from PySide6.QtWidgets import QLabel
from rocketui.enums import TextSize

class Text:
    def __init__(self, content, size=TextSize.Medium):
        self.content = content
        self.size = size
        self.label = QLabel()

    def render(self):
        text_value = self.content() if callable(self.content) else self.content
        self.label.setText(text_value)
        self.label.setStyleSheet(f"font-size: {self.size.value}px;")
        return self.label

    def update(self):
        if callable(self.content):
            self.label.setText(self.content())

