"""
 Shows three entries :
 - a simple entry
 - a password entry
 - a search entry

"""

from pylibui.core import App
from pylibui.controls import (Window, Entry, SearchEntry, PasswordEntry,
                              VerticalBox)


class MyWindow(Window):
    def on_close(self, data):
        super().on_close(data)
        app.stop()


class MyEntry(Entry):
    def on_changed(self, data):
        print('entry changed!')


app = App()

window = MyWindow('Entry example')
window.margined = True

entry = MyEntry()
search_entry = SearchEntry()
password_entry = PasswordEntry()

vbox = VerticalBox()
vbox.padded = True
vbox.append(entry)
vbox.append(search_entry)
vbox.append(password_entry)

window.set_child(vbox)
window.show()

app.start()
# app.close() # SEE https://github.com/joaoventura/pylibui/issues/18
