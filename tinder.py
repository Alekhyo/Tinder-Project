import guihelper
import dbhelper
from tkinter import *
from tkinter import messagebox

class Tinder(guihelper.GUI,dbhelper.DBHelper):
    def __init__(self):
        self._dbObject=dbhelper.DBHelper()
        super().__init__(self)    #we are passing object of class Tinder which is received in guihelper

    # we are passing reference of loginHandler,regHandler(not the funtions actually) to the parent class so that it can be used
    #super().__init__(self.loginHandler,self.regHandler,self.updateHandler)----> using this process we had to pass the reference of all the funtions(very tiring)
    # constructor is used to automatically invoke some functionality of the application without the users concern
    # super keyword is used by child class to invoke GUI(parent class) ka constructor
    # constructor of GUI class has a code which displays opens login window
    # we are initialising an object of dbhelper which automatically invokes the constructor of dbhelper which has a code which automatically connects to the server


    def loginHandler(self,*args):
    #loginHandler receives the email and password which is given in GUI
    #We use the .get() to fetch the email and password from GUI and put into loginHandler
    #guihelper needs the loginHandler function so we pass the reference of this function as parent class cannot inherit child class


        response=self._dbObject.search('email',args[0],'password',args[1],'users',mode=0)

        #print(response)   [(1, 'salman', 'bhai@gmail.com', 'katrina', 54, 'male', 'salman.jpg', 'mumbai', 'being human')]
        if len(response) == 0:
                self.printMessage("Invalid Login", "Please provide correct credentials",mode=0)

        else:
                self.user_id=response[0][0]   #stores the user_id as it is unique(primary key)
                self.doLogin(self.user_id,response)

                #self.mainWindow(response,self.updateHandler)
                # #takes you to a new window where you can see other profiles

    #response is a list of tuples where each tuple is information of each user like [('1','salman','bhai@gmail.com',.......),('2','virat',.....),....]
    #ekta user hole ekta tuple hobe
    #Judi bhul credentials thake tahole no user thakle empty list ashbe i.e len(list)=0

    def checker(self,name,email,password,age,gender,city,bio):
        age_verify=int(age)
        valid_name=''
        if name=='' or email=='' or password=='' or age=='' or city=='':
                self.printMessage("Try","Fill all the details properly",mode=0)
        elif(age_verify<18):
                self.printMessage("Sorry", "You're not an adult.\nYou can't register with us.", mode=0)
        else:
                for i in name:
                    if ord(i) == 32:
                        pass
                    else:
                        valid_name = valid_name + i

                if (valid_name.isalpha() == True):
                    if ('@' in email) and ('.' in email):
                            response=self._dbObject.search(name,email,password,age,gender,city,bio,mode=1)

                            if len(response)==0:
                                insertion=self.regHandler(name,email,password,age,gender,city,bio)
                                if(insertion==1):
                                    answer=self.printMessage("Successful","Registered.Do you wish to login?",mode=1)
                                    if(answer=='yes'):
                                        self.loginHandler(email,password)
                                        self.regWindow(self, destroy=1)
                                    else:
                                        self.regWindow(self,destroy=1)
                                else:
                                    self.printMessage("Sorry","Due to technical problems we can't register",mode=0)
                            else:
                                self.printMessage("Retry","This email is already registered with us",mode=0)
                    else:
                        self.printMessage("Retry","Enter a valid email",mode=0)
                else:
                    self.printMessage("Retry", "Enter a valid name", mode=0)

    def doLogin(self,user_id,data_own):

        self.mainWindow(self,user_id,data_own,mode=1)

    def viewUsers(self,num,user_id,mode=0):
        if mode==0:
            details=[]
            response=self._dbObject.search('user_id',user_id,'users','NOT LIKE',mode=2)

            if num<0:
                self.printMessage("Error","No User found",mode=0)
            elif num>len(response)-1:
                self.printMessage("Error","No User found",mode=0)
            else:
                x=response[num]
                details.append(x)
                self.mainWindow(self,user_id,details,mode=2,num=num)

        elif mode==1:
            response = self._dbObject.search('romeo_id', 'juliet_id', self.user_id, 'proposals', mode=3)
            if num < 0:
                self.printMessage("Error", "No User found", mode=0)
            elif num > len(response) - 1:
                self.printMessage("Error", "No User found", mode=0)
            else:
                identity = response[num][0]
                details = self._dbObject.search('user_id', identity, 'users', 'LIKE', mode=2)
                self.mainWindow(self,user_id,details,mode=7, num=num)

        elif mode==2:
            response = self._dbObject.search('juliet_id', 'romeo_id', self.user_id, 'proposals', mode=3)
            if num < 0:
                self.printMessage("Error", "No User found", mode=0)
            elif num > len(response) - 1:
                self.printMessage("Error", "No User found", mode=0)
            else:
                identity = response[num][0]
                details = self._dbObject.search('user_id', identity, 'users', 'LIKE', mode=2)
                self.mainWindow(self,user_id,details,mode=8, num=num)

        else:
            matches=[]
            response1 = self._dbObject.search('romeo_id', 'juliet_id', self.user_id, 'proposals', mode=3)
            response2 = self._dbObject.search('juliet_id', 'romeo_id', self.user_id, 'proposals', mode=3)

            if len(response1) != 0 and len(response2) == 0:
                self.printMessage("Error", "No Matches found", mode=0)

            elif len(response2) != 0 and len(response1) == 0:
                self.printMessage("Error", "No Matches found", mode=0)
            else:
                for i in response1:
                    for j in response2:
                        if i[0]==j[0]:
                            matches.append(i[0])
                        else:
                            pass

                if len(matches) == 0:
                    self.printMessage("Error", "No Matches found", mode=0)
                else:
                    if num>=len(matches) or num<0:
                        self.printMessage("Error", "No More Matches found", mode=0)
                    else:
                        identity = matches[num]
                        details = self._dbObject.search('user_id', identity, 'users', 'LIKE', mode=2)
                        self.mainWindow(self,user_id,details, mode=9, num=num)

    def regHandler(self,name,email,password,age,gender,city,bio):
        mydict={'user_id':"NULL",'name':name,'email':email,'password':password,'age':age,'gender':gender,'bg':'avatar.jpeg','city':city,'bio':bio}
        flag=self._dbObject.insert(mydict,'users')  #control is given to dbhelper file(DATA)
        if flag==1:
            return 1
        else:
            return 0

    def updateHandler(self,user_id,name,age,gender,city,bio,table_name):
        details = self._dbObject.get_details(user_id)

        if name == '':
            name = details[0][1]
        if age == '':
            age = details[0][4]
        if gender == '':
            gender = details[0][5]
        if city == '':
            city = details[0][7]
        if bio == '':
            bio = details[0][8]

        age_verify = int(age)
        if age_verify<18:
            self.printMessage("Sorry", "Seems like you are underage.\n", mode=0)
            self.mainWindow(self,user_id,details,mode=4)

        else:
            mydict1 = {'user_id':user_id,'name': name, 'age': age,'gender':gender,'city':city,'bio':bio}

            flag=self._dbObject.update(mydict1,table_name)
            if(flag==1):
                self.printMessage("UPDATE","Your settings have been updated",mode=2)
                self.mainWindow(self, user_id, details, mode=1)
            else:
                self.printMessage("Retry","Cannot Update Right Now",mode=0)

    def propose(self,juliet_id):
        response=self._dbObject.search('romeo_id',self.user_id,'juliet_id',juliet_id,'proposals',mode=0)
        if len(response)>0:
            self.printMessage("Wait","You've already sent proposal",mode=2)
        else:
            mydict = {'proposal_id': 'NULL', 'romeo_id': self.user_id, 'juliet_id': juliet_id}
            response = self._dbObject.insert(mydict, 'proposals')
            if response == 1:
                self.printMessage("Success", "Proposal sent",mode=2)
            else:
                self.printMessage("Fail", "Not Sent",mode=0)


    def proposalHandler(self,user_id,data_own,num,mode):
        if mode==1:
            self.viewUsers(num,user_id,1)

                    #details = self._dbObject.get_details(i)
                    #self.mainWindow(self,details,1,0)

        if mode==2:

            self.viewUsers(num,user_id,2)
            #if len(response) == 0:
            # print("Nothing")
            #else:
            #details = self._dbObject.get_details(i)
            #self.mainWindow(self, details, 1, 0)

        if mode==3:
            self.viewUsers(num,user_id,3)

    def deleteHandler(self,data_own):
        reply=self.printMessage("Verify","Are you Sure?",mode=1)
        if reply=='yes':
            flag=self._dbObject.deleteAccount(data_own[0][0])
            if(flag==1):
                self.printMessage("Successful","Your account deleted",mode=2)
                self.mainWindow(self,data_own,0,mode=6)
                self.__init__()
            else:
                self.printMessage("Failed","Try Again",mode=0)
                self.mainWindow(self,data_own,0,mode=1)
        else:
            self.mainWindow(self,data_own,0,mode=1)

obj1=Tinder()

#An application is based on MVC
#M-Model/Data using dbhelper
#V-View  using gui
# #C-Control using tinder