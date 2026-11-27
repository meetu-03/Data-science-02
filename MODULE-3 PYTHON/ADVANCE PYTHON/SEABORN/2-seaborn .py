import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data={
    "name":["meetu","forum","faiz","mishri"],
    "age":[20,20,21,23],
    "salary":[20000,23000,1200,14000,]

}


df=pd.DataFrame(data)

print(df)

# bar chart
sns.barplot(data=df,x="name",y="salary")
plt.title("name and salary")
plt.show()

# Scatterplot

sns.scatterplot(data=df,x="name",y="salary")
plt.ite("name vs salary")
plt.show()


#Histogram

sns.histplot(data=df,x="name",y="salary")
plt.title("name vs salary")
plt.show()
