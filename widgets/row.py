from PySide6.QtWidgets import QWidget, QHBoxLayout

class Row:
    def __init__(self, content):
        self.content_fn = content
        self.container = QWidget()
        self.layout = QHBoxLayout()

    def render(self):
        children = self.content_fn()
        if not isinstance(children, (list, tuple)):
            children = [children]

        for child in children:
            try:
                widget = child.render()
            except Exception as e:
                widget = child
            self.layout.addWidget(widget)
            if hasattr(child, "update"):
                self.layout.setStretchFactor(widget, 0)
                child.update_widget = widget

        self.container.setLayout(self.layout)
        return self.container

