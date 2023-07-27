from fastapi import FastAPI,File,UploadFile,Request
import uvicorn
import shutil
import os
import EasyOcr
import testpad
import Tesseract

ImageDir = "images/"
app = FastAPI()

@app.get("/")
def home():
    return {"Hello"}

@app.post("/extract_easy")
def perform_easy(image: UploadFile =File(...)):
    temp_file1 = save_file_to_disk(image,path="temp",save_as = "temp")
    easyoutput=EasyOcr.extract_text_from_image(temp_file1)
    print(easyoutput)
    return easyoutput

@app.post("/extract_paddle")
def perform_easy(image: UploadFile =File(...)):
    temp_file2 = save_file_to_disk(image,path="temp",save_as = "temp")
    paddleoutput=testpad.paddle_ocr(temp_file2)
    print(paddleoutput)
    return paddleoutput

@app.post("/extract_tesseract")
def perform_ocr(image: UploadFile =File(...)):
    temp_file3 = save_file_to_disk(image,path="temp",save_as = "temp")
    tesseract_output=Tesseract.tessearct_ocr(temp_file3)
    print(tesseract_output)
    return tesseract_output

@app.post("/combination")
def perform_allocr(image: UploadFile =File(...)):
    ocrresult = {}
    temp_file = save_file_to_disk(image,path="temp",save_as = "temp")
    paddle_output = testpad.paddle_ocr(temp_file)
    ocrresult["paddle_ocr"]=paddle_output
    print("paddle ocr detector:" +paddle_output)
    easy_output = EasyOcr.extract_text_from_image(temp_file)
    ocrresult["easy_ocr"]=easy_output
    print("easy ocr detector:" +easy_output)
    tesseract_output = Tesseract.tessearct_ocr(temp_file)
    ocrresult["tesseract_ocr"] = tesseract_output
    print("tesseract ocr detector:" +tesseract_output)
    return ocrresult




def save_file_to_disk(uploaded_file,path=".",save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path,save_as + extension)
    with open(temp_file,"wb") as buffer:
        shutil.copyfileobj(uploaded_file.file,buffer)
    return temp_file



if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.0",port=8000)

