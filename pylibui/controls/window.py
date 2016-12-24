"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Window(Control):
    def __init__(self, title, width=800, height=600, menuBar=True):
        """
        Creates a new window.

        :param title: the title of the window
        :param width: the width
        :param height: the height
        :param menuBar: if has menu bar
        """
        super().__init__()
        self.width = width
        self.height = height
        self.control = libui.uiNewWindow(title, width, height, int(menuBar))

        def handler(window, data):
            self.on_close(data)
            return 0

        self.closeHandler = libui.uiWindowOnClosing(self.control, handler,
                                                    None)

        def handlerOnContentSizeChanged(window, data):
            self.on_content_size_changed(data)

        self.contentSizeChangedHandler = libui.uiWindowOnContentSizeChanged(
            self.control, handlerOnContentSizeChanged, None)

    @property
    def title(self):
        """
        Returns the window's title.

        :return: string
        """
        return libui.uiWindowTitle(self.control)

    @title.setter
    def title(self, title):
        """
        Sets the window's title.

        :param title: string
        :return: None
        """
        libui.uiWindowSetTitle(self.control, title)

    @property
    def content_size(self):
        """
        Returns the window's content size.

        :return: tuple
        """
        return libui.uiWindowContentSize(self.control, self.width, self.height)

    @content_size.setter
    def content_size(self, *values):
        """
        Sets the window's content size.

        :param width: int
        :param height: int
        :return: None
        """
        libui.uiWindowSetContentSize(self.control, *values)

    @property
    def fullscreen(self):
        """
        Returns whether the window is in fullscreen.

        :return: bool
        """
        return bool(libui.uiWindowFullscreen(self.control))

    @fullscreen.setter
    def fullscreen(self, fullscreen):
        """
        Sets whether the window is in fullscreen.

        :param fullscreen: bool
        :return: None
        """
        libui.uiWindowSetFullscreen(self.control, int(fullscreen))

    def on_content_size_changed(self, data):
        """
        Executes when window's content size changed.

        :param data: data
        :return: None
        """
        pass

    def on_close(self, data):
        """
        Executes when window is closing.

        :param data: data
        :return: None
        """
        self.destroy()

    @property
    def borderless(self):
        """
        Returns whether the window is borderless.

        :return: bool
        """
        return bool(libui.uiWindowBorderless(self.control))

    @borderless.setter
    def borderless(self, borderless):
        """
        Sets whether the window is borderless.

        :param borderless: bool
        :return: None
        """
        libui.uiWindowSetBorderless(self.control, int(borderless))

    def set_child(self, child):
        """
        Sets a control as child of the window.

        :param child: control
        :return: None
        """
        libui.uiWindowSetChild(self.control, child.pointer())

    @property
    def margined(self):
        """
        Returns whether the window is margined or not.

        :return: bool
        """
        return bool(libui.uiWindowMargined(self.control))

    @margined.setter
    def margined(self, margined):
        """
        Sets whether the window is margined or not.

        :param margined: bool
        :return: None
        """
        libui.uiWindowSetMargined(self.control, int(margined))

    def open_file(self):
        return libui.uiOpenFile(self.control)

    def save_file(self):
        return libui.uiSaveFile(self.control)

    def show_message(self, title, description):
        libui.uiMsgBox(self.control, title, description)

    def show_error(self, title, description):
        libui.uiMsgBoxError(self.control, title, description)
