from tkinter import *
from search import search

root = Tk()

choice = StringVar()
Label(root, text = 'Enter movie name below').grid(row = 0, column = 0, padx = 6, pady = 6)
box = Entry(root, textvariable = choice)
box.grid(row = 1, column = 0, padx = 6, pady = 6)






btn = Button(root, text = 'Search', command=lambda : search(choice.get()))
btn.grid(row = 0, column = 1, padx = 6, pady = 6)

root.mainloop()
