# create a table via sqlite3 in task_managaer_app_db

import sqlite3

# create database connection
conn=sqlite3.connect("task_managaer_app_db")
#create a table in database

cur=conn.cursor()
cur.execute(
    """
create table if not exists tasks(
id integer primary key autoincrement,
title text,
assign_date text,
status text,
comment text

)

"""
)

cur=conn.cursor()
cur.execute(
    """
create table if not exists users(
uid integer primary key autoincrement,
name text,
mobile text,
email text,
date text

)

"""
)


#print message

print("table created successfully in database")

conn.execute(
"""
insert into tasks(id,title,assign_date,status,comment)
values(1,"python_task","09-10-2026","complate","good"),(2,"SQl","09-10-2026","pending","in-progress")

"""


)
print("data inster complate")
#save quary
conn.commit()
conn.close()

