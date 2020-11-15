import json
import tabulate as tb

#TODO add max data size

class GameDataBase():
	def __init__(self):
		self.data = {}
		self.headers = ["name","size","company","rating","price"]
		self.types = {"name":str, "size":float, "company":str, "rating":float, "price":float}

	def parse_input(self, raw_data):
		if len(raw_data) != len(self.headers):
			return []
		clean_data = {h : None for h in self.headers}

		for i in range(len(self.headers)):
			h = self.headers[i]
			if self.types[h] == float:
				try:
					clean_data[h] = float(raw_data[i])
				except:
					print(f"{h} is not a string, defaults to 'null'")
					clean_data[h] = 'null'
			elif self.types[h] == str and raw_data[i] != "":
				try:
					clean_data[h] = str(raw_data[i])
				except:
					print(f"{h} is not a float, defaults to 0")
					clean_data[h] = 0
		print(clean_data)
		return clean_data

	def add_record(self, raw_data):
		clean_data = self.parse_input(raw_data)
		if clean_data == []:
			return False
		i = 0	#finding the smalles available id
		while i in self.data.keys():	#may be changed later
			i+=1
		# print(clean_data)
		self.data.update({i : {k:v for k,v in zip(self.headers,clean_data)}}) #adding the new record

		print("-added new record at index {}".format(i))


	def remove_record(self, index):
		if(index in self.data.keys()):
			del self.data[index]
			print("-record {} has been deleted.".format(index))
		else:
			print("-record {} does not exist.".format(index))

	def show(self):
		if len(self.data) == 0:
			print("-the database is empty.")
		else: 
			print(self.data)
			table = [[k]+list(v.values()) for k,v in self.data.items()]		#used to be psql
			print(tb.tabulate(table, headers="keys", numalign="right", showindex=True, floatfmt=("id","name",".1f","comp",".1f",".2f")))

	def input_record(self):
		res = []
		for h in self.headers:
			res.append(input(f"Input {h} ({self.types[h]}): "))
		self.add_record(res)

	def input_remove(self):
		i = input("Type the id of the record to be deleted: ")
		try:
			i = int(i)
			gdb.remove_record(i)
		except:
			print("Invalid record id")
	
	# def save_data(self):
	# def load_data(self):	


gdb = GameDataBase()
gdb.show()
gdb.add_record(["Battlefield", 30, "EA", 6.5, 69.99])
gdb.add_record(["Skyrim", 50, "Bethesda", 9, 45.99])
gdb.add_record(["IceTower", 0.5, "Bethesda", 3.7, 0])
gdb.add_record(["ImmortalPlanet", 2, "MonsterCouch", 9, 19.99])
gdb.add_record(["Fallout 97", 34.8, "Bethesda", 9, 37.13])
gdb.add_record(["Nostale", 3.2, "Gameforge", 8.3, 0])
	# gdb.remove_record(1)
gdb.show()

def loop():
	print("---The Game Data Base---")
	print("Type ADD to add a new record.")
	print("Type VIEW to display the table.")
	print("Type REM to remove a record.")
	print("Type EXIT to close the program.")
	while True:
		choice = input("Choose action: ")
		if choice == "ADD":
			gdb.input_record()
		elif choice == "VIEW":
			gdb.show()
		elif choice == "REM":
			gdb.input_remove();
		elif choice == "EXIT":
			break;
		else:
			print("Command unknown")

if __name__ == '__main__':
	loop()