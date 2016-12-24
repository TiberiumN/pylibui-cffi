"""
 Shows a simple radio buttons.

"""

from pylibui.core import App
from pylibui.controls import Window, RadioButtons, VerticalBox


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


class MyRadioButtons(RadioButtons):
    def on_select(self, data):
        print(self.selected)


app = App()

window = MyWindow('Window', 153, 94)
window.margined = True

colors = ['Blue', 'Yellow', 'Green', 'Red']
radio_buttons = MyRadioButtons(colors)
radio_buttons.append('Pink')
radio_buttons.selected = 1

vbox = VerticalBox()
vbox.padded = True
vbox.append(radio_buttons)
window.set_child(vbox)

window.show()

app.start()
app.close()
