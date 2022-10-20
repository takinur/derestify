#!/usr/bin/python3
import os
import pymysql

# Database connection parameters - update as needed
DB_USER=os.getenv('DB_USER') or 'root'
DB_PSWD=os.getenv('DB_PSWD') or None
DB_HOST=os.getenv('DB_HOST') or 'localhost'

db = pymysql.connect(host=DB_HOST, 
										 user=DB_USER, 
										 password=DB_PSWD, 
										 database='mysql', 
										 cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
cursor.execute("SHOW DATABASES")

print("Content-type: text/html\n")
print("Setup Successful")
