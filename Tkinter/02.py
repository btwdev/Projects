from tkinter import *
from PIL import Image , ImageTk

a_root = Tk()

a_root.geometry("720x1080")
# photo = PhotoImage(file="1.png")

# for jpeg image
image = Image.open(r"Tkinter\photo.jpeg")
photo = ImageTk.PhotoImage(image)


b_label = Label(a_root,image=photo)
b_label.pack()


a_root.mainloop()


