from tkinter import *
import math
root = Tk()
root.title("计算器")
root.geometry("400x360")
root.resizable(width=False,height=False)

class Application(Frame):
    def __init__ (self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.file()
        self.p=""
    
    def cal(self,event,index):
        i = math.floor(index/4)
        j = index%4
        text = self.myList[i][j]
        if text=="=":
            try:
                r=eval(self.dankuang_ent.get())
                self.dankuang_ent.delete(0,END)
                self.dankuang_ent.insert(END,str(r))
                self.p=r
            except:
                self.dankuang_ent.delete(0,END)
                self.dankuang_ent.insert(END,'亲，无法运算')

        elif text=="AC":
            self.dankuang_ent.delete(0,END)
        elif text=="CE":
            h=str(self.dankuang_ent.get())
            d=h[0:-1]
            self.dankuang_ent.delete(0,END)
            self.dankuang_ent.insert(END,d)
        elif text=="ANS":
            self.dankuang_ent.insert(END,str(self.p))
        else:
            self.dankuang_ent.insert(END,text)
                       
        
        
    def file(self):
        self.buttons = []
        self.dankuang_ent=Entry(self,width=33,font = ('Helvetica', '16'),justify=RIGHT)
        self.dankuang_ent.grid(row=0,column=0,columnspan=4,sticky=W)
        self.myList = [['AC','CE','%','/'],['7','8','9','*'],['4','5','6','-']
                  ,['1','2','3','+'],['.','0','ANS','=']]
        for i in range(0,5):
            for j in range(0,4):
              self.buttons.append(Button(self,text=self.myList[i][j],width=10,height=3))
              self.buttons[i*4+j].bind("<ButtonPress-1>", lambda event, index=i*4+j: self.cal(event, index))
              self.buttons[i*4+j].grid(row=i+1,column=j,columnspan=1,sticky=W)  

            
        
app=Application(root)       
root.mainloop()
