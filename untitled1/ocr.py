import pytesseract
from PIL import Image
"""
                                            Created by ABHISHEK KOUSHIK B N 
                                                        AND
                                                       AKASH R
                                            on 01/02/2019
 """


def get_ocr(src):
    image = Image.open(src)
    text = pytesseract.image_to_string(image)
    return text
