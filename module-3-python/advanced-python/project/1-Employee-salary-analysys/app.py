import pandas as pd 
import matplotlib.pyplot as pptl

data= {
    "employee_name":["meet","faize","misri","foram","pranav","om","sahil","rajan"],
    "department":["IT","CS","HR","EE","EC","IT","CS","CS"],
    "salary":[18500,20000,50000,25000,19000,32000,23500,45000]

}


df=pd.DataFrame(data)
print(df)

print("------------------------------------")
print("total_salary is:",df["salary"].sum())   # all employee total salary
print("avrage_salary is :",df["salary"].mean())# AVG SALARY OF ALL EMPLOYEE  
avrage_salary=df["salary"].mean()
hi_salary=df [df["salary"] > avrage_salary]
print(hi_salary)


pptl.pie(
    hi_salary["salary"],
    labels=hi_salary["employee_name"],
    autopct="%1.1f%%"

)

pptl.show()