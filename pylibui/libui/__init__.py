from .lib import *


def uiControlPointer(obj):
    return ffi.cast('uiControl *', obj)
