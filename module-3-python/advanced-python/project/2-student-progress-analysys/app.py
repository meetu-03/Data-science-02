# ## Task 1: Student Performance Analysis

# Create a Pandas DataFrame containing the names of 10 students along with their marks in Mathematics, Science, and English.

# - Calculate the total and average marks for each student.
# - Find the student with the highest average marks.
# - Create a **bar chart using Matplotlib** showing the average marks of each student.




import pandas as pd
import matplotlib.pyplot as plt

data = {
    "student_name": ["meet","om","rajan","prince","sahi","faize","misri","foram","sagar","rahul"],

    "math_score": [85, 92, 78, 90, 88, 95, 76, 89, 82, 91],

    "science_score": [88, 95, 82, 93, 90, 92, 80, 87, 85, 94],

    "english_score": [90, 88, 85, 95, 86, 94, 79, 91, 88, 90]
}

df = pd.DataFrame(data)

# Total marks for each student
df["total"] = (
    df["math_score"] +
    df["science_score"] +
    df["english_score"]
)

# Average marks for each student
df["average"] = df[
    ["math_score", "science_score", "english_score"]
].mean(axis=1)

print(df)

# Student with highest average
highest = df.loc[df["average"].idxmax()]

print("Student with highest average:", highest["student_name"])
print("Highest average:", highest["average"])

# Bar chart
plt.bar(df["student_name"], df["average"])

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")


# generate_excel_file=df.to_excel("student.xlsx",engine="openpyxl",index=False)
# print("geneate succecefully:",generate_excel_file)

summry=pd.DataFrame({
    "total_marks": [df["total"].sum()],
    "average_marks": [df["average"].mean()]
})

with pd.ExcelWriter("student_summary.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, student1="Student Data", index=False)
    summry.to_excel(writer, student2="Summary", index=False)





plt.show()

