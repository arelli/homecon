from appJar import gui
from os import path

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

	def return_info(self):
		return_string = str(self.amount) + ", " + str(self.recipient) + ", " + str(self.sender) + ", " 
		return_string = return_string + str(self.date) + ", " + str(self.method) + ", " + str(self.comments) + "\n"
		return return_string


class method_of_payment:
	def __init__(self,name,comments,id):
		self.name = name
		self.comments = comments
		self.id = 0

class person:
	def __init__(self,name = "" ,surname = "",comments = "",id = ""):
		self.name = name
		self.surname = surname
		self.comments = comments
		self.id = 0

class organisation:
	def __init__(self,name,comments):
		self.name = name
		self.comments = comments
		self.id = 0

# save an object of the receipt class as a text, in a specified file by appending it as csv
def save_receipt(rcpt,filename):
	line_to_save = str(rcpt.amount) + ", " + str(rcpt.recipient) + ", " + str(rcpt.sender) + ", " + str(rcpt.date) + ", " + str(rcpt.method) + ", " + str(rcpt.comments) + ", " + str(rcpt.id)
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


def save_person(person,filename):
	line_to_save = str(person.name) + "," + str(person.surname) + "," + str(person.comments) + "," + str(person.id)
	with open(filename, "a") as savefile:
		savefile.write(line_to_save)
		savefile.write("\n")
		savefile.close()

def make_person(string):
	attr = string.split(",")  #split comma seperate elements
	temp_person = person()  # make a receipt object with these attributes
	temp_person.name = attr[0]
	temp_person.surname = attr[1]
	temp_person.comments = attr[2]
	temp_person.id = attr[3]
	return temp_person


# get list of income from file
def get_income():
	with open("income") as file:
	    my_income = [line.strip() for line in file]
	    file.close()
	return my_income;

# get list of expenses from file
def get_expenses():
	with open("expenses") as file:
	    my_expenses = [line.strip() for line in file]
	    file.close()
	return my_expenses

# get list of belongings from file
def get_belongings():
	with open("belongings") as file:
	    my_belongings = [line.strip() for line in file]
	    file.close()
	return my_belongings

# get list of methods from file
def get_methods():
	with open("methods") as file:
	    list_of_methods = [line.strip() for line in file]
	    file.close()
	return list_of_methods

# get list of persons objects from file
def get_persons():
	with open("persons") as file:
	    list_of_persons = [line.strip() for line in file]
	    file.close()

	list_of_persons_objects = []
	counter = 0
	while(counter<len(list_of_persons)):
		list_of_persons_objects.append(make_person(list_of_persons[counter]))
		counter = counter+1

	return list_of_persons_objects


def get_persons_names(list_of_persons_objects):
	list_of_persons_names = []
	counter = 0
	while(counter<len(list_of_persons_objects)):
		list_of_persons_names.append(str(str(list_of_persons_objects[counter].name)+ " " +str(list_of_persons_objects[counter].surname)))
		counter = counter + 1

	return list_of_persons_names;  # a string with all names+surnames in the persons list

#get list of organisations from file
def get_oganisations():
	with open("organisations") as file:
	    list_of_organisations = [line.strip() for line in file]
	    file.close()
	return list_of_organisations

# print a list from a file
def print_list(filename):
		file = open(filename, "r")
		line_list = [line.strip() for line in file]
		file. close()
		line_count = len(line_list)
		counter = 0
		print("***Printing the list of file " + filename + "****")
		while(counter<line_count):
			print("*********Next Receipt*********")
			temp_receipt = make_receipt(line_list[counter])
			temp_receipt.print_info()
			counter = counter + 1


# add an income receipt from the terminal
def add_income():
	print("Entering a new income receipt..")
	temp_receipt = receipt()
	temp_receipt.user_init()
	print("Object created.Saving to file..\n")
	save_receipt(temp_receipt,"income")
	print("Done!\n")

#add an expence receipt from the terminal
def add_expense():
	print("Entering a new income receipt..")
	temp_receipt = receipt()
	temp_receipt.user_init()
	print("Object created.Saving to file..\n")
	save_receipt(temp_receipt,"expenses")
	print("Done!\n")


if(path.exists("persons")==False):
	f = open("persons", "w")	
	f.close()

if(path.exists("income")==False):
	f = open("income", "w")	
	f.close()

if(path.exists("expense")==False):
	f = open("expense", "w")	
	f.close()

