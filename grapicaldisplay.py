from detective import SherlockHolmes
from tkinter import *
from tkinter import messagebox
class guiDisplay:
	def __init__(self,content):
		self.valueIwannafind = ""
		self.content = content
		# variable to store data from the detective
		self.ContentFoundBydetective = []

	def callThedetectiveJuan(self):
		detectiveHomes  = SherlockHolmes(self.content,self.valueIwannafind.get())
		detectiveHomes.findByphone()
		if len(detectiveHomes.givebackValue()) > 0:
			self.ContentFoundBydetective.append(detectiveHomes.givebackValue())
			self.showContentFound()


	def displaySearch(self):
		Label(text="        ", width=30).grid(row=1, column=1)
		Label(text="        ", width=30).grid(row=1, column=2)
		self.valueIwannafind = Entry(text="valueToCheck", width=30)
		self.valueIwannafind.grid(row=2, column=1)
		Button(text="find",width=25 , command = self.callThedetectiveJuan).grid(row=2, column=2)
		Label(text="        ", width=30).grid(row=3, column=1)
		Label(text="        ", width=30).grid(row=3, column=2)

	def showContentFound(self):
		messagebox.showinfo("Info", self.ContentFoundBydetective)


