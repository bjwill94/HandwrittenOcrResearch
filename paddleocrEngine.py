
from paddleocr import PaddleOCR
import json

def paddle_ocr(image_path):
    ocr = PaddleOCR()
    # image_path = 'C:/Users/HP/PycharmProjects/FastApi/Images/handwrittendata.png'
    result = ocr.ocr(image_path)
    return result
    # jsonarr = []
    # for res in result[0]:
    #     tupleref = res[1]
    #     jsonarr.append({
    #     "label": tupleref[0],
    #     "confidence": tupleref[1]
    # })
    # return json.dumps(jsonarr)

# paddle_ocr('C:/Users/HP/PycharmProjects/FastApi/Images/handwrittendata.png')

