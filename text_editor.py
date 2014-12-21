from tkinter import *
from tkinter import scrolledtext

def printSomething():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

def openFile():
    file object

def menuOpen():
    fileOpen = Toplevel(root)
    label = Label(fileOpen, text="Open file:")
    entry = Entry(fileOpen, text ="")
    button = Button(fileOpen, text="Open", command = openFile)
    label.pack(side = LEFT)
    entry.pack(side = LEFT)
    button.pack(side = LEFT)

    
def exitApp():
    root.destroy()

root = Tk()
text = scrolledtext.ScrolledText(root)
text.insert(INSERT, "Hello...")
text.insert(END, "BYE BYE....")
text.pack()

#main menubar
menubar = Menu(root)

#File menu in the menubar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = "New File", command = printSomething)
filemenu.add_command(label = "Open...", command=menuOpen)
filemenu.add_separator()
filemenu.add_command(label = "Save", command=printSomething)
filemenu.add_command(label = "Save as...", command=printSomething)
filemenu.add_separator()
filemenu.add_command(label = "Quit", command=exitApp)
menubar.add_cascade(label = "File", menu = filemenu)


root.config(menu = menubar)

root.mainloop()
