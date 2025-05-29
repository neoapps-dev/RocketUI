class State:
    def __init__(self, value):
        self._value = value
        self._listeners = []

    @property
    def value(self):
        return self._value

    def set(self, new_value):
        self._value = new_value
        for listener in self._listeners:
            listener()

    def bind(self, callback):
        self._listeners.append(callback)

