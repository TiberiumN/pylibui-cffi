"""
 Shows a simple spinbox.

"""

from pylibui.core import App
from pylibui.controls import Window, Spinbox


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True

spinbox = Spinbox(0, 100)
window.set_child(spinbox)

window.show()

app.start()
app.close()
