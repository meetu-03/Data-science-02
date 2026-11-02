import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1410",
        database="task_manager_db1"
    )

    if conn.is_connected():
        print("Connection established successfully!")

        cursor = conn.cursor()

        # Create table query
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT,
            status VARCHAR(20) DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        query = """
        INSERT INTO tasks (title, description, status)
        VALUES (%s, %s, %s)
        """

        data = [
        ("learn_numpy", "Practice NumPy arrays", "Pending"),
        ("learn_pandas", "Practice DataFrames", "Pending"),
        ("learn_sql", "Practice SQL queries", "In Progress"),
        ("learn_python", "Practice Python programs", "Completed"),
        ("learn_matplotlib", "Create data visualizations", "Pending"),
        ("build_project", "Build a Task Manager app", "In Progress")
        ]

        # cursor.executemany(query, data)
        conn.commit()
        conn.commit()
        # print("data insert succesfully")
        # cursor.execute("TRUNCATE TABLE tasks")
        # conn.commit()

        # print("All data deleted successfully!")    
        query1="""SELECT * FROM TASKS"""    


        df=pd.read_sql(query1,conn)
        print(df)
        


except Error as e:
    print(f"Something went wrong: {e}")
