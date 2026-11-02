
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
from mysql.connector import Error


# ==========================================
# DELETE FUNCTION
# ==========================================

def delete_data(cur, conn):

    print("\n========== DELETE MENU ==========")
    print("PRESS 1 FOR DELETE CUSTOMER")
    print("PRESS 2 FOR DELETE PRODUCT")
    print("PRESS 3 FOR DELETE SALES")
    print("PRESS 4 FOR RESET IDS")

    choice = int(input("ENTER YOUR CHOICE: "))

    if choice == 1:

        cid = int(input("ENTER CUSTOMER ID: "))

        cur.execute("""
            DELETE FROM TBL_SALES
            WHERE CUSTOMER_ID = %s
        """, (cid,))

        cur.execute("""
                    DELETE FROM TBL_CUSTOMER
                    WHERE CUSTOMER_ID = %s
                """, (cid,))

        conn.commit()

        if cur.rowcount > 0:
            print("CUSTOMER DELETED SUCCESSFULLY")
        else:
            print("CUSTOMER ID NOT FOUND")

    elif choice == 2:

        pid = int(input("ENTER PRODUCT ID: "))

        cur.execute("""
            DELETE FROM TBL_SALES
            WHERE PRODUCT_ID = %s
        """, (pid,))

        cur.execute("""
                    DELETE FROM TBL_PRODUCT
                    WHERE PRODUCT_ID = %s
                """, (pid,))

        conn.commit()

        if cur.rowcount > 0:
            print("PRODUCT DELETED SUCCESSFULLY")
        else:
            print("PRODUCT ID NOT FOUND")

    elif choice == 3:

        sid = int(input("ENTER SALES ID: "))

        cur.execute("""
            DELETE FROM TBL_SALES
            WHERE SALES_ID = %s
        """, (sid,))

        conn.commit()

        if cur.rowcount > 0:
            print("SALES DELETED SUCCESSFULLY")
        else:
            print("SALES ID NOT FOUND")
    elif choice==4:
        cur.execute("ALTER TABLE TBL_SALES AUTO_INCREMENT = 1")
        cur.execute("ALTER TABLE TBL_CUSTOMER AUTO_INCREMENT = 1")
        cur.execute("ALTER TABLE TBL_PRODUCT AUTO_INCREMENT = 1")
        conn.commit()
        print("All table IDs reset successfully!")
    else:
        print("INVALID CHOICE")


# ==========================================
# MAIN PROGRAM
# ==========================================