my_income = get_income()
my_expenses =  get_expenses()
my_belongings = []
list_of_methods = []
list_of_persons = get_persons()
list_of_organisations = []


# a one-window implementation of the add_receipt
def graphical_add_receipt():
	# handle button events
	def press(button):
		if button == "Exit":
			receipt_graphical.stop()
		if button == "SaveAsIncome":
			temp_receipt = receipt()
			temp_receipt.amount = receipt_graphical.getEntry("Amount")
			temp_receipt.sender = receipt_graphical.getEntry("Sender")
			temp_receipt.recipient = receipt_graphical.getEntry("Recipient")
			temp_receipt.date = receipt_graphical.getEntry("Date")
			temp_receipt.method = receipt_graphical.getEntry("Method")
			temp_receipt.comments = receipt_graphical.getEntry("Commends") 
			temp_receipt.id =  receipt_graphical.getEntry("identification")
			receipt_graphical.clearAllEntries(callFunction=False)
			save_receipt(temp_receipt,"income")
			print("saved the income..\n")
			receipt_graphical.stop()
		if button == "SaveAsExpense":
			temp_receipt = receipt()
			temp_receipt.amount = receipt_graphical.getEntry("Amount")
			temp_receipt.sender = receipt_graphical.getEntry("Sender")
			temp_receipt.recipient = receipt_graphical.getEntry("Recipient")
			temp_receipt.date = receipt_graphical.getEntry("Date")
			temp_receipt.method = receipt_graphical.getEntry("Method")
			temp_receipt.comments = receipt_graphical.getEntry("Commends") 
			temp_receipt.id =  receipt_graphical.getEntry("identification")
			receipt_graphical.clearAllEntries(callFunction=False)
			save_receipt(temp_receipt,"expenses")
			print("saved the expenses..\n")
			receipt_graphical.stop()

	# create a GUI variable called receipt_graphical
	receipt_graphical = gui("Receipt Adder", "500x400")
	receipt_graphical.setBg("green")
	receipt_graphical.setFont(15)

	# add & configure widgets - widgets get a name, to help referencing them later
	receipt_graphical.addLabel("title", "Add a Receipt")

	receipt_graphical.addLabelEntry("Amount.............")
	receipt_graphical.addLabelEntry("Sender.............")
	receipt_graphical.addLabelEntry("Recipient..........")
	receipt_graphical.addLabelEntry("Date...............")
	receipt_graphical.addLabelEntry("Method.............")
	receipt_graphical.addLabelEntry("Commends...........")
	receipt_graphical.addLabelEntry("identification.....")

	# link the buttons to the function called press
	receipt_graphical.addButtons(["SaveAsIncome", "SaveAsExpense", "Exit"], press)

	receipt_graphical.setFocus("Amount.............")
	# start the GUI
	receipt_graphical.go()

