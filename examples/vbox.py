"""
 Shows a window with a vertical box and some labels.

"""

from pylibui.core import App
from pylibui.controls import Window, Label, VerticalBox, Button


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


class MyButton(Button):
    def on_click(self, data):
        vbox.delete(0)
        self.enabled = False


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True

delete = MyButton("Delete 'Hello World!'")

vbox = VerticalBox()
vbox.padded = True
window.set_child(vbox)

vbox.append(Label('Hello World!'))
vbox.append(Label('Goodbye World!'))
vbox.append(delete)

window.show()

app.start()
app.close()