try:

    # DATABASE CONNECTION

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sales_report_db"
    )

    if conn.is_connected():

        print("Database connected successfully!")

        cur = conn.cursor()

        # ==========================================
        # TABLE 1: CUSTOMER
        # ==========================================

        cur.execute("""
            CREATE TABLE IF NOT EXISTS TBL_CUSTOMER (
                CUSTOMER_ID INT PRIMARY KEY AUTO_INCREMENT,
                CUSTOMER_NAME VARCHAR(255) NOT NULL,
                EMAIL VARCHAR(255) UNIQUE,
                CITY VARCHAR(100)
            )
        """)

        print("Customer table created successfully!")


        # ==========================================
        # TABLE 2: PRODUCT
        # ==========================================

        cur.execute("""
            CREATE TABLE IF NOT EXISTS TBL_PRODUCT (
                PRODUCT_ID INT PRIMARY KEY AUTO_INCREMENT,
                PRODUCT_NAME VARCHAR(255) NOT NULL,
                CATEGORY VARCHAR(100),
                PRICE DECIMAL(10,2) NOT NULL
            )
        """)

        print("Product table created successfully!")


        # ==========================================
        # TABLE 3: SALES
        # ==========================================

        cur.execute("""
            CREATE TABLE IF NOT EXISTS TBL_SALES (
                SALES_ID INT PRIMARY KEY AUTO_INCREMENT,
                CUSTOMER_ID INT NOT NULL,
                PRODUCT_ID INT NOT NULL,
                QUANTITY INT NOT NULL,
                TOTAL_AMOUNT DECIMAL(10,2) NOT NULL,
                SALES_DATE DATE NOT NULL,

                FOREIGN KEY (CUSTOMER_ID)
                    REFERENCES TBL_CUSTOMER(CUSTOMER_ID),

                FOREIGN KEY (PRODUCT_ID)
                    REFERENCES TBL_PRODUCT(PRODUCT_ID)
            )
        """)

        print("Sales table created successfully!")

        conn.commit()


        # ==========================================
        # MENU BASED INSERTION
        # ==========================================

        while True:

            print("\n========== SALES REPORT SYSTEM ==========")

            print("Press 1 for Add Customer")
            print("Press 2 for Add Product")
            print("Press 3 for Add Sales")
            print("Press 4 for Delete Data")
            print("Press 5 for Exit")

            try:

                choice = int(input("\nENTER YOUR CHOICE: "))


                # ==================================
                # INSERT CUSTOMER
                # ==================================

                if choice == 1:

                    CUSTOMER_NAME = input("ENTER CUSTOMER NAME: ")
                    EMAIL = input("ENTER EMAIL: ")
                    CITY = input("ENTER CITY: ")

                    query = """
                        INSERT INTO TBL_CUSTOMER
                        (CUSTOMER_NAME, EMAIL, CITY)
                        VALUES (%s, %s, %s)
                    """

                    values = (CUSTOMER_NAME, EMAIL, CITY)

                    cur.execute(query, values)

                    conn.commit()

                    print("Customer data inserted successfully!")


                # ==================================
                # INSERT PRODUCT
                # ==================================

                elif choice == 2:

                    PRODUCT_NAME = input("ENTER PRODUCT NAME: ")
                    CATEGORY = input("ENTER CATEGORY: ")
                    PRICE = float(input("ENTER PRICE: "))

                    if PRICE <= 0:

                        print("Price must be greater than zero!")
                        continue

                    query = """
                        INSERT INTO TBL_PRODUCT
                        (PRODUCT_NAME, CATEGORY, PRICE)
                        VALUES (%s, %s, %s)
                    """

                    values = (PRODUCT_NAME, CATEGORY, PRICE)

                    cur.execute(query, values)

                    conn.commit()

                    print("Product data inserted successfully!")


                # ==================================
                # INSERT SALES
                # ==================================

                elif choice == 3:

                    cid = int(input("ENTER CUSTOMER ID: "))
                    pid = int(input("ENTER PRODUCT ID: "))
                    qty = int(input("ENTER QUANTITY: "))
                    date = input("ENTER SALES DATE (YYYY-MM-DD): ")

                    if qty <= 0:

                        print("Quantity must be greater than zero!")
                        continue


                    # FETCH PRODUCT PRICE

                    cur.execute("""
                        SELECT PRICE
                        FROM TBL_PRODUCT
                        WHERE PRODUCT_ID = %s
                    """, (pid,))

                    result = cur.fetchone()

                    if result is None:

                        print("Invalid Product ID!")

                    else:

                        price = float(result[0])

                        # AUTOMATIC CALCULATION

                        TOTAL_AMOUNT = qty * price

                        print("\nProduct Price:", price)
                        print("Quantity:", qty)
                        print("Total Amount:", TOTAL_AMOUNT)


                        # INSERT SALES DATA

                        cur.execute("""
                            INSERT INTO TBL_SALES
                            (CUSTOMER_ID, PRODUCT_ID, QUANTITY,
                             TOTAL_AMOUNT, SALES_DATE)
                            VALUES (%s, %s, %s, %s, %s)
                        """, (cid, pid, qty, TOTAL_AMOUNT, date))

                        conn.commit()

                        print("Sales data inserted successfully!")


                # ==================================
                # DELETE DATA
                # ==================================

                elif choice == 4:

                    delete_data(cur, conn)


                # ==================================
                # EXIT
                # ==================================

                elif choice == 5:

                    print("EXITING SALES REPORT SYSTEM...")

                    cur.close()
                    conn.close()

                    print("Database connection closed!")

                    break


                else:

                    print("INVALID CHOICE! TRY AGAIN.")


            except ValueError:

                print("Please enter valid numeric values!")

            except Error as e:

                conn.rollback()

                print(f"Database Error: {e}")


except Error as e:

    print(f"Connection Error: {e}")

