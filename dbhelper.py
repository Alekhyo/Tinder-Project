import mysql.connector
class DBHelper():
    def __init__(self):
        try:
            self._connection=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="tinder")
            self._mycursor=self._connection.cursor()
        except:
            print("Couldnot Connect")

    def search(self,*args,mode=0):
        """
                   This function runs various search queries
                   Date:29/01/2020
                   Created By:Alekhyo
                   Input:valid inputs
                   Output:a tuple

        """
        if mode==0:
            try:
                self._mycursor.execute("SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'".format(args[4],args[0],args[1],args[2],args[3]))
                response=self._mycursor.fetchall()
                return response
            except:
                print("Couldnot Connect")
        if mode==1:
            try:
                self._mycursor.execute("SELECT * FROM `users` WHERE `email` LIKE '{}'".format(args[1]))
                response=self._mycursor.fetchall()
                return response
            except:
                print("Couldnot Connect")

        if mode==2:
            try:
                self._mycursor.execute("SELECT * FROM `{}` WHERE `{}` {} '{}'".format(args[2],args[0],args[3],args[1]))
                response=self._mycursor.fetchall()
                return response
            except:
                print("Couldnot Connect")
        if mode==3:
            try:
                self._mycursor.execute("SELECT {} FROM `{}` WHERE `{}` LIKE '{}'".format(args[0],args[3],args[1],args[2]))
                response=self._mycursor.fetchall()
                return response
            except:
                print("Couldnot Connect")

    def get_details(self,user_id):
        """
                           This function retrieves details of the users
                           Date:29/01/2020
                           Created By:Alekhyo
                           Input:user_id
                           Output:a tuple

        """

        try:
            self._mycursor.execute("SELECT * FROM `users` WHERE `user_id` LIKE '{}'".format(user_id))
            response = self._mycursor.fetchall()
            return response
        except:
            print("Couldnot Connect")

    def insert(self,inputDict,table):
        """
                           This function inserts values into database
                           Date:29/01/2020
                           Created By:Alekhyo
                           Input:valid inputs
                           Output:1/0

        """
        cols=""
        colval=""
        for i in inputDict:
            cols=cols+ "`" + i + "`" + ","
            colval=colval+"'"+str(inputDict[i])+"'"+","

        cols=cols[:-1]
        colval=colval[:-1]

        try:
            self._mycursor.execute("INSERT INTO `{}` ({}) VALUES ({})".format(table,cols,colval))
            self._connection.commit()
            return 1
        except:
            return 0

    def update(self,inputDict1,table1):
        """
                                   This function updates values into database
                                   Date:29/01/2020
                                   Created By:Alekhyo
                                   Input:valid inputs
                                   Output:1/0

        """
        editval=""
        p_key=""
        id=""
        for i in inputDict1:
            if i=='user_id':
                p_key=i
                id=str(inputDict1[i])
            else:
                editval = editval + "`" + i + "`" + "=" + "'" + str(inputDict1[i]) + "'" + ","

        editval=editval[:-1]

        try:
            self._mycursor.execute("UPDATE `{}` SET {} WHERE `{}`.`{}` = {}".format(table1,editval,table1,p_key,id))
            self._connection.commit()
            return 1
        except:
            return 0

    def deleteAccount(self,data):
        """
                                   This function deletes user details from databse
                                   Date:29/01/2020
                                   Created By:Alekhyo
                                   Input:valid inputs
                                   Output:1/0

        """
        try:
                self._mycursor.execute("DELETE FROM `users` WHERE `users`.`user_id` LIKE {}".format(data))
                self._mycursor.execute("DELETE FROM `proposals` WHERE `proposals`.`romeo_id` LIKE {}".format(data))
                self._mycursor.execute("DELETE FROM `proposals` WHERE `proposals`.`juliet_id` LIKE {}".format(data))
                self._connection.commit()
                return 1
        except:
                return 0
