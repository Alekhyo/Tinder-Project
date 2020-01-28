import mysql.connector              #database is used for CRUD. C-create, R-Retrieve, U-update, D-delete
class DBHelper():
    def __init__(self):
        try:
            self._connection=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="tinder")
            self._mycursor=self._connection.cursor()
        except:
            print("Couldnot Connect")

        # self._connection is a certificate you get so that you dont't need to authenticate every time you access the database
        # self._myscursor is like a cursor . It helps to browse through the query

    def search(self,*args,mode=0):
        if mode==0:
            try:
                self._mycursor.execute("SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'".format(args[4],args[0],args[1],args[2],args[3]))
                response=self._mycursor.fetchall()    #whatever we are fetching . all the data is getting is stored in response which is returned in loginHandler()
                return response                       #response is a list of tuples where each tuple is information of each user like [('1','salman','bhai@gmail.com',.......)]
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
        # SELECT * FROM `users` WHERE `user_id` LIKE '2'
        try:
            self._mycursor.execute("SELECT * FROM `users` WHERE `user_id` LIKE '{}'".format(user_id))
            response = self._mycursor.fetchall()
            return response
        except:
            print("Couldnot Connect")

    def insert(self,inputDict,table):
        # INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `age`, `gender`, `bg`, `city`, `bio`) VALUES (NULL, 'virat', 'vkohli@gmail.com', 'anushka', '28', 'male', 'virat.jpg', 'delhi', 'captain')
        # insert into 'table'('column_name1',.........) values ('column_value1',.......)

        cols=""                                         #we are using this approach so that we can use insert() for any column_name,column_value and any table
        colval=""
        for i in inputDict:
            cols=cols+ "`" + i + "`" + ","            #this generates the column_names as a string like this `user_id`, `name`, `email`, `password`, `age`, `gender`, `bg`, `city`, `bio`,
            colval=colval+"'"+str(inputDict[i])+"'"+","   #this generates the column_values as a string like this NULL, 'virat', 'vkohli@gmail.com', 'anushka', '28', 'male', 'virat.jpg', 'delhi', 'captain',

        cols=cols[:-1]   #there is an extra comma(,) at last . we want to omit that so we use slicing and we get `user_id`, `name`, `email`, `password`, `age`, `gender`, `bg`, `city`, `bio`
        colval=colval[:-1] #there is an extra comma(,) at last . we want to omit that so we use slicing and we get NULL, 'virat', 'vkohli@gmail.com', 'anushka', '28', 'male', 'virat.jpg', 'delhi', 'captain'

        try:
            self._mycursor.execute("INSERT INTO `{}` ({}) VALUES ({})".format(table,cols,colval))
            self._connection.commit()       #as we are inserting or deleting, we have to use commit() i.e only during write operation not in read operation
            return 1
        except:
            return 0

    def update(self,inputDict1,table1):
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
            self._mycursor.execute("UPDATE `{}` SET {} WHERE `{}`.`{}` = {}".format(table1,editval,table1,p_key,id))    # UPDATE `users` SET `name` = 'katrina kaif', `age` = '30' WHERE `users`.`user_id` = 4;
            self._connection.commit()
            return 1
        except:
            return 0

    def deleteAccount(self,data):
            try:
                self._mycursor.execute("DELETE FROM `users` WHERE `users`.`user_id` LIKE {}".format(data))              #DELETE FROM `users` WHERE `users`.`user_id` = 9
                self._mycursor.execute("DELETE FROM `proposals` WHERE `proposals`.`romeo_id` LIKE {}".format(data))     #DELETE FROM `proposals` WHERE `proposals`.`romeo_id` = 9
                self._mycursor.execute("DELETE FROM `proposals` WHERE `proposals`.`juliet_id` LIKE {}".format(data))    #DELETE FROM `proposals` WHERE `proposals`.`juliet_id` = 9
                self._connection.commit()                                                                               #deletes the user data from users table and proposals table also
                return 1
            except:
                return 0
