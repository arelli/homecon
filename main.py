
from appJar import gui

class receipt:
	def __init__(self,amount = "",recipient = "", sender = "" ,date = "" ,method = "" ,comments = "" ,id = ""):
			self.amount = ""
			self.recipient = ""
			self.sender = ""
			self.date = ""
			self.method = ""
			self.comments = ""
			self.id = ""

	def user_init(self):
			self.amount = input("Enter the amount of money in the transaction:        ")
			self.recipient = input("Enter the recipient:                            ")
			self.sender = input("Enter the sender:                                        ")
			self.date = input("Enter the date of the transaction:                   ")
			self.method = input("Enter the method(cash,debit e.t.c.):                 ")
			self.comments = input("Enter any comment about the transaction:             ")
			self.id = input("Enter an id for the trasaction:                      ")


	def print_info(self):
		print("Amount:                " + str(self.amount))
		print("Recipient:             " + str(self.recipient))
		print("Sender:                " + str(self.sender))
		print("Date:                  " + str(self.date))
		print("Method of Payment:     " + str(self.method))
		print("Comments:              " + str(self.comments))
		print("id Number:             " + str(self.id))


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
	line_to_save = str(rcpt.amount) + "," + str(rcpt.recipient) + "," + str(rcpt.sender) + "," + str(rcpt.date) + "," + str(rcpt.method) + "," + str(rcpt.comments) + "," + str(rcpt.id)
	with open(filename, "a") as savefile:
		savefile.write(line_to_save)
		savefile.write("\n")
		savefile.close()

# Method to take a string with comma seperated values and create a receipt object out of it
# used to get receipt objects saved in the main memory
def make_receipt(string):
	attr = string.split(",")  #split comma seperate elements
	temp_receipt = receipt()  # make a receipt object with these attributes
	temp_receipt.amount = attr[0]
	temp_receipt.recipient = attr[1]
	temp_receipt.sender = attr[2]
	temp_receipt.date = attr[3]
	temp_receipt.method = attr[4]
	temp_receipt.comments = attr[5]
	temp_receipt.id = attr[6]
	return temp_receipt


def get_income():
	with open("income") as file:
	    my_income = [line.strip() for line in file]
	    file.close()
	return my_income;


def get_expenses():
	with open("expenses") as file:
	    my_expenses = [line.strip() for line in file]
	    file.close()
	return my_expenses


def get_belongings():
	with open("belongings") as file:
	    my_belongings = [line.strip() for line in file]
	    file.close()
	return my_belongings


def get_methods():
	with open("methods") as file:
	    list_of_methods = [line.strip() for line in file]
	    file.close()
	return list_of_methods


def get_persons():
	with open("persons") as file:
	    list_of_persons = [line.strip() for line in file]
	    file.close()
	return list_of_persons


def get_oganisations():
	with open("organisations") as file:
	    list_of_organisations = [line.strip() for line in file]
	    file.close()
	return list_of_organisations


def add_income():
	print("Entering a new income receipt..")
	temp_receipt = receipt()
	temp_receipt.user_init()
	print("Object created.Saving to file..\n")
	save_receipt(temp_receipt,"income")
	print("Done!\n")


def add_expense():
	print("Entering a new income receipt..")
	temp_receipt = receipt()
	temp_receipt.user_init()
	print("Object created.Saving to file..\n")
	save_receipt(temp_receipt,"expenses")
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

def graphical_add_receipt():
	# handle button events
	def press(button):
		if button == "Exit":
			app.stop()
		if button == "SaveAsIncome":
			temp_receipt = receipt()
			temp_receipt.amount = app.getEntry("Amount")
			temp_receipt.recipient = app.getEntry("Recipient")
			temp_receipt.sender = app.getEntry("Sender")
			temp_receipt.date = app.getEntry("Date")
			temp_receipt.method = app.getEntry("Method")
			temp_receipt.comments = app.getEntry("Commends") 
			temp_receipt.id =  app.getEntry("identification")
			save_receipt(temp_receipt,"income")
			print("saved the income..\n")
			app.stop()
		if button == "SaveAsExpense":
			temp_receipt = receipt()
			temp_receipt.amount = app.getEntry("Amount")
			temp_receipt.recipient = app.getEntry("Recipient")
			temp_receipt.recipient = app.getEntry("Recipient")
			temp_receipt.date = app.getEntry("Date")
			temp_receipt.method = app.getEntry("Method")
			temp_receipt.comments = app.getEntry("Commends") 
			temp_receipt.id =  app.getEntry("identification")
			save_receipt(temp_receipt,"expenses")
			print("saved the expenses..\n")
			app.stop()

	# create a GUI variable called app
	app = gui("Receipt Adder", "500x400")
	app.setBg("green")
	app.setFont(15)

	# add & configure widgets - widgets get a name, to help referencing them later
	app.addLabel("title", "Add a Receipt")

	app.addLabelEntry("Amount")
	app.addLabelEntry("Recipient")
	app.addLabelEntry("Sender")
	app.addLabelEntry("Date")
	app.addLabelEntry("Method")
	app.addLabelEntry("Commends")
	app.addLabelEntry("identification")

	# link the buttons to the function called press
	app.addButtons(["SaveAsIncome", "SaveAsExpense", "Exit"], press)

	app.setFocus("Amount")
	# start the GUI
	app.go()


choice = -1

while(choice!="0"):
	if (choice == "1"):
		graphical_add_receipt()
	elif(choice == "2"):
		print_list("income")
	elif(choice == "3"):
		print_list("expenses")
	else:
		print("Please enter a valid option(0-3).\n")

	choice = input("1:add receipt(income or expense), 2:print income, 3:print expenses, 0:exit:   ")






