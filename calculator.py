from tkinter import *
from tkinter import ttk

class Calculator(ttk.Frame):
    def __init__(self,parent,**kwargs):
        ttk.Frame.__init__(self,parent,height=kwargs['height'],width=kwargs['width'])


class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculator")
        self.geometry("272x300")
        self.Calculator=Calculator(self,height=300,width=200)
        self.Calculator.place(x=0,y=0)

    def start(self):
        self.mainloop()

if __name__=='__main__':
    app=MainApp()
    app.start()