import random
from datetime import date
import time

class Generate:
	def pesel(count=1):
		PESEL_OUT = []

		queue = 0
		while count > queue:
			check = False
			pesel_date_sex = []
			random_date_pesel = random.randint(1, int(time.time()))
			data = date.fromtimestamp(time.time()-random_date_pesel)
			data_string = date.strftime(data, "%Y%m%d")

			#Tworzenie PESELu
			if data_string[:2] == '20':
				six_first = str(int(data_string) + 2_000)[2:]
			elif data_string[:2] == '19':
				six_first = data_string[2:]
			four = random.randint(1, 9999)

			six_first += str(four).zfill(4)

			if (four % 10) % 2 == 0:
				sex = 'Kobieta'
			elif (four % 10) % 2 == 1:
				sex = 'Mężczyzna' 

			control_number = 10 - ((int(six_first[0])+int(six_first[1])*3+int(six_first[2])*7+
							int(six_first[3])*9+int(six_first[4])+int(six_first[5])*3+
							int(six_first[6])*7+int(six_first[7])*9+int(six_first[8])+
							int(six_first[9])*3) % 10) 
			six_first += str(control_number)[-1]

			pesel_date_sex.append(six_first)
			pesel_date_sex.append(data)
			pesel_date_sex.append(sex)
			
			if PESEL_OUT:
				for k in PESEL_OUT:
					if six_first == k[0]:
						check = True
						break
			if check == True:
				continue
			PESEL_OUT.append(pesel_date_sex)
			queue += 1
			
		return PESEL_OUT
