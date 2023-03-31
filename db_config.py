'''
Created on 

Course work: Mar 27, 2023

@author: 
    Bagiya

Source: https://stackoverflow.com/questions/24272223/importerror-no-module-named-mysql-connector-using-python2
        https://www.javatpoint.com/python-mysql-creating-new-database
'''

# dependencies
import mysql.connector  
import os
from dotenv import load_dotenv


load_dotenv()

  

# my connection
myconn = mysql.connector.connect(host = "localhost", 
                                 user = os.environ.get('USER_NAME'),
                                 passwd = os.environ.get('PASSWORD'), 
                                 database = os.environ.get('DB_NAME')
                                 )  
  
#printing the connection object   
# print(myconn)  

# user = os.environ.get('USER_NAME')
# print(user)

mycursor = myconn.cursor()


def getcredentials(user, password):
    
    query = "SELECT * FROM Login WHERE user = %s AND password = %s"
    values = (user, password)


    mycursor.execute(query, values)
    result = mycursor.fetchone()
    print(result)
    if result:
        return True 
    else:
        False         






    

