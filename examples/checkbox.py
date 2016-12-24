"""
 Shows a simple checkbox.

"""

from pylibui.core import App
from pylibui.controls import Window, Checkbox

class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()

class MyCheckbox(Checkbox):
    def on_toggle(self, data):
        print('checkbox toggled!')


app = App()

window = MyWindow('Checkbox example')
window.margined = True

checkbox = MyCheckbox('a checkbox!')
checkbox.text = 'a checkbox'
checkbox.checked = True
window.set_child(checkbox)

window.show()

app.start()
app.close()
