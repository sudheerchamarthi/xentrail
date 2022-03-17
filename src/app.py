from flask import Flask
import platform
import datetime
import os
from datetime import date
import mysql.connector
app = Flask(__name__)
  
@app.route('/')
def myapp():
    START_DATE = os.environ.get('START_DATE')
    CANDIDATE_NBAME = os.environ.get('CANDIDATE_NBAME')
    HOST = "172.17.0.3"
    DBUSERNAME = "root"
    DBPASSWORD = "Secret@123"
    DBNAME = "appaudit"
    DB_TABLE_NAME="audit"
    #return "My OS is " +  str(platform.platform())
    #return "Xendit - Trial - " + CANDIDATE_NBAME + " - "+ START_DATE + " - " + date.today().strftime("%Y/%m/%d")
    #return str(round(datetime.datetime.utcnow().timestamp() * 1000)) 
    mydb = mysql.connector.connect(host=HOST, user=DBUSERNAME, passwd=DBPASSWORD)
    mycursor=mydb.cursor()
    # Create Databse if not exists 
    mycursor.execute("create database IF NOT EXISTS " + DBNAME)
    # Choose DB
    mycursor.execute("use "+ DBNAME)
    #Create Table
    mycursor.execute("create table IF NOT EXISTS " + DB_TABLE_NAME + " (logging varchar(70),timestamp varchar(20));")
    #Insert
    mycursor.execute("INSERT INTO " + DB_TABLE_NAME + " (logging, timestamp) VALUES ('Yes'," + str(round(datetime.datetime.utcnow().timestamp() * 1000)) + " ) ") 
    mydb.commit()
    return "Success!. Logged entry in DB with Timestamp"




if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = os.environ.get('PORT'), debug = True) 
