from PIL import Image
import pytesseract
import os

class ocr:

    def __init__(self, image_name):
        return self.img_to_text(image_name)

    def img_to_text(self, *args):
        
        texts = []

        for image_name in args:
            image_path = "images/"+image_name

            gray = Image.open(image_path).convert('L')

            gray_img_name = "{}".format("gray_"+image_name)
            gray_file_path = "images/" + gray_img_name 

            gray.save(gray_file_path)

            text = pytesseract.image_to_string(Image.open(gray_file_path))
            os.remove(gray_file_path)

        return texts  



if __name__=="__main__":
    ocr('receipt.jpg')

