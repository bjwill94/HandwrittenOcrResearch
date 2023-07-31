
# Handwritten Text extraction from images Using Ocr Models

This project repository aims to extract handwritten data from images by making use of different OCR Models that includes paddleOCR, tesseractOCR, easyOCR and trOCR. We use StreamlitUI for UI to pass an input image to the ocr models using FastApi integration then show OCR generated text as an output in StreamlitUI.



## Step 1
The input image for OCR extraction is uploaded using the streamlitUi to pass an input image to the ocr models.
## Step 2
The input image uploaded via streamlitui is passed to the ocr model using FastApi integration.
## Step 3
The texts extracted from the image is passed back to the streamlitUi using the fastapi and the extracted text is displayed as output on the click of a button.
## Requirements
Make sure you have the following dependencies installed:

1. easyocr
2. fastapi
3. ipython
4. paddleocr
5. Pillow
6. Pillow
7. pytesseract
8. Requests
9. streamlit
10. transformers
11. uvicorn

You can install these using the requirements.txt file: pip install -r requirements.txt
## Usage/Examples

1. Clone the repository: git clone https://github.com/bjwill94/HandwrittenOcrResearch.git
2. Change the directory: cd UI
3. Create a virtual environment: python -m venv env
4. Activate the virtual environment: .\venv\Scripts\activate
5. Install the required dependencies: pip install -r requirements.txt
6. Run the uvicorn application to start the fastapi server:uvicorn ocr:app --reload
7. Run the Streamlit application: streamlit run StreamlitUi.py

For Tesseract OCR you also need to install its setup which can be found in the following link: https://github.com/UB-Mannheim/tesseract/wiki

## Demo
1. Streamlit Ui to upload an image to perform OCR

<img width="660" alt="image" src="https://github.com/bjwill94/HandwrittenOcrResearch/assets/56854060/677f6d70-e3bd-487d-99e0-f6aba2883bf4">

2. Output after performing the OCR 

<img width="614" alt="image" src="https://github.com/bjwill94/HandwrittenOcrResearch/assets/56854060/a0182cbc-24f2-4f38-bac2-2087f9f8238a">

## Acknowledgements

 1. This project utilizes the FastApi for passing the input image to the server as well as fetching back the ocr to the Ui.The FastApi documentation can be refered by https://fastapi.tiangolo.com/

2. The PaddleOCR library is used for OCR processing. For more information, please refer to the PaddleOCR GitHub page.
3. The EasyOCR library is used for OCR processing. For more information, please refer to the EasyOCR GitHub page.
4. The TesseractOcr library is used for OCR processing.For more information, please refer to the TesseractOcr.
5. The Streamlit library is used to create the web application. For more information, please refer to the Streamlit documentation.

