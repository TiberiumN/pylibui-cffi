"""
 Shows a simple slider.

"""

from pylibui.core import App
from pylibui.controls import Window, Slider


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


class MySlider(Slider):
    def on_change(self, data):
        print(self.value)


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True

slider = MySlider(0, 100)
slider.value = 50
window.set_child(slider)

window.show()

app.start()
app.close()
