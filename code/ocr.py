from PIL import Image
import pytesseract
import os

class OCR:

	def __call__(self, image_names):
		return self.img_to_text(image_names)

	def img_to_text(self, args):
        
		texts = []

		for image_name in args:
			image_path = "images/"+image_name

			gray = Image.open(image_path).convert('L')

			gray_img_name = "{}".format("gray_"+image_name)
			gray_file_path = "images/" + gray_img_name 

			gray.save(gray_file_path)

			text = pytesseract.image_to_string(Image.open(gray_file_path))
			texts.append(text)

			os.remove(gray_file_path)

		return texts  



if __name__=="__main__":
	ocr = OCR()
	print(ocr(['receipt.jpg','cp_receipt1.jpg']))
