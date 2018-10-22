import os
from ocr import OCR 

class receiptParser:
	
	ocr = OCR()
	raw_tickets = None

	def __init__(self, image_folder_path):
		self.image_files = [f for f in os.listdir(image_folder_path) if bool(os.path.isfile(os.path.join(image_folder_path, f)) and '.jpg' in f)] 
		print(self.image_files)

	def scrape_tickets(self):
		self.raw_tickets = self.ocr(self.image_files)

	def format_num(self, num):
		return num.replace(',','.').replace('-','.')

	def determine_num(self, num):
		#input: string
		#output: boolean
		num = self.format_num(num)
		
		if num.count('.')==1:
			vals = num.split('.')# if '.' in num else num.split(',')
			if ('$' in num):
				return True #on basis of it being in the form $XX.YY
			elif len(vals[1])==2 and vals[0].isdigit() and vals[1].isdigit(): #In form XX.YY
				return True
			else:
				return False
		else:
			return False 	 

	def parse_tickets(self):
		if not self.raw_tickets:
			self.scrape_tickets()
		
		final_costs = []	
		count = 1

		for raw_ticket in self.raw_tickets:
			ticket_data = raw_ticket.split()
			
			nums = [float(self.format_num(num.replace('$',''))) for num in ticket_data if self.determine_num(num)]			

			if nums:
				total = max(nums)
				final_costs.append(total)
			else:
				total = "[UNDEFINED]"

			#print("The total cost of receipt #{} is: ${}".format(count,total))
			count+=1
		
		return final_costs

if __name__=="__main__":
	rp = receiptParser('images/')
	print(rp.parse_tickets())
