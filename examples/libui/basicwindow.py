"""
 Examples for the pylibui.libui module

 Create a simple window.

"""

from pylibui import libui

# Initialize libui
options = libui.uiInitOptions()
libui.uiInit(options)

# Window
window = libui.uiNewWindow('Window', 640, 480, 1)
libui.uiWindowSetMargined(window, 1)


# Create quit handler
def on_closing(window, data):
    print('On closing..')
    control = libui.uiControlPointer(window)
    libui.uiControlDestroy(control)
    libui.uiQuit()
    return 0


# Keep reference to native C on_closing handler
onclose = libui.uiWindowOnClosing(window, on_closing, None)

# Show window
control = libui.uiControlPointer(window)
libui.uiControlShow(control)

# Main loop
libui.uiMain()

# Destroy
libui.uiUninit()
