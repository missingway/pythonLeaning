from tkinter import *
root=Tk()
root.title("江哥的GUI")
root.geometry("500x300")
class App(Frame):
    def __init__(self, master):
        super(App,self).__init__(master)
        self.grid()
        self.file()
    def file(self):
        self.lbl=Label(self, text="输入密码，我就会告诉你一条武林秘诀")
        self.lbl.grid(row=0,column=0,columnspan=3,sticky=W)
        self.psw_lbl=Label(self, text="密码：")
        self.psw_lbl.grid(row=1,column=0,columnspan=1,sticky=W)
        self.psw_ent=Entry(self)
        self.psw_ent.grid(row=1,column=1,columnspan=1,sticky=W)
        self.mima_bttn=Button(self,text="提交",command = self.reveal)
        self.mima_bttn.grid(row=2,column=0,columnspan=1,sticky=W)
        self.secret_txt=Text(self,width=60,height=12,wrap=WORD)
        self.secret_txt.grid(row=3,column=0,columnspan=3,sticky=W)
    def reveal(self):
        contents = self.psw_ent.get()
        if contents == "师傅，请教我武林秘诀":
            message="吸气--呼气--，提臀，放屁。方圆百里，芸芸众生，不复存在。"
        else:
            message="你的功底还没达到取得此秘诀的境界，等修炼好了再来吧"
        self.secret_txt.delete(0.0,END)
        self.secret_txt.insert(0.0,message)
        
app = App(root)
root.mainloop()

