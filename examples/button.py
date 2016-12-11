"""
 Shows a simple button.

"""

from pylibui.core import App
from pylibui.controls import Window, Button


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


class MyButton(Button):
    def on_click(self, data):
        if self.text == 'click me':
            self.text = 'click me again'
        else:
            self.text = 'click me'


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True

button = MyButton('click me')
window.set_child(button)

window.show()

app.start()
app.close()
