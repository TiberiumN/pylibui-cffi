"""
 Shows a simple tab with two pages, one margined, one not margined.

"""

from pylibui.core import App
from pylibui.controls import Window, Tab, HorizontalBox, Label


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


app = App()

window = MyWindow('Window', 400, 300)
window.margined = True

tab = Tab()

tabPage1 = HorizontalBox()
tabPage2 = HorizontalBox()

labelPage1 = Label("Page 1, margined")
labelPage2 = Label("Page 2, not margined")

tabPage1.append(labelPage1)
tabPage2.append(labelPage2)

tab.append("Page 1", tabPage1)
tab.set_margined(0, True)

tab.append("Page 2", tabPage2)
tab.set_margined(1, False)

print("Number of pages: " + str(tab.get_pages_num()))

window.set_child(tab)

window.show()

app.start()
app.close()
