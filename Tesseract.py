# import pytesseract
# from PIL import Image
#
# def tessearct_ocr(imagepath):
#     image=Image.open(imagepath)
#     text=pytesseract.image_to_string(image)
#     return text




import pytesseract
from PIL import Image

def tessearct_ocr(imagepath):
    image=Image.open(imagepath)
    text=pytesseract.image_to_string(image)
    return text
imagepath="C:/Users/HP/PycharmProjects/FastApi/Images/handwrittendata.png"
extracted_text = tessearct_ocr(imagepath)
print(extracted_text)