# a main menu window that supports subwindows
def menu_graphical():
	def launch(win):
		app.showSubWindow(win)

	# method to house all the main_gui related buttons(such as exit)
	def main_gui_press(button):  
		if button == "Exit":
			app.stop()
		if button == "ViewReceipts":
			print_list("expenses")
			print_list("income")
			app.showSubWindow("ViewReceipts")

	app = gui("Homecon Manager", "500x400")
	app.setBg("green")
	app.setFont(12)
	app.addLabel("title","Homecon Financε Manager")
	app.setLabelBg("title","orange")

	# these go in the main window
	app.addButtons(["AddReceipt","AddPerson"], launch)

	app.addButtons(["ViewReceipts"], main_gui_press)

	app.addButtons(["Exit"],main_gui_press)


	# add receipt PopUp
	#this has all the button press functionality for subWindow 1
	def press_receipt_window(button):
		if button == "SaveAsIncome":
			temp_receipt = receipt()
			temp_receipt.amount = app.getEntry("Amount")
			temp_receipt.sender = app.getEntry("Sender")
			temp_receipt.recipient = app.getEntry("Recipient")
			temp_receipt.date = app.getEntry("Date")
			temp_receipt.method = app.getEntry("Method")
			temp_receipt.comments = app.getEntry("Comments") 
			temp_receipt.id =  app.getEntry("Id")
			save_receipt(temp_receipt,"income")
			print("saved the income..\n")
			update_receipts_output_text()
		if button == "SaveAsExpense":
			temp_receipt = receipt()
			temp_receipt.amount = app.getEntry("Amount")
			temp_receipt.sender = app.getEntry("Sender")
			temp_receipt.recipient = app.getEntry("Recipient")
			temp_receipt.date = app.getEntry("Date")
			temp_receipt.method = app.getEntry("Method")
			temp_receipt.comments = app.getEntry("Comments") 
			temp_receipt.id =  app.getEntry("Id")
			save_receipt(temp_receipt,"expenses")
			print("saved the expense..\n")
			update_receipts_output_text()

		#the subwindows never really close. They can only be hidden after use
		app.hideSubWindow("AddReceipt")

	# get a string with all the persons names to use in autocomplete 
	persons_names = get_persons_names(get_persons())


	app.startSubWindow("AddReceipt", modal=True)
	app.addLabel("l1", "Add a Receipt")
	app.addNumericEntry("Amount")  # numeric entry to force number input only
	app.addAutoEntry("Sender",persons_names)
	app.addAutoEntry("Recipient",persons_names)
	app.addEntry("Date")
	app.addAutoEntry("Method", ["cash", "bank deposit", "debit card","credit card","other"])
	app.addEntry("Comments")
	app.addEntry("Id")

	app.setEntryDefault("Amount", "The amount of money here")  # this sets the "title" inside the text field
	app.setEntryDefault("Sender","Enter who sent the money")
	app.setEntryDefault("Recipient", "Enter who received the money")
	app.setEntryDefault("Date", "Enter Date of transaction")
	app.setEntryDefault("Method", "method of payment, e.g. cash")
	app.setEntryDefault("Comments", "any comments here")
	app.setEntryDefault("Id", "please leave this empty")

	app.addButtons(["SaveAsIncome", "SaveAsExpense"], press_receipt_window)
	app.stopSubWindow()


	# show receipts sub window
	app.startSubWindow("ViewReceipts", modal=True)
	app.addMessage("output","List of Transactions:")
	app.addScrolledTextArea("output_text_area", text = None)

	def update_receipts_output_text():
		my_income = get_income()
		my_expenses = get_expenses()
		app.clearTextArea("output_text_area", callFunction=False)
		app.setTextArea("output_text_area", "Here is a list with all income:\n\n", end=True, callFunction=False)
		app.setTextArea("output_text_area", "*******************\n", end=True, callFunction=False)
		counter = 0
		while(counter<len(my_income)):
			app.setTextArea("output_text_area", my_income[counter] + "\n\n" , end=True, callFunction=False) 
			app.setTextArea("output_text_area", "*******************\n", end=True, callFunction=False)
			counter = counter + 1

		app.setTextArea("output_text_area", "Here is a list with all expense:\n", end=True, callFunction=False)
		app.setTextArea("output_text_area", "*******************\n", end=True, callFunction=False)
		counter = 0
		while(counter<len(my_expenses)):
			app.setTextArea("output_text_area", my_expenses[counter] + "\n" , end=True, callFunction=False) 
			app.setTextArea("output_text_area", "*******************\n", end=True, callFunction=False)
			counter = counter + 1

	update_receipts_output_text()

	app.stopSubWindow()


	#add person pop-Up
	def press_person_window(button):
		if button == "Cancel":
			app.hideSubWindow("AddPerson")
		if button == "SavePerson":
			temp_person = person()
			temp_person.name = app.getEntry("Name")
			temp_person.surname = app.getEntry("Surname")
			temp_person.comments = app.getEntry("person_comments")
			temp_person.id = app.getEntry("person_id")
			save_person(temp_person,"persons")
			print("saved the person..\n")
			persons_names = get_persons_names(get_persons())
			app.changeAutoEntry("Sender",persons_names)  # update the persons list live
			app.changeAutoEntry("Recipient",persons_names)
			print("updated person catalog...")
			app.hideSubWindow("AddPerson")
			#save the persons info to the file

	app.startSubWindow("AddPerson", modal=True)
	app.addLabel("title_addperson", "Add a Person")
	app.addEntry("Name")
	app.addEntry("Surname")
	app.addEntry("person_comments")
	app.addEntry("person_id")

	app.setEntryDefault("Name","Name")
	app.setEntryDefault("Surname","Surname")
	app.setEntryDefault("person_comments","Comments here")
	app.setEntryDefault("person_id","id-leave as is")
	app.addButtons(["SavePerson", "Cancel"], press_person_window)
	
	
	app.go()

# start the gui
menu_graphical()
