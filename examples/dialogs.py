"""
 Shows four dialogs:
 - an open file dialog
 - a save file dialog
 - a message dialog
 - an error dialog

"""

from pylibui.core import App
from pylibui.controls import Window, VerticalBox, Combobox


class MyWindow(Window):
    def onClose(self, data):
        super().on_close(data)
        app.stop()


class MyCombobox(Combobox):
    def on_selected(self, data):
        selected = self.selected
        if (selected == 0):
            print(window.open_file())
        elif (selected == 1):
            print(window.save_file())
        elif (selected == 2):
            window.show_message("Message", "Description")
        elif (selected == 3):
            window.show_error("Error", "Description")


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True

dialogs = MyCombobox([
    "Open",
    "Save",
    "Message",
    "Error"
])

vbox = VerticalBox()
vbox.append(dialogs)
window.set_child(vbox)

window.show()

app.start()
app.close()
