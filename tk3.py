from tkinter import *
win=Tk()
win.geometry('500x400+400+200')
win.configure(bg='powder blue')
win.title('Ducat')
win.resizable(width=False,height=False)
b1=Button(win,text='Button-1')
b2=Button(win,text='Button-2')

b1.pack() #side='top',anchor='c'
b2.pack() #side='top',anchor='c'

win.mainloop() 
