#how to connect with database


import sqlite3
#create a database
conn=sqlite3.connect("task_manager_app_db")
print("database connection succesfully")
conn.close()