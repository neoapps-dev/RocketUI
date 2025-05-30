# 🚀 RocketUI

**RocketUI** is a minimalistic, declarative UI framework designed for building reactive Python apps with a clean and intuitive API. based on Qt6

## ✨ Features

* 📦 Component(Rocketable)-based architecture
* 🔄 Reactive state management
* 🧱 Built-in widgets (Text, Button, TextInput, etc.)
* 🧪 Custom components via `Rocketables`
* 💡 Simple and readable syntax
* 🔥 Support for PySide6 Qt widgets

## 📦 Installation

1. From `pip`:
```bash
pip install rocketui  # coming soon, currently use github
```

2. From GitHub:
```bash
git clone https://github.com/neoapps-dev/rocketui.git
# do the command in your project root/src directory and use it
```


## 🚀 Quick Start

Here's a simple example to get you started:

```python
from rocketui.core import App
from rocketui.widgets.column import Column
from rocketui.widgets.text import Text
from rocketui.widgets.button import Button
from rocketui.widgets.textinput import TextInput
from rocketui.enums import TextSize
from rocketui.state import State

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
```

## 🧪 Rocketables

RocketUI includes support for custom components ("Rocketables"), here's an example one attached with RocketUI:

```python
from rocketui.rocketables.test import Test

class MyApp:
    def rocketize(self):
        return Column(content=lambda: [
            Test().rocketize()  # rocketize the rocketable Test
        ]
    )
```

And here is the `Test` Rocketable code:

```python
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
```

## 📚 Documentation

(WIP. undocumented but still shows API. gonna be hosted in the future)
1. Clone the repo and `cd` into it.
2. Run the command: `chmod +x generate-docs.sh && ./generate-docs.sh`
3. Run the command: `python3 -m http.server 8000 -d docs`
4. Visit the documentation at `http://localhost:8000`

## 🤝 Contributing

We welcome contributions! Feel free to fork the repo and submit a pull request.

## 📜 License

GPLv3
