import tkinter

window = tkinter.Tk()
window.title("Akash")
window.geometry('500x400+400+200')
window.configure(bg='#80cbc4')

login = tkinter.Button(window, text='login')
reset = tkinter.Button(window, text='reset')

login.pack(side='top', anchor='e')
window.mainloop()