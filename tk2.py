from tkinter import *
win=Tk()
win.geometry('500x400+400+200')
win.configure(bg='powder blue')
win.title('Ducat')
win.resizable(width=False,height=False)
b1=Button(win,text='Button-1')
b1.pack(side='top',anchor='c',pady=10,ipadx=30,ipady=30)

b2=Button(win,text='Button-2')
b2.pack(side='top',anchor='c',pady=10)

b3=Button(win,text='Button-3')

b4=Button(win,text='Button-4')
b5=Button(win,text='Button-5')
b6=Button(win,text='Button-6')

b4.pack(side='left',anchor='c',padx=10)
b5.pack(side='left',anchor='c')

win.mainloop() 
