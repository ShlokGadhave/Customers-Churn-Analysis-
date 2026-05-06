import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
df=pd.read_csv('Customer Churn.csv')
print(df)
df.head()
df.info()
# Replacing blanks with zero as the tenure is zero 
df['TotalCharges']=df['TotalCharges'].replace(' ','0') 
df['TotalCharges']=df['TotalCharges'].astype(float) #convertng data type 
df.info()
print(df.isnull().sum())
print(df.describe())
print(df['customerID'].duplicated().sum())

# Conversion of values of senior citizen to Yes and No 
def conv(value):
    if value==1:
        return 'Yes'
    else:
        return 'No'
df['SeniorCitizen']=df['SeniorCitizen'].apply(conv)
print(df.head(30))
# Churn Visualization
count=sns.countplot(x=df['Churn'])
count.bar_label(count.containers[0])
plt.title('Count of customers by churn')
plt.show()
plt.figure(figsize=(3,4))
gp=df.groupby('Churn').agg({'Churn':'count'})
print(gp)
ar=plt.pie(gp['Churn'],labels=gp.index,autopct="%1.2f%%")
plt.title("Percentage of churn customers")
plt.show()
# From the given pie chart it clear that total 26.51% of customers have churned out 

plt.figure(figsize=(4,4))
kr=sns.countplot(x=df['gender'],data=df,hue='Churn')
kr.bar_label(kr.containers[0])
plt.title('Churn By Gender')
plt.show()