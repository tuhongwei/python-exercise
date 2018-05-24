#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
	"""docstring for Application"""
	def __init__(self, master=None):
		super(Application, self).__init__(master)#or Frame.__init__(self,master)
		self.pack()
		self.createWidgets2()
	def createWidgets1(self):
		self.helloLabel = Label(self,text='Hello World!')
		self.helloLabel.pack()
		self.quitButton = Button(self,text='Quit',command=self.quit)
		self.quitButton.pack()
	def createWidgets2(self):
		self.nameInput = Entry(self,text='world')
		self.nameInput.pack()
		self.alertButton = Button(self,text='Hello',command=self.hello)
		self.alertButton.pack()
	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message','Hello %s' % name)
app = Application()
app.master.title('Hello world')
app.mainloop()	