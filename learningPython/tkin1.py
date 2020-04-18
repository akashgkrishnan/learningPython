import tkinter

window = tkinter.Tk()
window.geometry('500x400+400+300')
window.title('Akash')
window.configure(bg='red')
b1 = tkinter.Button(window, text='New')
b1.pack(side='bottom', anchor='se')

b1 = tkinter.Button(window, text='amma')
b1.pack(side='top', anchor='e')


b3 = tkinter.Button(window, text='akash')
b3.pack(side='top', anchor='w')

b2 = tkinter.Button(window, text='akhila')
b2.pack(side='right')

window.mainloop()
