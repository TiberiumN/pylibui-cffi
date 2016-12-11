"""
 Shows an empty window.

"""

from pylibui.core import App
from pylibui.controls import Window


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True
window.show()

app.start()
app.close()
