import guihelper
import dbhelper
from tkinter import *
from tkinter import messagebox

class Tinder(guihelper.GUI,dbhelper.DBHelper):
    def __init__(self):
        self._dbObject=dbhelper.DBHelper()
        super().__init__(self)

    def loginHandler(self,*args):
        response=self._dbObject.search('email',args[0],'password',args[1],'users',mode=0)

        if len(response) == 0:
                self.printMessage("Invalid Login", "Please provide correct credentials",mode=0)

        else:
                self.user_id=response[0][0]
                self.doLogin(self.user_id,response)

    def checker(self,name,email,password,age,gender,city,bio,image):
        """
                                    This function checks various credentials during registraion
                                    Date:29/01/2020
                                    Created By:Alekhyo
                                    Input: valid inputs
                                    Output: GUI output
        """
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
                                insertion=self.regHandler(name,email,password,age,gender,city,bio,image)
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
        """
                                    This function displays the details of the logged in user
                                    Date:29/01/2020
                                    Created By:Alekhyo
                                    Input: valid input
                                    Output: GUI output
        """
        self.mainWindow(self,user_id,data_own,mode=1)

    def viewUsers(self,num,user_id,mode=0):
        """
                                    This function displays details of other users
                                    Date:29/01/2020
                                    Created By:Alekhyo
                                    Input: tuple,mode
                                    Output: GUI output
        """
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

    def regHandler(self,name,email,password,age,gender,city,bio,image):
        """
                                    This function registers a new user
                                    Date:29/01/2020
                                    Created By:Alekhyo
                                    Input: valid inputs
                                    Output:1/0
        """
        mydict={'user_id':"NULL",'name':name,'email':email,'password':password,'age':age,'gender':gender,'bg':image,'city':city,'bio':bio}
        flag=self._dbObject.insert(mydict,'users')
        if flag==1:
            return 1
        else:
            return 0

    def updateHandler(self,user_id,name,age,gender,city,bio,table_name):
        """
                                    This function updates several messages
                                    Date:29/01/2020
                                    Created By:Alekhyo
                                    Input: mode
                                    Output: GUI output
        """
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
        """
                                    This function sends proposal to other users
                                    Date:29/01/2020
                                    Created By:Alekhyo
                                    Input: user_id
                                    Output: GUI output
        """
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
        """
                                    This function displays several proposal activities
                                    Date:29/01/2020
                                    Created By:Alekhyo
                                    Input: user_id,tuple,mode
                                    Output: GUI output
        """
        if mode==1:
            self.viewUsers(num,user_id,1)

        if mode==2:
            self.viewUsers(num,user_id,2)

        if mode==3:
            self.viewUsers(num,user_id,3)

    def deleteHandler(self,data_own):
        """
                                    This function deletes the current user's details
                                    Date:29/01/2020
                                    Created By:Alekhyo
                                    Input: tuple
                                    Output: GUI output
        """
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