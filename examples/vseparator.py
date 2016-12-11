"""
 Shows a simple vertical separator.

"""

from pylibui.core import App
from pylibui.controls import Window, VerticalSeparator


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True

separator = VerticalSeparator()
window.set_child(separator)

window.show()

app.start()
app.close()
