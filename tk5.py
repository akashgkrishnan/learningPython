from tkinter import *
win=Tk()
win.geometry('500x400+400+200')
win.configure(bg='powder blue')
win.title('Ducat')
win.resizable(width=False,height=False)
b1=Button(win,text='Button-1')
b2=Button(win,text='Button-2')
b3=Button(win,text='Button-3')
b4=Button(win,text='Button-4')
b5=Button(win,text='Button-5')
b6=Button(win,text='Button-6')
b1.grid(row=0,column=0,padx=10,pady=10)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2,padx=10,pady=10)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)


win.mainloop() 
