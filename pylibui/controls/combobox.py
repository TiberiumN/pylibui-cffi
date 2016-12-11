"""
Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Combobox(Control):
    def __init__(self, items=None):
        """
        Creates a new combobox.

        """
        super().__init__()
        if items is None:
            items = []
        self.items = items
        self.control = libui.uiNewCombobox()

        for item in items:
            self.append(item)

        def on_selected(combobox, data):
            self.on_selected(data)

        self.selectedHandler = libui.uiComboboxOnSelected(
            self.control, on_selected, None)

    def append(self, text):
        """
        Appends a new item to the combobox.

        :param text: string
        :return: None
        """
        libui.uiComboboxAppend(self.control, text)

    @property
    def selected(self):
        """
        Returns index of the selected item.

        :return: int
        """
        return libui.uiComboboxSelected(self.control)

    @selected.setter
    def selected(self, n):
        """
        Sets selected item.

        :n: integer
        :return: None
        """
        libui.uiComboboxSetSelected(self.control, n)

    def on_selected(self, data):
        """
        Executes when an item in combobox selected.

        :param data: data
        :return: None
        """
        pass
