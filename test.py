from appJar import gui 

def launch(win):
    app.showSubWindow(win)

app=gui()

# these go in the main window
app.addButtons(["one", "two"], launch)

#this has all the button press functionality for subWindow 1
def press_1(button):
	if button == "TestExit":
		print(app.getEntry("TestEntry"))

# this is a pop-up
app.startSubWindow("one", modal=True)
app.addLabel("l1", "SubWindow One")
app.addLabelEntry("TestEntry")
app.addButtons(["TestExit"], press_1)
app.stopSubWindow()

# this is another pop-up
app.startSubWindow("two")
app.addLabel("l2", "SubWindow Two")
app.stopSubWindow()

app.go()
