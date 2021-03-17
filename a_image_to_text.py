#!/usr/bin/env python
# coding: utf-8

# In[1]:


# text recognition
import cv2
#import tesseract
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\student\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
# read image
im = cv2.imread(r'C:\Users\student\Downloads\ocr_handwriting_reco_result01.JPG')
# configurations
config = ('-l eng --oem 1 --psm 3')
# pytessercat
text = pytesseract.image_to_string(im, config=config)
# print text
text = text.split('\n')
print(text)


# In[ ]:




