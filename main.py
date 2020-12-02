
class receipt:
	def __init__(self,amount,recipient,date,method,comments,id):
		self.amount = amount
		self.recipient = recipient
		self.date = date
		self.method = method
		self.comments = comments
		self.id = 0
	def print_info(self):
		print("Amount:" + str(self.amount))
		print("Recipient:" + str(self.recipient))
		print("Date:" + str(self.date))
		print("Method of Payment:" + str(self.method))
		print("Comments:" + str(self.comments))
		print("ID Number:" + str(self.id))


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
		savefile.write("\n")
		savefile.write(line_to_save)
		savefile.close()

# Method to take a string with comma seperated values and create a receipt object out of it
# used to get receipt objects saved in the main memory
def make_receipt(string):
	attr = string.split(",")  #split comma seperate elements
	temp_receipt = receipt(attr[0],attr[1],attr[2],attr[3],attr[4],attr[5])  # make a receipt object with these attributes
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


my_income = []
my_expenses = []
my_belongings = []
list_of_methods = []
list_of_persons = []
list_of_organisations = []



receipt1 = receipt("15","nikos","simera","cash","no_comment","459")

save_receipt(receipt1,"expenses.txt")

my_expenses = get_expenses()
print(my_expenses)



try_receipt = make_receipt("15,nikos,16/10/1999,cash,no comment,0")
try_receipt.print_info()




