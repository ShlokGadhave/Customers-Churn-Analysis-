# Customer Churn Analysis using Python 📊

## 📌 Project Overview
This project focuses on analyzing customer churn data using Python libraries such as **Pandas, NumPy, Matplotlib, and Seaborn**.  
The main objective of the project is to identify patterns and factors that influence customer churn in a telecom company.

Customer churn refers to customers leaving or discontinuing the company's services. By analyzing churn behavior, businesses can improve customer retention strategies and reduce revenue loss.

---

# 🚀 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# 📂 Dataset Information

The dataset used in this project contains telecom customer information such as:

- Customer ID
- Gender
- Senior Citizen Status
- Tenure
- Internet Services
- Phone Services
- Contract Type
- Payment Method
- Churn Status

---

# ⚙️ Project Workflow

## 1️⃣ Data Loading
- Imported the dataset using Pandas.
- Displayed dataset structure using:
  - `head()`
  - `info()`
  - `describe()`

---

## 2️⃣ Data Cleaning
Performed preprocessing tasks such as:

- Replaced blank values in `TotalCharges`
- Converted `TotalCharges` datatype to float
- Checked missing values
- Checked duplicate customer IDs
- Converted `SeniorCitizen` values:
  - `1 → Yes`
  - `0 → No`

---

## 3️⃣ Exploratory Data Analysis (EDA)

The project includes multiple visualizations to understand churn behavior.

### 📈 Visualizations Included

- Churn Distribution
- Gender-wise Churn
- Senior Citizen Churn Analysis
- Tenure Distribution
- Contract Type Analysis
- Service-wise Churn Comparison
- Payment Method Analysis

---

# 📊 Key Insights

## 🔹 Churn Distribution
- Around **26.5%** customers have churned.
- Majority customers are retained.

---

## 🔹 Gender Analysis
- Male and Female churn rates are nearly similar.
- Gender does not significantly impact churn.

---

## 🔹 Senior Citizen Analysis
- Senior citizens show comparatively higher churn percentage.
- Older customers may require better support and engagement.

---

## 🔹 Tenure Analysis
- Customers with low tenure churn more frequently.
- Long-term customers are more likely to stay.

---

## 🔹 Contract Type Analysis
- Customers with **Month-to-Month contracts** have the highest churn.
- One-year and Two-year contract customers are more stable.

---

## 🔹 Service Analysis
Customers using services like:
- Online Security
- Tech Support
- Device Protection

tend to churn less.

Customers without these services show higher churn probability.

---

## 🔹 Payment Method Analysis
Electronic payment users show comparatively higher churn behavior.

---

# 📌 Conclusion

This project successfully identifies major factors affecting customer churn.  
The analysis shows that:

- Short-term customers are more likely to churn.
- Long-term contracts improve customer retention.
- Additional services like Online Security and Tech Support help reduce churn.
- Senior citizens require more attention for retention strategies.

These insights can help telecom companies improve customer satisfaction and reduce churn rates.

---

# 📷 Suggested Graphs for README

## 1️⃣ Churn Distribution

```python
count=sns.countplot(x=df['Churn'])
count.bar_label(count.containers[0])
plt.title('Count of customers by churn')
plt.show()
```

---

## 2️⃣ Churn by Tenure

```python
sns.histplot(x=df['tenure'],data=df,bins=50,hue='Churn')
plt.title('Churn By Tenure')
plt.show()
```

---

## 3️⃣ Contract Type Analysis

```python
sns.countplot(x=df['Contract'],data=df,hue='Churn')
plt.title('Count of Customers based on the contracts')
plt.show()
```

---

## 4️⃣ Payment Method Analysis

```python
sns.countplot(x='PaymentMethod',data=df,hue='Churn')
plt.title('Count of Payment Method Used')
plt.show()
```

---

# 📁 Project Structure

```bash
Customer-Churn-Analysis/
│
├── main.py
├── Customer Churn.csv
├── README.md
└── graphs/
```

---

# ▶️ How to Run the Project

## Step 1
Clone the repository

```bash
git clone <your-github-repo-link>
```

## Step 2
Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

## Step 3
Run the project

```bash
python main.py
```

---


---

# 🏆 Learning Outcomes

Through this project, I learned:

- Data Cleaning Techniques
- Exploratory Data Analysis
- Data Visualization
- Customer Behavior Analysis
- Business Insight Generation




