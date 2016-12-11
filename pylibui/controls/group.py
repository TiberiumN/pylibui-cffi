"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Group(Control):
    def __init__(self, title):
        """
        Creates a new group.

        :param title: string
        """
        super().__init__()
        self.control = libui.uiNewGroup(title)

    @property
    def title(self):
        """
        Returns the title of the group.

        :return: string
        """
        return libui.uiGroupTitle(self.control)

    @title.setter
    def title(self, title):
        """
        Sets the title of the group.

        :param title: string
        :return: None
        """
        libui.uiGroupSetTitle(self.control, title)

    def set_child(self, child):
        """
        Sets a control as child of the group.

        :param child: control
        :return: None
        """
        libui.uiGroupSetChild(self.control, child.pointer())

    @property
    def margined(self):
        """
        Returns whether the group is margined.

        :return: bool
        """
        return bool(libui.uiGroupMargined(self.control))

    @margined.setter
    def margined(self, margined):
        """
        Sets whether the group is margined.

        :param margined: bool
        :return: None
        """
        libui.uiGroupSetMargined(self.control, int(margined))
