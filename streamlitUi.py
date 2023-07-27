
# import streamlit as st
# import requests
#
# # Streamlit code
# st.markdown(" #Welcome to OCR application")
# uploaded_image = st.file_uploader("Upload a photo")
#
# # OCR sections
# ocr_sections = [
#     {"name": "Easy OCR", "endpoint": "extract_easy", "button_text": "Perform Easy OCR"},
#     {"name": "Paddle OCR", "endpoint": "extract_paddle", "button_text": "Perform Paddle OCR"},
#     {"name": "Tesseract OCR", "endpoint": "extract_tesseract", "button_text": "Perform Tesseract OCR"}
# ]
#
# ocr_responses = {}  # Dictionary to store OCR responses
#
# for section in ocr_sections:
#     st.markdown(f" #Click for {section['name']}")
#     submit_button = st.button(section["button_text"])
#
#     if submit_button and uploaded_image is not None:
#         files = {"image": uploaded_image}
#         response = requests.post(f"http://localhost:8000/{section['endpoint']}", files=files)
#         ocr_responses[section['name']] = response.json()
#
#     # Display OCR responses
#     if section['name'] in ocr_responses:
#         st.write(ocr_responses[section['name']])

# import streamlit as st
# import requests
#
# # Streamlit code
# st.markdown(" #Welcome to OCR application")
# uploaded_image = st.file_uploader("Upload a photo")
# easy_output_placeholder = st.empty()
#

# #ocr section
# st.markdown("click the button for ocr")
# submit_button_paddle = st.button("perform ocr")
#
# # Pass the uploaded image to the FastAPI endpoint when the submit button is clicked
# if submit_button_paddle and uploaded_image is not None:
#     files = {"image": uploaded_image}
#     response = requests.post("http://localhost:8000/extract_paddle", files=files)
#     st.write(response.json())

import streamlit as st
import requests

# Streamlit code
st.markdown(" #Welcome to OCR application")
uploaded_image = st.file_uploader("Upload a photo")
easy_output_placeholder = st.empty()

#ocr section
st.markdown("click the button for ocr")
submit_button_paddle = st.button("perform ocr")

# Pass the uploaded image to the FastAPI endpoint when the submit button is clicked
if submit_button_paddle and uploaded_image is not None:
    files = {"image": uploaded_image}
    response = requests.post("http://localhost:8000/extract_paddle", files=files)
    ocr_data = response.json()

    # Display OCR responses in different columns
    if ocr_data:
        cols = st.columns(len(ocr_data))
        for idx, (name, value) in enumerate(ocr_data.items()):
            cols[idx].markdown(f"## {name}")
            cols[idx].write(value)

