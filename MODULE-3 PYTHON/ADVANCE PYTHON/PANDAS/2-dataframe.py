import pandas as pd

data={ "id":[1,2,3,4,5,],
      "name":["meet","forum","faig","mishri","brijes"],
      "age":[12,32,45,63,21],
      "salary":[10000,20000,33000,4000,50110]

}

df=pd.DataFrame(data)
print(df)
# FIND THE MAX SALARY DATA

max=df["salary"].max()
print("maximum salary is :",max)


min=df["salary"].min()
print("minimum salary is :",min)



avg=df["salary"].mean()
print("avg salary is :",avg)



sum=df["salary"].sum()
print("sum of salary is :",sum)

