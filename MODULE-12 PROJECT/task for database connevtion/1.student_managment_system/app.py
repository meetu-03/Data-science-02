# # 
# ## Task 1: Student Management System
# - Create a Python application to manage student records.
# - Perform CRUD operations (Create, Read, Update, Delete) on student details.
# - Connect the application with both SQLite and MySQL databases.




import mysql.connector
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

    

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_managment_db"
)

if conn.is_connected():
    print("Database connected successfully")

cur = conn.cursor()
cur.execute("ALTER TABLE STUDENT_MNG AUTO_INCREMENT = 1")
print("all id reset")

cur.execute("""
    CREATE TABLE IF NOT EXISTS STUDENT_MNG (
        STU_ID INT PRIMARY KEY AUTO_INCREMENT,
        STU_NAME VARCHAR(255),
        STU_SCHOOL VARCHAR(255),
        ADDRESS VARCHAR(255),
        STANDERD INT
    )
""")

conn.commit()

print("Table STUDENT_MNG created successfully")



#data insert with input



while True:

    print("PRESS 1 FOR ADD STUDENT :  ")
    print("PRESS 2 FOR DELET STUDENT :  ")
    print("PRESS 3 FOR FETCH STUDENT DATA :  ")
    print("PRESS 4 FOR EXCEL SHEET :  ")
    print("PRESS 5 FOR CHART :  ")
    print(" PRESS 6 FOR EXITING PROGRAM :  ")

    
    choice=int(input("ENTER YOU CHOICE :  "))


    if choice == 1:
        STU_NAME=str(input("ENTER STUDENT NAME :  "))
        STU_SCHOOL=str(input("ENTER STUDENT SCHOLL NAME :  "))
        ADDRESS=str(input("ENTER ADDRESS :  "))
        STANDERD=int(input("ENTER STUDENT'S STANDERD :  "))


        QUERY="""
        INSERT INTO STUDENT_MNG
        (STU_NAME,STU_SCHOOL,ADDRESS,STANDERD)
        VALUES(%s,%s,%s,%s)

        """

        values=(STU_NAME,STU_SCHOOL,ADDRESS,STANDERD)


        cur.execute(QUERY,values)
        conn.commit()

        print("DATA INSERTY SUCCESSFULLY")

    elif choice == 2:

            STU_ID = int(input("ENTER STUDENT ID FOR DELETE DATA: "))

            QUERY = """
            DELETE FROM STUDENT_MNG
            WHERE STU_ID = %s
            """

            cur.execute(QUERY, (STU_ID,))
            conn.commit()

            if cur.rowcount > 0:
             print("Student deleted successfully!")
            else:
             print("Student ID not found!")

 
    elif choice == 3:

             STU_ID = int(input("ENTER STUDENT ID: "))

             QUERY = """
             SELECT * FROM STUDENT_MNG
             WHERE STU_ID = %s
             """

             cur.execute(QUERY, (STU_ID,))
             result = cur.fetchall()

             if result:
                print("DATA FETCHED SUCCESSFULLY")

                for row in result:
                  print(row)
             else:
               print("STUDENT ID NOT FOUND")



    elif choice == 4:
        query="""SELECT * FROM STUDENT_MNG"""
        df=pd.read_sql(query,conn)
        EXCEL_FILE=df.to_excel("student_data.xlsx", index=False, engine='openpyxl')
        print("EXCEL FILE GENEREATED SUCCESSFULLY")
       
    elif choice == 5 :
        
        query = """SELECT STANDERD, COUNT(*) AS student_count FROM STUDENT_MNG GROUP BY STANDERD"""
        df = pd.read_sql(query, conn)

        plt.bar(df['STANDERD'], df['student_count'])
        plt.xlabel('Standard')
        plt.ylabel('Number of Students')
        plt.title('Number of Students by Standard')
        plt.show()

    elif choice == 6:
        print("EXITING THE PROGRAM")
        break

    else :
        print("invalid choice. Please try again.")
        




