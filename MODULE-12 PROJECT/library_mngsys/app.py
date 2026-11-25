
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd

# ==========================================
# DATABASE CONNECTION
# ==========================================

conn = sqlite3.connect("library.db")
cursor = conn.cursor()


# ==========================================
# CREATE TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
""")

conn.commit()


# ==========================================
# INSERT SAMPLE DATA
# ==========================================

cursor.execute("SELECT COUNT(*) FROM books")

count = cursor.fetchone()[0]

if count == 0:

    sample_data = [
        ("Python Programming", "Guido van Rossum", "Programming", 10),
        ("Data Science Handbook", "Jake VanderPlas", "Data Science", 5),
        ("Machine Learning", "Tom Mitchell", "AI & ML", 7),
        ("Deep Learning", "Ian Goodfellow", "AI & ML", 4),
        ("Rich Dad Poor Dad", "Robert Kiyosaki", "Finance", 8),
        ("Atomic Habits", "James Clear", "Self Help", 6),
        ("The Alchemist", "Paulo Coelho", "Novel", 3),
        ("SQL for Beginners", "John Russell", "Programming", 9),
        ("Think and Grow Rich", "Napoleon Hill", "Motivation", 5),
        ("Wings of Fire", "A.P.J. Abdul Kalam", "Biography", 0)
    ]

    cursor.executemany("""
    INSERT INTO books (title, author, category, quantity)
    VALUES (?, ?, ?, ?)
    """, sample_data)

    conn.commit()

    print("Sample Data Inserted Successfully!")


# ==========================================
# 1. ADD BOOK
# ==========================================

def add_book():

    print("\n========== ADD BOOK ==========")

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    category = input("Enter Category: ").strip()
    quantity = int(input("Enter Quantity: "))

    if not title or not author or not category:
        print("Fields cannot be empty!")
        return

    if quantity < 0:
        print("Quantity cannot be negative!")
        return

    cursor.execute("""
    INSERT INTO books (title, author, category, quantity)
    VALUES (?, ?, ?, ?)
    """, (title, author, category, quantity))

    conn.commit()

    print("\nBook Added Successfully!")


# ==========================================
# 2. VIEW ALL BOOKS
# ==========================================

def view_books():

    print("\n========== ALL BOOKS ==========")

    df = pd.read_sql_query("SELECT * FROM books", conn)

    if df.empty:
        print("No Books Available!")

    else:
        print(df.to_string(index=False))


# ==========================================
# 3. SEARCH BOOK
# ==========================================

def search_book():

    print("\n========== SEARCH BOOK ==========")

    book_id = int(input("Enter Book ID: "))

    df = pd.read_sql_query(
        "SELECT * FROM books WHERE book_id = ?",
        conn,
        params=(book_id,)
    )

    if df.empty:
        print("Book Not Found!")

    else:
        print(df.to_string(index=False))


# ==========================================
# 4. UPDATE BOOK
# ==========================================

def update_book():

    print("\n========== UPDATE BOOK ==========")

    book_id = int(input("Enter Book ID: "))

    cursor.execute(
        "SELECT * FROM books WHERE book_id = ?",
        (book_id,)
    )

    book = cursor.fetchone()

    if book is None:
        print("Book Not Found!")
        return

    print("\n1. Update Title")
    print("2. Update Author")
    print("3. Update Category")
    print("4. Update Quantity")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        value = input("Enter New Title: ").strip()

        if not value:
            print("Title cannot be empty!")
            return

        cursor.execute(
            "UPDATE books SET title = ? WHERE book_id = ?",
            (value, book_id)
        )

    elif choice == "2":

        value = input("Enter New Author: ").strip()

        if not value:
            print("Author cannot be empty!")
            return

        cursor.execute(
            "UPDATE books SET author = ? WHERE book_id = ?",
            (value, book_id)
        )

    elif choice == "3":

        value = input("Enter New Category: ").strip()

        if not value:
            print("Category cannot be empty!")
            return

        cursor.execute(
            "UPDATE books SET category = ? WHERE book_id = ?",
            (value, book_id)
        )

    elif choice == "4":

        value = int(input("Enter New Quantity: "))

        if value < 0:
            print("Quantity cannot be negative!")
            return

        cursor.execute(
            "UPDATE books SET quantity = ? WHERE book_id = ?",
            (value, book_id)
        )

    else:
        print("Invalid Choice!")
        return

    conn.commit()

    print("\nBook Updated Successfully!")


# ==========================================
# 5. DELETE BOOK
# ==========================================

def delete_book():

    print("\n========== DELETE BOOK ==========")

    book_id = int(input("Enter Book ID: "))

    cursor.execute(
        "SELECT * FROM books WHERE book_id = ?",
        (book_id,)
    )

    book = cursor.fetchone()

    if book is None:
        print("Book Not Found!")
        return

    confirm = input("Are You Sure? (yes/no): ")

    if confirm.lower() == "yes":

        cursor.execute(
            "DELETE FROM books WHERE book_id = ?",
            (book_id,)
        )

        conn.commit()

        print("Book Deleted Successfully!")

    else:
        print("Delete Cancelled!")


# ==========================================
# 6. GENERATE EXCEL FILE
# ==========================================

def export_excel():

    print("\n========== EXCEL GENERATION ==========")

    df = pd.read_sql_query("SELECT * FROM books", conn)

    if df.empty:
        print("No Data Available!")
        return

    file_name = "Library_Books.xlsx"

    df.to_excel(
        file_name,
        index=False,
        engine="openpyxl"
    )

    print("\nExcel File Generated Successfully!")
    print("File Name:", file_name)


# ==========================================
# 7. DISPLAY CHARTS
# ==========================================

def show_charts():

    print("\n========== DATA VISUALIZATION ==========")

    df = pd.read_sql_query("SELECT * FROM books", conn)

    if df.empty:
        print("No Data Available for Charts!")
        return

    print("\n1. Category Wise Books")
    print("2. Book Quantity Chart")
    print("3. Availability Chart")
    print("4. All Charts")

    choice = input("\nEnter Your Choice: ")

    # CATEGORY WISE CHART

    if choice == "1" or choice == "4":

        category_data = df.groupby("category")["quantity"].sum()

        category_data.plot(
            kind="bar",
            title="Category Wise Books"
        )

        plt.xlabel("Category")
        plt.ylabel("Total Quantity")
        plt.tight_layout()
        plt.show()

    # BOOK QUANTITY CHART

    if choice == "2" or choice == "4":

        plt.bar(df["title"], df["quantity"])

        plt.title("Book Quantity Chart")
        plt.xlabel("Book Title")
        plt.ylabel("Quantity")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    # AVAILABILITY CHART

    if choice == "3" or choice == "4":

        available = (df["quantity"] > 0).sum()
        unavailable = (df["quantity"] == 0).sum()

        plt.pie(
            [available, unavailable],
            labels=["Available", "Unavailable"],
            autopct="%1.1f%%"
        )

        plt.title("Book Availability")
        plt.tight_layout()
        plt.show()

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid Choice!")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n========================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("========================================")

    print("\n1. View All Books")
    print("2. Generate Excel File")
    print("3. Display Charts")
    print("4. Add Book")
    print("5. Update Book")
    print("6. Delete Book")
    print("7. Search Book")
    print("8. Exit")

    choice = input("\nEnter Your Choice: ")

    try:

        if choice == "1":
            view_books()

        elif choice == "2":
            export_excel()

        elif choice == "3":
            show_charts()

        elif choice == "4":
            add_book()

        elif choice == "5":
            update_book()

        elif choice == "6":
            delete_book()

        elif choice == "7":
            search_book()

        elif choice == "8":
            print("\nThank You for Using Library Management System!")
            break

        else:
            print("\nInvalid Choice! Please Try Again.")

    except ValueError:
        print("\nPlease Enter Valid Numeric Values!")

    except sqlite3.Error as e:
        print("\nDatabase Error:", e)



# ==========================================
# CLOSE DATABASE
# ==========================================

conn.close()

print("\nDatabase Connection Closed!")
