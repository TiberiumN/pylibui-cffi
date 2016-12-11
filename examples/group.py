"""
 Shows a simple group.

"""

from pylibui.core import App
from pylibui.controls import Window, Group, Button


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True

button = Button('My Label')
group = Group('my Group')
group.margined = True
group.set_child(button)
window.set_child(group)

window.show()

app.start()
app.close()
