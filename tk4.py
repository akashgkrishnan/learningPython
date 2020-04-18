from tkinter import *
win=Tk()
win.geometry('500x400+400+200')
win.configure(bg='powder blue')
win.title('Ducat')
win.resizable(width=False,height=False)
b1=Button(win,text='ok' ,width=10)
b2=Button(win,text='submit',width=10)
b1.place(x=100,y=100)
b2.place(x=100,y=200) 

win.mainloop() 
