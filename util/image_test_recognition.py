import time
import threading
import win32api
import win32con

from libs.CaptureScreen import CaptureScreen
from libs.OCR import OCR


def start_recognition(label):

    # wait button click release
    while True:
        mouse_state = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)
        if mouse_state == 0:
            break
        
    capture_screen_worker = CaptureScreen()
    start_position,end_position = capture_screen_worker.capture_screen_area()
    while True:
        img = capture_screen_worker.screen_shot(start_position,end_position)
        gray_image = OCR.image_to_gray(img)
        binary_image = OCR.otsu_binarization(gray_image)
        content = OCR.extract_japanese_from_image(binary_image)
        label.configure(text=f"辨識文字是: {content}")
        time.sleep(0.5) 

def start_recognition_thread(label):
    threading.Thread(target=start_recognition, args=(label,), daemon=True).start()