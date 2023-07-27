import os
import shutil

from fastapi import FastAPI,File,UploadFile,Request
from fastapi.templating import Jinja2Templates
import uvicorn
import testpad
import EasyOcr
import Tesseract
import trocr

ImageDir = "images/"
app = FastAPI()
templates = Jinja2Templates(directory="Templates")
#
@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/extract_paddle")
def perform_ocr(image: UploadFile =File(...)):
    ocrresult = {}
    temp_file = save_file_to_disk(image,path="temp",save_as = "temp")
    paddle_output = testpad.paddle_ocr(temp_file)
    ocrresult["paddle_ocr"]=paddle_output
    print("********************************************************")
    print("paddle ocr detector:" +paddle_output)
    easy_output = EasyOcr.extract_text_from_image(temp_file)
    ocrresult["easy_ocr"] = easy_output
    print("easy ocr detector:" +easy_output)
    tesseract_output = Tesseract.tessearct_ocr(temp_file)
    ocrresult["tesseract_ocr"] = tesseract_output
    print("tesseract ocr detector:" +tesseract_output)
    return ocrresult

@app.post("/extract_tesseract/tess/tesseract")
def perform_ocr(image3: UploadFile = File(...)):
    temp_file3 = save_file_to_disk(image3,path="temp",save_as = "temp")
    temp_var = Tesseract.tessearct_ocr(temp_file3)
    print(temp_var)

def save_file_to_disk(uploaded_file,path=".",save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path,save_as + extension)
    with open(temp_file,"wb") as buffer:
        shutil.copyfileobj(uploaded_file.file,buffer)
    return temp_file

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.0",port=8000)





