from paddleocr import PaddleOCR
import json

def paddle_ocr(image_path):
    ocr = PaddleOCR()
    # image_path = 'C:/Users/HP/PycharmProjects/FastApi/Images/handwrittendata.png'
    result = ocr.ocr(image_path)
    jsonarr = []
    for res in result[0]:
        tupleref = res[1]
        jsonarr.append(tupleref[0]
    #         {
    #     "label": tupleref[0],
    #     # "confidence": tupleref[1]
    # }
        )
        # elements=jsonarr
        # sentence = ' '.join(elements)
        # return sentence
    elements=json.dumps(jsonarr)
    # sentence = ' '.join(elements)
    return elements

# paddle_ocr('C:/Users/HP/PycharmProjects/FastApi/Images/handinvoice1.png')

