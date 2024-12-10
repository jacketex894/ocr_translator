import unittest
from PIL import Image
import os
import numpy as np
from rapidfuzz import fuzz

from libs.OCR import OCR
from .test_output import english_output,japanese_output
os.chdir('./tests/OCR_test/test_files')

def compare_strings(str1, str2):
    return fuzz.ratio(str1, str2)

class TestOCR(unittest.TestCase):
    def test_can_create_ocr(self):
        ocr_worker = OCR()
        self.assertIsInstance(ocr_worker, OCR)
    
    #load image test
    def test_can_load_image(self):
        img = OCR.load_image_as_gray_image("english_test.png")
        self.assertIsInstance(img, Image.Image)
    def test_load_image_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            img = OCR.load_image_as_gray_image("not_exist.png")
    def test_load_not_image_file(self):
        with self.assertRaises(Exception):
            img = OCR.load_image_as_gray_image("test.txt")
    
    #image pre process test
    def test_can_otsu_binarization(self):
        image_data = np.array([
            [50, 150, 200],
            [100, 180, 50],
            [30, 200, 255]
        ])
        image = Image.new('L', (3, 3))
        image.putdata([pixel for row in image_data for pixel in row])
        binary_image  = OCR.otsu_binarization(image)
        binary_image_data = list(binary_image.getdata())
        self.assertEqual(binary_image_data[0],0)  # 50 < otsu_threshold
        self.assertEqual(binary_image_data[1],255)  # 150 > otsu_threshold
        self.assertEqual(binary_image_data[-1],255)  # 255 > otsu_threshold
    
    #english word identify test
    def test_can_identify_english_from_image(self):
        img = OCR.load_image_as_gray_image("english_test.png")
        content = OCR.extract_english_from_image(img)
        self.assertGreater(compare_strings(content, english_output), 90)
    
    #japanese word identify test
    def test_can_identify_japanese_from_image(self):
        img = OCR.load_image_as_gray_image("japanese_test.png")
        content = OCR.extract_japanese_from_image(img)
        self.assertGreater(compare_strings(content, japanese_output), 90)
if __name__ == '__main__':
    unittest.main()