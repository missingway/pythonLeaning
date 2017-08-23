from tkinter import *

root=Tk()
root.title("三子棋")
root.geometry("590x610")
root.resizable(width=False,height=False)

class App(Frame):
	def __init__ (self,mester):
		super(App,self).__init__(mester)
		self.configure(bg='orange')
		self.person=''
		self.pc=''
		self.begin=''
		self.turn=''
		self.best_moves=(4,0,2,6,8,1,3,5,7)
		self.grid()
		self.main()

	def main(self):
		self.initBoard()
		if self.turn=="person":
			pass
		else:
			self.pcmove()

	def pcmove(self):
		for x in self.best_moves:
			if self.board[x] =="":
				self.board[x]=self.pc
				self.turn='person'
				break

	def initBoard(self):
		self.lbl=Label(self,text="您选X还是O",font = ('Helvetica', '16'),bg="orange",fg="white",pady=10)
		self.lbl.grid(row=0,column=1,columnspan=3,sticky=W,padx=75)
		self.x_bttn=Button(self,text="X",width=10,height=3,background='silver',font = ('Helvetica', '12'))
		self.x_bttn.grid(row=1,column=1,columnspan=1,sticky=W)
		self.x_bttn.bind("<ButtonPress-1>",lambda event,f="X":self.start(event,f))
		self.o_bttn=Button(self,text="O",width=10,height=3,bg='silver',font = ('Helvetica', '12'))
		self.o_bttn.grid(row=1,column=2,columnspan=1,sticky=W)
		self.o_bttn.bind("<ButtonPress-1>",lambda event,i="O":self.start(event,i))
		self.board=[]
		self.buttons=[]
		for x in range(0,9):
			self.board.append("")
			self.buttons.append(Button(self,text="",width=6,height=2,background='black',fg='white',font = ('Helvetica', '40')))
			self.buttons[x].grid(row=x//3+2,column=x%3,columnspan=1,sticky=W)
			self.buttons[x].bind("<ButtonPress-1>",lambda event, index=x: self.personmove(event, index))
	
	def personmove(self,event,index):
		if self.board[index]=='' and self.turn=='person':
			self.board[index]=self.person
			self.buttons[index].configure(text=self.person)
			self.turn='pc'
		print(self.board)

	def start(self,event,l):
		if l=="X":
			self.begin=l
			self.person="X"
			self.pc="O"
			self.turn='person'
		else:
			self.begin=l
			self.person="O"
			self.pc="X"
			self.turn='pc'






app=App(root)
root.mainloop()
