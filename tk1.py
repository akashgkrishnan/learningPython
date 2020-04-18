#tkinter is the part of standard python library,we need not to download it seperately.(in windows)
from tkinter import *
win=Tk()
#win.geometry('500x400')
win.state('zoomed')
win.configure(bg='powder blue')
win.title('Ducat')
win.resizable(width=False,height=False)
win.mainloop() #run the window inside infinite loop so that it can be visible to user

'''
Note:
  In Idle,mainloop() is optional as it is provided by idle itself incase of window programming
'''
  
