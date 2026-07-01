from tkinter import *

cal_root = Tk()

#Wihth X Height
cal_root.geometry("")

# Widget , height
cal_root.wm_minsize(200 , 100) #minimum

cal_root.maxsize(1000,1000) # maximum

a = Label(text="Calculator")
a.pack()

cal_root.mainloop()