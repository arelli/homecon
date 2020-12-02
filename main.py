
class receipt:
	def __init__(self,amount = "",recipient = "" ,date = "" ,method = "" ,comments = "" ,id = ""):
			self.amount = ""
			self.recipient = ""
			self.date = ""
			self.method = ""
			self.comments = ""
			self.id = ""

	def user_init(self):
			self.amount = input("Enter the amount of money in the transaction:        ")
			self.recipient = input("Enter where the money whent(person/organisation):    ")
			self.date = input("Enter the date of the transaction:                   ")
			self.method = input("Enter the method(cash,debit e.t.c.):                 ")
			self.comments = input("Enter any comment about the transaction:             ")
			self.id = input("Enter an id for the trasaction:                      ")


	def print_info(self):
		print("Amount:                " + str(self.amount))
		print("Recipient:             " + str(self.recipient))
		print("Date:                  " + str(self.date))
		print("Method of Payment:     " + str(self.method))
		print("Comments:              " + str(self.comments))
		print("ID Number:             " + str(self.id))


class method_of_payment:
	def __init__(self,name,comments,id):
		self.name = name
		self.comments = comments
		self.id = 0

class person:
	def __init__(self,name,surname,commments,id):
		self.name = name
		self.surname = surname
		self.comments = comments
		self.id = 0

class organisation:
	def __init__(self,name,comments):
		self.name = name
		self.comments = comments
		self.id = 0


def save_receipt(rcpt,filename):
	line_to_save = str(rcpt.amount) + "," + str(rcpt.recipient) + "," + str(rcpt.date) + "," + str(rcpt.method) + "," + str(rcpt.comments) + "," + str(rcpt.id)
	with open(filename, "a") as savefile:
		savefile.write(line_to_save)
		savefile.write("\n")
		savefile.close()

# Method to take a string with comma seperated values and create a receipt object out of it
# used to get receipt objects saved in the main memory
def make_receipt(string):
	attr = string.split(",")  #split comma seperate elements
	temp_receipt = receipt(attr[0],attr[1],attr[2],attr[3],attr[4],attr[5])  # make a receipt object with these attributes
	temp_receipt.amount = attr[0]
	temp_receipt.recipient = attr[1]
	temp_receipt.date = attr[2]
	temp_receipt.method = attr[3]
	temp_receipt.comments = attr[4]
	temp_receipt.i = attr[5]
	return temp_receipt


def get_income():
	with open("income.txt") as file:
	    my_income = [line.strip() for line in file]
	    file.close()
	return my_income;


def get_expenses():
	with open("expenses.txt") as file:
	    my_expenses = [line.strip() for line in file]
	    file.close()
	return my_expenses


def get_belongings():
	with open("belongings.txt") as file:
	    my_belongings = [line.strip() for line in file]
	    file.close()
	return my_belongings


def get_methods():
	with open("methods.txt") as file:
	    list_of_methods = [line.strip() for line in file]
	    file.close()
	return list_of_methods


def get_persons():
	with open("persons.txt") as file:
	    list_of_persons = [line.strip() for line in file]
	    file.close()
	return list_of_persons


def get_oganisations():
	with open("organisations.txt") as file:
	    list_of_organisations = [line.strip() for line in file]
	    file.close()
	return list_of_organisations


def add_income():
	print("Entering a new income receipt..")
	temp_receipt = receipt()
	temp_receipt.user_init()
	print("Object created.Saving to file..\n")
	save_receipt(temp_receipt,"income.txt")
	print("Done!\n")


def add_expense():
	print("Entering a new income receipt..")
	temp_receipt = receipt()
	temp_receipt.user_init()
	print("Object created.Saving to file..\n")
	save_receipt(temp_receipt,"expenses.txt")
	print("Done!\n")

def print_list(filename):
		file = open(filename, "r")
		line_list = [line.strip() for line in file]
		file. close()
		line_count = len(line_list)
		counter = 0
		while(counter<line_count):
			print("\n")
			temp_receipt = make_receipt(line_list[counter])
			temp_receipt.print_info()
			counter = counter + 1
			print("\n")

my_income = []
my_expenses = []
my_belongings = []
list_of_methods = []
list_of_persons = []
list_of_organisations = []


choice = -1

while(choice!="0"):
	if (choice == "1"):
		add_income()
	elif (choice == "2"):
		add_expense()
	elif(choice == "3"):
		print_list("income.txt")
	elif(choice == "4"):
		print_list("expenses.txt")
	else:
		print("Please enter a valid option(0-4).\n")

	choice = input("1:add income, 2:add expense, 3:print income, 4:print expenses, 0:exit:   ")






