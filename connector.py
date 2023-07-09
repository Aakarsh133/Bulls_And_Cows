import mysql.connector
import datetime

def connect():
    db= mysql.connector.connect(host= "localhost", user= 'root', passwd= "Ghori@133")
    cursor= db.cursor()
    
    dt= datetime.datetime.now()
    dt= dt.strftime("%d%m%Y%H%M%S")

    cursor.execute("USE BULLS_AND_COWS")
    comm= "CREATE TABLE {} (name VARCHAR(255), score int)"
    cursor.execute(comm.format(dt))

connect()
