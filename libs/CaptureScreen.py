from pynput import mouse
from PIL import ImageGrab,Image
from ctypes import windll, Structure, c_long, byref
import win32api
import win32gui
import win32con
import mss

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

class CaptureScreen():
    def __init__(self):
        pass
    def get_cursor_pos(self) -> tuple[c_long,c_long]:
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return pt.x, pt.y
    def capture_screen_area(self):
        start_position = None
        end_position = None
        while True:
            if win32api.GetAsyncKeyState(win32con.VK_LBUTTON) < 0:
                if start_position is None:
                    start_position = self.get_cursor_pos()
                end_position = self.get_cursor_pos()
            #after release the left mouse button
            elif start_position and end_position:
                break
        return start_position,end_position