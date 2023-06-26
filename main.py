from fastapi import FastAPI,File,UploadFile,Request
import uvicorn
# import uuid
import shutil
import os
import paddleocrEngine


ImageDir = "images/"
app = FastAPI()

@app.get("/")
def home():
    return {"Hello"}

@app.post("/extract_text")
def perform_ocr(image: UploadFile =File(...)):
    temp_file = save_file_to_disk(image,path="temp",save_as = "temp")
    paddleocrEngine.paddle_ocr(temp_file)


def save_file_to_disk(uploaded_file,path=".",save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path,save_as + extension)
    with open(temp_file,"wb") as buffer:
        shutil.copyfileobj(uploaded_file.file,buffer)
    return temp_file

# @app.post("/upload/")
# async def create_upload_file(file:UploadFile =File(...)):
#     file.filename = f"{uuid.uuid4()}.png"
#     contents = await file.read()
#     with open(f"{ImageDir}{file.filename}", "wb") as f:
#         f.write(contents)
#     return {"filename":file.filename}


if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.0",port=8000)

