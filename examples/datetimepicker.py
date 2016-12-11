"""
Shows a window with three date/time pickers.

"""

from pylibui.core import App
from pylibui.controls import (Window, VerticalBox, DateTimePicker, DatePicker,
                              TimePicker)


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True

vbox = VerticalBox()
vbox.padded = True
window.set_child(vbox)

vbox.append(DateTimePicker())
vbox.append(DatePicker())
vbox.append(TimePicker())

window.show()

app.start()
app.close()
