import unittest
from PIL import Image
from unittest.mock import patch,MagicMock
from libs.CaptureScreen import CaptureScreen,POINT
from ctypes import windll, byref
class TestScreenCapture(unittest.TestCase):
    def setUp(self):
        self.capture_screen_worker = CaptureScreen()
    def test_can_create_capture_screen(self):
        self.assertIsInstance(self.capture_screen_worker,CaptureScreen)
    def test_can_get_cursor_pos(self):
        x,y = self.capture_screen_worker.get_cursor_pos()
        self.assertGreaterEqual(x, 0)
        self.assertGreaterEqual(y, 0)
    def test_can_get_screen_area(self):
        print('Start the test to get the screen area.\nPlease click and hold the left mouse button to drag and select a range.')
        start_position,end_position = self.capture_screen_worker.capture_screen_area()
        self.assertGreaterEqual(start_position, (0,0))
        self.assertGreaterEqual(end_position, (0,0))
if __name__ == '__main__':
     unittest.main()