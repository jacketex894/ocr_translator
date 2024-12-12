import unittest
from unittest.mock import patch
from libs.CaptureScreen import CaptureScreen
from PIL import Image

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
        screen_shot_image = self.capture_screen_worker.screen_shot(start_position,end_position)
        self.assertIsInstance(screen_shot_image,Image.Image)
if __name__ == '__main__':
     unittest.main()