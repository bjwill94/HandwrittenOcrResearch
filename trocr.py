from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
from IPython.display import display
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-large-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-large-handwritten")
def show_image(pathStr):
    img= Image.open(pathStr).convert("RGB")
    display(img)
    return img
#
def ocr_image(src_img):
    pixel_values = processor(images=src_img,return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    return processor.batch_decode(generated_ids,skip_special_tokens=True)[0]
#
#
shw_iamge = show_image('Images/handwrittendata.png')
shw_image1= shw_iamge.crop((0,10,shw_iamge.width,40))
# display(shw_image1)
print(ocr_image(shw_iamge))
