# series is an inbuilt method in python via pandas 
# series is used to provides data of 1 column 


import pandas as pd

age=[10,20,30,40,50]
res=pd.Series(age)
print(res)

# multiple data via series 


data={ "id":[1,2,3,4,5,],
      "name":["meet","forum","faig","mishri","brijesh"],
      "age":[12,32,45,63,21],
      "salary":[10000,20000,33000,4000,50110]

}

res=pd.Series(data)
print(res)
