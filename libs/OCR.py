from PIL import Image
import os 
import cv2
import numpy as np
import pytesseract

class OCR():
    def __init__(self):
        pass
    @staticmethod
    def load_image_as_gray_image(path:str) -> Image:
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file at {path} does not exist.")
        with Image.open(path) as img:
            gray_img = img.convert("L")
            return gray_img
    @staticmethod
    def otsu_binarization(img:Image) -> Image:
        np_img = np.array(img)
        _, cv_binary_image = cv2.threshold(np_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        binary_image = Image.fromarray(cv_binary_image)
        return binary_image
    @staticmethod
    def extract_english_from_image(img:Image) -> str:
        binary_image = OCR.otsu_binarization(img)
        text = pytesseract.image_to_string(binary_image)
        return text
    @staticmethod
    def extract_japanese_from_image(img:Image) -> str:
        custom_config = r'--psm 4'
        binary_image = OCR.otsu_binarization(img)
        text = pytesseract.image_to_string(binary_image, lang='jpn', config=custom_config)
        return text
