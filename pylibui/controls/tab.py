"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Tab(Control):
    def __init__(self):
        """
        Creates a new tab.
        """
        super().__init__()
        self.control = libui.uiNewTab()

    def append(self, name, control):
        """
        Appends a control to the tab.

        :param name: str
        :param control: uiControl
        :return: None
        """
        libui.uiTabAppend(self.control, name, control.pointer())

    def insert_at(self, name, before, control):
        """
        Inserts a control to the tab.

        :param name: str
        :param before: int
        :param control: uiControl
        :return: None
        """
        libui.uiTabInsertAt(self.control, name, before, control.pointer())

    def delete(self, index):
        """
        Deletes a control from the tab.

        :param tab: uiTab
        :param index: int
        :return: None
        """
        libui.uiTabDelete(self.control, index)

    def get_margined(self, page):
        """
        Returns whether the tab's page is margined or not.

        :param page: int
        :return: bool
        """
        return bool(libui.uiTabMargined(self.control, page))

    def set_margined(self, page, margined):
        """
        Sets whether the tab's page is margined or not.

        :param page: int
        :param margined: bool
        :return: None
        """
        libui.uiTabSetMargined(self.control, page, int(margined))

    def get_pages_num(self):
        """
        Returns the number of pages in the tab.

        :return: int
        """
        return libui.uiTabNumPages(self.control)
