"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Slider(Control):
    def __init__(self, min_value, max_value):
        """
        Creates a new slider.

        :param min_value: int
        :param max_value: int
        """
        super().__init__()
        self.control = libui.uiNewSlider(min_value, max_value)

        def handler(window, data):
            self.on_change(data)

        self.changedHandler = libui.uiSliderOnChanged(self.control, handler,
                                                      None)

    @property
    def value(self):
        """
        Returns the value of the slider.

        :return: int
        """
        return libui.uiSliderValue(self.control)

    @value.setter
    def value(self, value):
        """
        Sets the value of the slider.

        :param value: int
        :return: None
        """
        libui.uiSliderSetValue(self.control, value)

    def on_change(self, data):
        """
        Executes when slider's value change.

        :param data: data
        :return: None
        """
        pass
