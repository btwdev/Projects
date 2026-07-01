from tkinter import *
root = Tk()

root.geometry("635x556")
root.title("My gui with harry")

# Importance of label option
# text = add the text
# bd = background
# fg = foreground
# padx = x padding
# pady = x padding
# relief = border styling - SUNKEN , RAISED , GROOVE , RIDGE




title_label = Label(text='''Wikipedias fundamental principles are summarized in its five pillars. While the Wikipedia \ncommunity has developed many policies and guidelines, new editors do not\n need to be familiar with them before they start contributing.
Anyone can edit Wikipedia's text, data, references, and images.\n The quality of content is more important than the expertise of who contributes it. Wikipedia's content must conform with its policies, including being verifiable by published\n reliable sources. Contributions based on personal opinions, beliefs, or personal experiences, unreviewed research, libellous material, and copyright violations are not allowed, \nand will not remain. Wikipedia's software makes it easy to reverse errors, and experienced editors watch and patrol bad edits.\n

Wikipedia differs from printed references in important ways. Anyone can instantly improve it, add quality informa\ntion, remove misinformation, and fix errors and vandalism. Since Wikipedia is continually updated, encyclopedic articles on major news events appear within minutes.\n
For over 24 years, editors have volunteered their time and talents to create history's most comprehensive encyclopedia while providing references and other\n resources to researchers worldwide (see Researching with Wikipedia). In summary, Wikipedia has tested the wisdom of the crowd since 2001 and has found that it succeeds\n''', bg = "green",fg="white",padx=113,pady=72,font="comicsansms 12 bold", borderwidth=3,relief=SUNKEN)

title_label.pack(side=BOTTOM,anchor="sw")

root.mainloop()