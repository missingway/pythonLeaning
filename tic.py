from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("三子棋")
root.geometry("600x610")
root.resizable(width=False,height=False)

class App(Frame):
	def __init__ (self,mester):
		super(App,self).__init__(mester)
		self.configure(bg='orange')
		self.grid()
		self.file()
	def file(self):
		self.lbl=Label(self,text="您选X还是O",font = ('Helvetica', '16'),bg="orange",fg="white",pady=10)
		self.lbl.grid(row=0,column=1,columnspan=3,sticky=W,padx=75)
		self.x_bttn=Button(self,text="X",width=10,height=3,background='silver',font = ('Helvetica', '12'))
		self.x_bttn.grid(row=1,column=1,columnspan=1,sticky=W)
		self.o_bttn=Button(self,text="O",width=10,height=3,bg='silver',font = ('Helvetica', '12'))
		self.o_bttn.grid(row=1,column=2,columnspan=1,sticky=W)
		self.board=[]
		self.buttons=[]
		for x in range(0,9):
			self.board.append("")
			self.buttons.append(Button(self,text="",width=27,height=9,background='black'))
			self.buttons[x].grid(row=x//3+2,column=x%3,columnspan=1,sticky=W)
			self.buttons[x].bind("<ButtonPress-1>",lambda event, index=x: self.go(event, index))
	
	def go(self,event,index):
		print(index)



app=App(root)
root.mainloop()
