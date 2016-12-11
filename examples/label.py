"""
 Shows a simple label.

"""

from pylibui.core import App
from pylibui.controls import Window, Label


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True

label = Label("My Label")
window.set_child(label)

window.show()

app.start()
app.close()
