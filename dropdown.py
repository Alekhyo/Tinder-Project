from tkinter import *
root=Tk()

clicked=StringVar()
clicked.set('Male')
drop=OptionMenu(root,clicked,'Male','Female','Other').grid(row=1,column=1)

mybutton=Button(root,text="select",command=lambda: print(clicked.get())).grid(row=2,column=1)

root.mainloop()


