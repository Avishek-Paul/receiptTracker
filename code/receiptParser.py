import os
from ocr import OCR 

class receiptParser:
	
	ocr = OCR()
	raw_tickets = None

	def __init__(self, image_folder_path):
		self.image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))] 
		
	def scrape_tickets(self):
		self.raw_tickets = self.ocr(self.image_files)

	def parse_tickets(self):
		if not self.raw_tickets:
			self.scrape_tickets()
		
		count = 1
		for raw_ticket in self.raw_tickets:
			ticket_data = raw_ticket.split()
			nums = [float(num[1:]) for num in ticket_data if bool('$' in num and '.' in num)]
			total = max(nums)
			print("The total cost of receipt #{} is: ${}".format(count,total))
			count+=1	

if __name__=="__main__":
	rp = receiptParser('images/')
	rp.parse_tickets()
