from fastapi import FastAPI,File,UploadFile,Request
from fastapi.templating import Jinja2Templates
import uvicorn
import testpad
import EasyOcr
import Tesseract

ImageDir = "images/"
app = FastAPI()
templates = Jinja2Templates(directory="Templates")

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

# @app.post("/extract")
# def perform_ocr():
#     paddleocrEngine.paddle_ocr()


@app.post("/extract_paddle")
def perform_ocr(image: UploadFile =File(...)):
    # temp_file = save_file_to_disk(image,path="temp",save_as = "temp")
    temp_var = testpad.paddle_ocr(image)
    print(temp_var)

@app.post("/extract_easy/easy")
def perform_ocr(image2: UploadFile =File(...)):
    # temp_file = save_file_to_disk(image,path="temp",save_as = "temp")
    temp_var = EasyOcr.extract_text_from_image(image2)
    print(temp_var)


@app.post("/extract_tesseract/tess/tesseract")
def perform_ocr(image3: UploadFile = File(...)):
    # temp_file = save_file_to_disk(image,path="temp",save_as = "temp")
    temp_var = Tesseract.tessearct_ocr(image3)
    print(temp_var)

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.0",port=8000)

# def save_file_to_disk(uploaded_file,path=".",save_as="default"):
#     extension = os.path.splitext(uploaded_file.filename)[-1]
#     temp_file = os.path.join(path,save_as + extension)
#     with open(temp_file,"wb") as buffer:
#         shutil.copyfileobj(uploaded_file.file,buffer)
#     return temp_file



# @app.post("/upload/")
# async def create_upload_file(file:UploadFile =File(...)):
#     file.filename = f"{uuid.uuid4()}.jpg"
#     contents = await file.read()
#
#     with open(f"{ImageDir}{file.filename}","wb") as f:
#         f.write(contents)
#
#         return {"filename":file.filename}



