"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Checkbox(Control):
    def __init__(self, text):
        """
        Creates a new checkbox.

        """
        super().__init__()
        self.control = libui.uiNewCheckbox(text)

        def handler(window, data):
            self.on_toggle(data)

        self.toggledHandler = libui.uiCheckboxOnToggled(self.control, handler,
                                                        None)

    @property
    def text(self):
        """
        Returns the text of the checkbox.

        :return: string
        """
        return libui.uiCheckboxText(self.control)

    @text.setter
    def text(self, text):
        """
        Sets the text of the checkbox.

        :param text: the text of the checkbox
        :return: None
        """
        libui.uiCheckboxSetText(self.control, text)

    @property
    def checked(self):
        """
        Gets whether the checkbox is checked or not.

        :return: bool
        """
        return bool(libui.uiCheckboxChecked(self.control))

    @checked.setter
    def checked(self, checked):
        """
        Sets whether the checkbox is checked or not.

        :param checked: bool
        :return: None
        """
        libui.uiCheckboxSetChecked(self.control, int(checked))

    def on_toggle(self, data):
        """
        Executes when the checkbox is toggled.

        :param data: data
        :return: None
        """
        pass
