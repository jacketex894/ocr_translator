import time
import threading
import win32api
import win32con
import customtkinter
import queue
import multiprocessing

from libs.CaptureScreen import CaptureScreen
from libs.OCR import OCR
from libs.LLM import LLM
from libs.llm_models_info import sakura_model_14b

recognition_thread = queue.LifoQueue(maxsize=1)

def start_recognition(recognition_label:customtkinter.CTkLabel):
    # wait button click release
    while True:
        mouse_state = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)
        if mouse_state == 0:
            break
    recognition_label.configure(text="Please select the recognition area first.")
    capture_screen_worker = CaptureScreen()
    start_position,end_position = capture_screen_worker.capture_screen_area()
    while True:
        img = capture_screen_worker.screen_shot(start_position,end_position)
        gray_image = OCR.image_to_gray(img)
        binary_image = OCR.otsu_binarization(gray_image)
        content = OCR.extract_japanese_from_image(binary_image)
        recognition_label.configure(text=f"Recognize Text: {content}")
        while not recognition_thread.empty():
            recognition_thread.get()
        recognition_thread.put(content)
        time.sleep(0.5)

def start_recognition_thread(recognition_label):
    threading.Thread(target=start_recognition, args=(recognition_label,), daemon=True).start()

def start_translate(translate_label:customtkinter.CTkLabel):
    llm_worker = LLM(sakura_model_14b['model_name'],sakura_model_14b['huggingface_repo_id'])
    while True:
        content = recognition_thread.get()
        if content:
            answer = llm_worker.excute_model(content)
            translate_label.configure(text=f"Translate Text:{answer}")

def start_translate_thread(translate_label:customtkinter.CTkLabel):
    threading.Thread(target=start_translate, args=(translate_label,), daemon=True).start()