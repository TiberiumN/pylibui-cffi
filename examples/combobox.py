"""
 Shows a simple combobox.

"""

from pylibui.core import App
from pylibui.controls import Window, Combobox


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


class MyCombobox(Combobox):
    def on_selected(self, data):
        print(self.selected)


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True

colors = ['Blue', 'Yellow', 'Green', 'Red']
combobox = MyCombobox(colors)
combobox.append('Pink')
combobox.selected = 3

window.set_child(combobox)

window.show()

app.start()
app.close()
