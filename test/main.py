from rocketui.core import App
from rocketui.widgets.column import Column
from rocketui.widgets.text import Text
from rocketui.widgets.button import Button
from rocketui.widgets.textinput import TextInput
from rocketui.enums import TextSize
from rocketui.state import State
from rocketui.rocketables.test import Test

class MyApp:
    def rocketize(self):
        self.result = State("")
        self.label = Text(lambda: f"{self.result.value}", size=TextSize.Big)
        self.input = TextInput("Eval...")
        self.result.bind(self.label.update)
        return Column(
            content=lambda: [
                self.label,
                self.input,
                Button("Eval", on_click=self.evalcode)
            ]
        )

    def evalcode(self):
        try:
            self.result.set(eval(self.input.get_value()))
        except Exception as e:
            self.result.set(e)

app = App(MyApp)
app.rocketize()
