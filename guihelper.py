from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog

class GUI:
    def __init__(self,other):
        self._root=Tk()
        self._root.configure(background="#f4d03f")
        self._root.maxsize(400,400)
        self._root.minsize(325,420)
        self._root.title("TINDER")

        self._label1=Label(self._root,text="Tinder")
        self._label1.configure(font=("Times",25,"bold","underline"),width=10,bg="#f4d03f")
        self._label1.grid(row=1,column=1,pady=(20,20))

        self._label2 = Label(self._root, text="Email: ",bg="#f4d03f")
        self._label2.configure(font=("Constantia",14))
        self._label2.grid(row=2,column=0,pady=(3,3))

        self._emailInput=Entry(self._root)
        self._emailInput.grid(row=2,column=1,pady=(3,3),ipady=3,ipadx=30)

        self._label3 = Label(self._root, text="Password: ",bg="#f4d03f")
        self._label3.configure(font=("Constantia", 14))
        self._label3.grid(row=3,column=0,pady=(3,3))

        self._passwordInput = Entry(self._root)
        self._passwordInput.grid(row=3,column=1,pady=(3,3), ipady=4, ipadx=30)

        self._loginBtn=Button(self._root,text='Login',bg='#1e8449',fg='#ecf0f1',width=30,height=2,command=lambda:other.loginHandler(self._emailInput.get(),self._passwordInput.get()))
        self._loginBtn.grid(row=4,column=1,pady=(10,10))

        self._label4 = Label(self._root, text="Not a member?")
        self._label4.configure(font=("Constantia", 13,"bold"))
        self._label4.grid(row=6,column=1,pady=(50,10))

        self._RegBtn = Button(self._root, text='Click Here',bg='#c0392b',fg='#f4f6f7',width=10, height=2, command=lambda: self.regWindow(other))     #reference of object of class Tinder is being further passed
        self._RegBtn.grid(row=7,column=1,pady=(15,10))                                                                                              #opens the registration page

        self._root.mainloop()

    def openpic(self):
        self._root1.path = filedialog.askopenfilename(initialdir="/",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self._root1.image=ImageTk.PhotoImage(Image.open(self._root1.path))
        return self._root1.path


    def regWindow(self,other,destroy=0):
        """
                This function invokes Registration Window or destroys the Registration Window
                Date:29/01/2020
                Created By:Alekhyo
                Input:instance of tinder class
                Output:GUI screen
        """
        if(destroy==0):
            self._root1=Tk()
            self._root1.configure(background="#9b59b6")
            self._root1.maxsize(600,500)
            self._root1.minsize(400, 450)
            self._root1.title("REGISTRATION")

            self._label0 = Label(self._root1, text="Tinder")
            self._label0.configure(font=("Times", 24, "bold","underline"),width=10,bg="#9b59b6")
            self._label0.grid(row=0,column=1,pady=(30, 30))

            self._label2= Label(self._root1, text="Name:",bg="#f4d03f")
            self._label2.configure(font=("Constantia", 13))
            self._label2.grid(row=2,column=0,padx=(40,20),pady=(5,5))

            self._nameInput = Entry(self._root1)
            self._nameInput.grid(row=2,column=1,padx=(40,20),pady=(5,5),ipady=5, ipadx=20)

            self._label3 = Label(self._root1, text="Email:",bg="#f4d03f")
            self._label3.configure(font=("Constantia", 13))
            self._label3.grid(row=3,column=0,pady=(5, 5),padx=(40,20))

            self._emailInput = Entry(self._root1)
            self._emailInput.grid(row=3,column=1,padx=(40,20),pady=(5,5), ipady=7, ipadx=20)

            self._label4 = Label(self._root1, text="Password:",bg="#f4d03f")
            self._label4.configure(font=("Constantia", 13))
            self._label4.grid(row=4,column=0,pady=(5, 5),padx=(40,20))

            self._passwordInput = Entry(self._root1)
            self._passwordInput.grid(row=4,column=1,padx=(40,20),pady=(5,5), ipady=7, ipadx=20)

            self._label5 = Label(self._root1, text="Age:",bg="#f4d03f")
            self._label5.configure(font=("Constantia", 13))
            self._label5.grid(row=5, column=0, pady=(5, 5),padx=(40,20))

            self._ageInput=Entry(self._root1)
            self._ageInput.grid(row=5,column=1,padx=(40,20),pady=(5,5), ipady=7, ipadx=20)

            self._label6 = Label(self._root1, text="Gender:",bg="#f4d03f")
            self._label6.configure(font=("Constantia", 13))
            self._label6.grid(row=6, column=0, pady=(5, 5),padx=(40,20))

            clicked = StringVar(self._root1)
            clicked.set("Male")
            drop = OptionMenu(self._root1, clicked,"Male","Female","Other").grid(row=6, column=1,ipady=1,ipadx=14)

            self._label7 = Label(self._root1, text="City:",bg="#f4d03f")
            self._label7.configure(font=("Constantia", 13))
            self._label7.grid(row=7, column=0, pady=(5, 5),padx=(40,20))

            self._cityInput = Entry(self._root1)
            self._cityInput.grid(row=7,column=1,padx=(40,20),pady=(5,5), ipady=7, ipadx=20)

            self._label8 = Label(self._root1, text="Bio:",bg="#f4d03f")
            self._label8.configure(font=("Constantia", 13))
            self._label8.grid(row=8, column=0, pady=(5, 5),padx=(40,20))

            self._bioInput = Entry(self._root1)
            self._bioInput.grid(row=8,column=1,padx=(40,20),pady=(5,5), ipady=7, ipadx=20)


            self._registerBtn = Button(self._root1, text="Select Picture and Register",bg="#f4d03f", fg='#c0392b',width=10, height=2,command=lambda:other.checker(self._nameInput.get(),self._emailInput.get(),self._passwordInput.get(),self._ageInput.get(),clicked.get(),self._cityInput.get(),self._bioInput.get(),self.openpic()))
            self._registerBtn.grid(row=9,column=1,pady=(10,10),padx=(10,10),ipadx=(33))

            self._root1.mainloop()
        if destroy==1:
            self._root1.destroy()

    def clearScreenr(self):
        """
                    This function clears the GUI screen
                    Date:29/01/2020
                    Created By:Alekhyo
                    Input: ---
                    Output: ----
        """
        for i in self._root.pack_slaves():
            i.destroy()

    def clearScreeng(self):
        """
                            This function clears the GUI screen
                            Date:29/01/2020
                            Created By:Alekhyo
                            Input: ---
                            Output: ----
        """
        for i in self._root.grid_slaves():
            i.destroy()

    def headermenu(self,other,user_id,data_own):
        """
                            This function invokes header menus
                            Date:29/01/2020
                            Created By:Alekhyo
                            Input: tuple
                            Output: GUI output
        """
        menu = Menu(self._root,activebackground="#f39c12")
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command=lambda:other.doLogin(user_id,data_own))
        filemenu.add_command(label="Edit Profile", command=lambda: self.mainWindow(other,user_id,data_own,mode=4,num=0))
        filemenu.add_command(label="View Profile", command=lambda: other.viewUsers(0,user_id,mode=0))
        filemenu.add_command(label="LogOut", command=lambda: self.mainWindow(other,user_id,data_own,mode=5))

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="Received", command=lambda: self.proposalWindow(other,user_id,data_own,mode=1,num=0))
        helpmenu.add_command(label="Sent", command=lambda: self.proposalWindow(other,user_id,data_own,mode=2,num=0))
        helpmenu.add_command(label="Matches", command=lambda: self.proposalWindow(other,user_id,data_own,mode=3,num=0))

    def mainWindow(self,other,user_id,data_own,mode,num=0):
        """
                            This function invokes the Main Window
                            Date:29/01/2020
                            Created By:Alekhyo
                            Input: tuples
                            Output: GUI output
        """
        self.clearScreenr()
        self.clearScreeng()
        self.headermenu(other,user_id,data_own)

        data = other._dbObject.get_details(user_id)

        if(mode==0):
            imageUrl = data_own[0][6]
            load = Image.open(imageUrl)
            load = load.resize((200, 200), Image.ANTIALIAS)

            render = ImageTk.PhotoImage(load)

            img = Label(image=render)
            img.image = render
            img.grid(row=0, column=2, rowspan=2, columnspan=2)

            self._label1 = Label(self._root, text="Name: ", bg="#f4d03f")
            self._label1.configure(font=("Times", 17))
            self._label1.grid(row=2, column=2)

            name = data_own[0][1]
            self._label2 = Label(self._root, text=name.upper(), bg="#f4d03f", fg="#c0392b")
            self._label2.configure(font=("Helvetica", 13))
            self._label2.grid(row=2, column=3)

            self._label3 = Label(self._root, text="Age: ", bg="#f4d03f")
            self._label3.configure(font=("Times", 17))
            self._label3.grid(row=3, column=2)

            age = str(data_own[0][4])
            self._label4 = Label(self._root, text=age, bg="#f4d03f", fg="#c0392b")
            self._label4.configure(font=("Helvetica", 13))
            self._label4.grid(row=3, column=3)

            self._label5 = Label(self._root, text="Gender: ", bg="#f4d03f")
            self._label5.configure(font=("Times", 17))
            self._label5.grid(row=4, column=2)

            gender = data_own[0][5]
            self._label6 = Label(self._root, text=gender.upper(), bg="#f4d03f", fg="#c0392b")
            self._label6.configure(font=("Helvetica", 13))
            self._label6.grid(row=4, column=3)

            self._label7 = Label(self._root, text="City: ", bg="#f4d03f")
            self._label7.configure(font=("Times", 17))
            self._label7.grid(row=5, column=2)

            city = data_own[0][7]
            self._label8 = Label(self._root, text=city.upper(), bg="#f4d03f", fg="#c0392b")
            self._label8.configure(font=("Helvetica", 13))
            self._label8.grid(row=5, column=3)

            self._label9 = Label(self._root, text="Bio: ", bg="#f4d03f")
            self._label9.configure(font=("Times", 17))
            self._label9.grid(row=6, column=2)

            bio = data_own[0][8]
            self._label10 = Label(self._root, text=bio.upper(), bg="#f4d03f", fg="#c0392b")
            self._label10.configure(font=("Helvetica", 13))
            self._label10.grid(row=6, column=3)
        if (mode == 1):
            imageUrl = data[0][6]
            load = Image.open(imageUrl)
            load = load.resize((200, 200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)

            img = Label(image=render)
            img.image = render
            img.grid(row=0, column=2, rowspan=2, columnspan=2)

            self._label1 = Label(self._root, text="Name: ", bg="#f4d03f")
            self._label1.configure(font=("Times", 17))
            self._label1.grid(row=2, column=2)

            name = data[0][1]
            self._label2 = Label(self._root, text=name.upper(), bg="#f4d03f", fg="#c0392b")
            self._label2.configure(font=("Helvetica", 13))
            self._label2.grid(row=2, column=3)

            self._label3 = Label(self._root, text="Age: ", bg="#f4d03f")
            self._label3.configure(font=("Times", 17))
            self._label3.grid(row=3, column=2)

            age = str(data[0][4])
            self._label4 = Label(self._root, text=age, bg="#f4d03f", fg="#c0392b")
            self._label4.configure(font=("Helvetica", 13))
            self._label4.grid(row=3, column=3)

            self._label5 = Label(self._root, text="Gender: ", bg="#f4d03f")
            self._label5.configure(font=("Times", 17))
            self._label5.grid(row=4, column=2)

            gender = data[0][5]
            self._label6 = Label(self._root, text=gender.upper(), bg="#f4d03f", fg="#c0392b")
            self._label6.configure(font=("Helvetica", 13))
            self._label6.grid(row=4, column=3)

            self._label7 = Label(self._root, text="City: ", bg="#f4d03f")
            self._label7.configure(font=("Times", 17))
            self._label7.grid(row=5, column=2)

            city = data[0][7]
            self._label8 = Label(self._root, text=city.upper(), bg="#f4d03f", fg="#c0392b")
            self._label8.configure(font=("Helvetica", 13))
            self._label8.grid(row=5, column=3)

            self._label9 = Label(self._root, text="Bio: ", bg="#f4d03f")
            self._label9.configure(font=("Times", 17))
            self._label9.grid(row=6, column=2)

            bio = data[0][8]
            self._label10 = Label(self._root, text=bio.upper(), bg="#f4d03f", fg="#c0392b")
            self._label10.configure(font=("Helvetica", 13))
            self._label10.grid(row=6, column=3)

        if(mode==2):
            self.mainWindow(other,user_id, data_own,mode=0)
            self._frame = Frame(self._root,bg="#f4d03f")
            self._frame.grid(row=7,column=1,columnspan=5,pady=(10,10))
            self._btn1 = Button(self._frame, text="Previous", fg="#fff", bg="#fd5068",command=lambda:other.viewUsers(num-1,user_id))
            self._btn1.grid(row=7,column=1,padx=(0,6))
            self._btn2 = Button(self._frame, text="Propose", fg="#fff", bg="#fd5068",command=lambda :other.propose(data_own[0][0]))
            self._btn2.grid(row=7,column=3,padx=(0,6))
            self._btn3 = Button(self._frame, text="Next", fg="#fff", bg="#fd5068",command=lambda:other.viewUsers(num+1,user_id))
            self._btn3.grid(row=7,column=5,padx=(0,6))

        if(mode==3):
            self.mainWindow(other,user_id,data_own,mode=0)
            self._frame=Frame(self._root)
            self._frame.grid(row=8,column=3)

            self._deleteBtn=Button(self._frame,text="Delete Account",command=lambda:other.deleteHandler(data_own))
            self._deleteBtn.grid(row=0,column=0)

        if(mode==4):

            self._label1 = Label(self._root, text="Name: ")
            self._label1.configure(font=("Constantia", 17),bg="#f4d03f")
            self._label1.grid(row=1, column=0)

            self._nameEdit = Entry(self._root)
            self._nameEdit.grid(row=1, column=1)

            self._label2 = Label(self._root, text="Age: ",bg="#f4d03f")
            self._label2.configure(font=("Constantia", 17))
            self._label2.grid(row=2, column=0)

            self._ageEdit = Entry(self._root)
            self._ageEdit.grid(row=2, column=1)

            self._label3 = Label(self._root, text="Gender: ",bg="#f4d03f")
            self._label3.configure(font=("Constantia", 17))
            self._label3.grid(row=3, column=0)

            clicked = StringVar(self._root)
            clicked.set("Male")
            drop = OptionMenu(self._root, clicked, "Male", "Female", "Other").grid(row=3, column=1, ipady=1, ipadx=14)

            self._label4 = Label(self._root, text="City: ",bg="#f4d03f")
            self._label4.configure(font=("Constantia", 17))
            self._label4.grid(row=4, column=0)
            
            self._cityEdit = Entry(self._root)
            self._cityEdit.grid(row=4, column=1)

            self._label5 = Label(self._root, text="Bio: ",bg="#f4d03f")
            self._label5.configure(font=("Constantia", 17))
            self._label5.grid(row=5, column=0)

            self._bioEdit = Entry(self._root)
            self._bioEdit.grid(row=5, column=1)

            self._frame1 = Frame(self._root,background="#f4d03f")
            self._frame1.grid(row=7, column=1)



            self._editBTN = Button(self._frame1, text="EDIT",fg='blue',command=lambda: other.updateHandler(data_own[0][0], self._nameEdit.get(), self._ageEdit.get(),clicked.get(), self._cityEdit.get(),self._bioEdit.get(),'users'))
            self._editBTN.grid(row=0, column=0,pady=(10,10),padx=(10,10))

            self._frame2 = Frame(self._root,background="#f4d03f")
            self._frame2.grid(row=8, column=1)
            self._deleteBtn = Button(self._frame2, text="Delete Account",fg='red', command=lambda: self.mainWindow(self,user_id,data_own,mode=3,num=0))
            self._deleteBtn.grid(row=0, column=0,pady=(10,10),padx=(10,10))

        if mode==5:
            self.mainWindow(other,user_id,data_own,mode=6)
            self.__init__()

        if mode==6:
            self._root.destroy()

        if mode==7:
            self.mainWindow(other,user_id,data_own,mode=0)

            self._frame = Frame(self._root,background="#f4d03f")
            self._frame.grid(row=8, column=1, columnspan=3, rowspan=3,pady=(15,15))

            self._btn1 = Button(self._frame, text="Previous", fg="#fff", bg="#fd5068",command=lambda: other.viewUsers(num - 1,user_id,mode=1))
            self._btn1.grid(row=8, column=1,padx=(0,8))

            self._btn3 = Button(self._frame, text="Next", fg="#fff", bg="#fd5068",command=lambda: other.viewUsers(num + 1,user_id,mode=1))
            self._btn3.grid(row=8, column=3,padx=(0,8))

        if mode==8:
            self.mainWindow(other,user_id,data_own,mode=0)

            self._frame = Frame(self._root,background="#f4d03f")
            self._frame.grid(row=8, column=1, columnspan=3, rowspan=3,pady=(15,15))

            self._btn1 = Button(self._frame, text="Previous", fg="#fff", bg="#fd5068",command=lambda: other.viewUsers(num - 1,user_id,mode=2))
            self._btn1.grid(row=8, column=1,padx=(0,8))

            self._btn3 = Button(self._frame, text="Next", fg="#fff", bg="#fd5068",command=lambda: other.viewUsers(num + 1,user_id,mode=2))
            self._btn3.grid(row=8, column=3,padx=(0,8))

        if mode==9:
            self.mainWindow(other,user_id,data_own,mode=0)

            self._frame = Frame(self._root,background="#f4d03f")
            self._frame.grid(row=8, column=1, columnspan=3, rowspan=3,pady=(15,15))

            self._btn1 = Button(self._frame, text="Previous", fg="#fff", bg="#fd5068",command=lambda: other.viewUsers(num - 1,user_id,mode=3))
            self._btn1.grid(row=8, column=1,padx=(0,8))

            self._btn3 = Button(self._frame, text="Next", fg="#fff", bg="#fd5068",command=lambda: other.viewUsers(num + 1,user_id,mode=3))
            self._btn3.grid(row=8, column=3,padx=(0,8))

    def proposalWindow(self,other,user_id,data_own,num,mode):
        """
                            This function displays sent/received/matches
                            Date:29/01/2020
                            Created By:Alekhyo
                            Input: tuples,mode
                            Output: GUI output
        """

        self.clearScreeng()
        self.headermenu(other,user_id,data_own)
        if mode==1:
            other.proposalHandler(user_id,data_own,num,mode=mode)
        elif mode==2:
            other.proposalHandler(user_id,data_own,num,mode=mode)
        else:
            other.proposalHandler(user_id,data_own,num,mode=mode)


    def printMessage(self, title, message,mode):
        """
                            This function displays several messages
                            Date:29/01/2020
                            Created By:Alekhyo
                            Input: mode
                            Output: GUI output
        """
        master = Tk()
        master.withdraw()
        if(mode==0):
            messagebox.showerror(title, message)
        if(mode==1):
            return(messagebox.askquestion(title,message))
        if(mode==2):
            messagebox.showinfo(title,message)