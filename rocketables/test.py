from rocketui.state import State
from rocketui.widgets.text import Text
from rocketui.widgets.button import Button
from rocketui.widgets.column import Column
from rocketui.enums import TextSize
from rocketui.rocketable import Rocketable

class Test(Rocketable):
    def rocketize(self):
        self.counter = State(0)
        self.label = Text(lambda: f"Counter: {self.counter.value}", size=TextSize.Medium)
        self.counter.bind(self.label.update)
        return Column(lambda: [
            self.label,
            Button("Increase", on_click=self.increment)
        ])

    def increment(self):
        self.counter.set(self.counter.value + 1)

