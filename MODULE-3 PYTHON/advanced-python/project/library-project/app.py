
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Database connection
conn = sqlite3.connect("library_db.sqlite")
cur = conn.cursor()



# 2. Create tables
cur.executescript("""
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT
);

CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    book_id INTEGER,
    loan_date TEXT,
    returned INTEGER DEFAULT 0,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);
""")

# 3. Insert authors
cur.executemany(
    "INSERT OR IGNORE INTO authors VALUES (?, ?, ?)",
    [
        (1, "R.K. Narayan", "India"),
        (2, "J.K. Rowling", "UK"),
        (3, "Chetan Bhagat", "India")
    ]
)

# 4. Insert books
cur.executemany(
    "INSERT OR IGNORE INTO books VALUES (?, ?, ?, ?)",
    [
        (1, "Malgudi Days", "Fiction", 1),
        (2, "Harry Potter", "Fantasy", 2),
        (3, "Five Point Someone", "Drama", 3),
        (4, "Half Girlfriend", "Romance", 3),
        (5, "Swami and Friends", "Fiction", 1)
    ]
)

# 5. Insert students
cur.executemany(
    "INSERT OR IGNORE INTO students VALUES (?, ?, ?)",
    [
        (1, "Meet", "10A"),
        (2, "Faiz", "10B"),
        (3, "Forum", "10A"),
        (4, "Pranav", "11C"),
        (5, "Astha", "10B")
    ]
)

# 6. Insert loan records
cur.executemany(
    "INSERT OR IGNORE INTO loans VALUES (?, ?, ?, ?, ?)",
    [
        (1, 1, 1, "2026-09-01", 1),
        (2, 2, 2, "2026-09-03", 0),
        (3, 3, 3, "2026-09-05", 1),
        (4, 4, 4, "2026-09-10", 0),
        (5, 5, 2, "2026-09-12", 1),
        (6, 1, 5, "2026-09-15", 0),
        (7, 2, 3, "2026-09-18", 1)
    ]
)

conn.commit()
print("Data inserted successfully!")

# 7. Update loan status
cur.execute("""
UPDATE loans
SET returned = 1
WHERE id = 2
""")

conn.commit()
print("Loan updated successfully!")

# 8. JOIN all tables
query = """
SELECT
    students.name AS student_name,
    students.class,
    books.title AS book_title,
    authors.name AS author_name,
    loans.loan_date,
    loans.returned
FROM loans
JOIN students
ON loans.student_id = students.id
JOIN books
ON loans.book_id = books.id
JOIN authors
ON books.author_id = authors.id
"""

loans_df = pd.read_sql(query, conn)

# Show loan status
loans_df["status"] = loans_df["returned"].map({
    1: "Returned",
    0: "Not returned"
})

print("\nAll Loan Records:")
print(loans_df)

# 9. Loans per author
author_query = """
SELECT
    authors.name AS author_name,
    COUNT(loans.id) AS total_loans,
    SUM(loans.returned) AS returned_loans
FROM loans
JOIN books
ON loans.book_id = books.id
JOIN authors
ON books.author_id = authors.id
GROUP BY authors.id, authors.name
ORDER BY total_loans DESC
"""

author_df = pd.read_sql(author_query, conn)

print("\nLoans Per Author:")
print(author_df)

# 10. Export to Excel
with pd.ExcelWriter("library_report.xlsx") as writer:
    loans_df.to_excel(writer, sheet_name="Loans", index=False)
    author_df.to_excel(writer, sheet_name="Authors", index=False)

print("\nExcel file created successfully!")

# 11. Count returned and unreturned books
returned = (loans_df["status"] == "Returned").sum()
not_returned = (loans_df["status"] == "Not returned").sum()

print("\nReturned books:", returned)
print("Not returned books:", not_returned)

# 12. Pie chart
plt.figure(figsize=(6, 5))

plt.pie(
    [returned, not_returned],
    labels=["Returned", "Not returned"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Book Return Status")
plt.show()


conn.close()

print("\nDatabase connection closed!")
