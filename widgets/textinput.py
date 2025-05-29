from PyQt6.QtWidgets import QLineEdit

class TextInput:
    def __init__(self, placeholder=""):
        self.placeholder = placeholder
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(self.placeholder)

    def render(self):
        return self.line_edit

    def update(self, text):
        self.line_edit.setText(text)

    def get_value(self):
        return self.line_edit.text()
