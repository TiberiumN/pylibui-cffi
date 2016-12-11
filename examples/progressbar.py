"""
 Shows a simple progress bar.

"""

from pylibui.core import App
from pylibui.controls import Window, ProgressBar


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


app = App()

window = MyWindow('Progress bar example')
window.margined = True

progressbar = ProgressBar()
progressbar.value = 60
window.set_child(progressbar)

window.show()

app.start()
app.close()
