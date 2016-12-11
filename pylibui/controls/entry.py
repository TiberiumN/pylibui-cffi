"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class BaseEntry(Control):
    @property
    def text(self):
        """
        Returns the text of the entry.

        :return: string
        """
        return libui.uiEntryText(self.control)

    @text.setter
    def text(self, text):
        """
        Sets the text of the entry.

        :param text: string
        :return: None
        """
        libui.uiEntrySetText(self.control, text)

    @property
    def read_only(self):
        """
        Returns whether the entry is read only or not.

        :return: bool
        """
        return bool(libui.uiEntryReadOnly(self.control))

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets whether the entry is read only or not.

        :param read_only: bool
        :return: None
        """
        libui.uiEntrySetReadOnly(self.control, int(read_only))

    def on_changed(self, data):
        """
        Executes when the entry is changed.

        :param data: data
        :return: None
        """
        pass


class Entry(BaseEntry):
    def __init__(self):
        """
        Creates a new entry.

        """
        super().__init__()
        self.control = libui.uiNewEntry()

        def handler(window, data):
            self.on_changed(data)
            return None

        self.changedHandler = libui.uiEntryOnChanged(self.control, handler,
                                                     None)


class PasswordEntry(Entry):
    def __init__(self):
        """
        Creates a new password entry.

        """
        super().__init__()
        self.control = libui.uiNewPasswordEntry()

        def handler(window, data):
            self.on_changed(data)

        self.changedHandler = libui.uiEntryOnChanged(self.control, handler,
                                                     None)


class SearchEntry(Entry):
    def __init__(self):
        """
        Creates a new search entry.

        """
        super().__init__()
        self.control = libui.uiNewSearchEntry()

        def handler(window, data):
            self.on_changed(data)

        self.changedHandler = libui.uiEntryOnChanged(self.control, handler,
                                                     None)
