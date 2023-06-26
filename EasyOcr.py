# import easyocr
#
# def extract_text_from_image(image_path):
#     # Create an instance of the EasyOCR reader
#     reader = easyocr.Reader(['en'])  # Specify the languages you want to recognize
#
#     # Read the image using EasyOCR
#     result = reader.readtext(image_path)
#
#     # Concatenate the recognized text into a single sentence
#     text = ' '.join([detection[1] for detection in result])
#
#     # Return the extracted text
#     return text
#


import easyocr

def extract_text_from_image(image_path):
    # Create an instance of the EasyOCR reader
    reader = easyocr.Reader(['en'])  # Specify the languages you want to recognize

    # Read the image using EasyOCR
    result = reader.readtext(image_path)

    # Concatenate the recognized text into a single sentence
    text = ' '.join([detection[1] for detection in result])

    # Return the extracted text
    return text


# Provide the path to your image file
image_path = "Images/handwrittendata.png"

# Extract text from the image
extracted_text = extract_text_from_image(image_path)

# Print the extracted text
print(extracted_text)



# import easyocr
#
# # Create an instance of the EasyOCR reader
# reader = easyocr.Reader(['en'])  # Specify the languages you want to recognize
# image_path = "Images/handwrittendata.png"
#
# # Read the image using EasyOCR
# result = reader.readtext(image_path)
#
# for detection in result:
#     text = detection[1]
#     confidence = detection[2]
#     box = detection[0]
#
#     # Print the text and its confidence level
#     print("Text:", text)
#     print("Confidence:", confidence)
#     print("Bounding box coordinates:", box)
#
