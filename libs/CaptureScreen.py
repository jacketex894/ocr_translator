from ctypes import windll, Structure, c_long, byref
import win32api
import win32gui
import win32con
import win32print
import time
from mss import models
from PIL import Image,ImageGrab

UPDATE_TIME = 0.001


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

class CaptureScreen():
    def __init__(self):

        # get windows scaling
        hdc = win32gui.GetDC(0)
        device_height = win32print.GetDeviceCaps(hdc,win32con.DESKTOPVERTRES)
        display_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        win32gui.ReleaseDC(0, hdc)
        self.scale = device_height / display_height

    def get_cursor_pos(self) -> tuple[c_long,c_long]:
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return pt.x, pt.y
    
    def draw_rectangle(self,hdc:int,start_position:tuple[int,int],end_position:tuple[int,int]):
        pen = win32gui.CreatePen(win32con.PS_SOLID, 2, win32api.RGB(255, 0, 0))
        brush = win32gui.GetStockObject(win32con.NULL_BRUSH)
        win32gui.SelectObject(hdc, pen)
        win32gui.SelectObject(hdc, brush)
        win32gui.Rectangle(hdc, int(start_position[0]*self.scale), int(start_position[1]*self.scale), int(end_position[0]*self.scale), int(end_position[1]*self.scale))
        win32gui.DeleteObject(pen)
    
    def capture_screen_area(self)->tuple[tuple[int,int],tuple[int,int]]:
        start_position = None
        end_position = None

        #get device content for drawing red rectangle
        hdc = win32gui.GetDC(0)
        while True:

            #check mouse left button click
            if win32api.GetAsyncKeyState(win32con.VK_LBUTTON) < 0:
                if start_position is None:
                    start_position = self.get_cursor_pos()
                end_position = self.get_cursor_pos()
                
                #clean rectangle
                win32gui.InvalidateRect(0, None, True)
                if start_position and end_position:
                    self.draw_rectangle(hdc,start_position,end_position)
            #after release the left mouse button
            elif start_position and end_position:
                break
            time.sleep(UPDATE_TIME) 
        win32gui.ReleaseDC(0, hdc)
        return start_position,end_position
    def screen_shot(self,start_position:tuple[int,int],end_position:tuple[int,int]) -> Image.Image:
        screen_range= (
            int(min(start_position[0], end_position[0]) * self.scale),
            int(min(start_position[1], end_position[1]) * self.scale),
            int(max(start_position[0], end_position[0]) * self.scale),
            int(max(start_position[1], end_position[1]) * self.scale),
        )
        img = ImageGrab.grab(bbox=screen_range)
        return img