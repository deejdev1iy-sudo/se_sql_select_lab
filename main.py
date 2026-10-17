# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
""", conn)
print(df_first_five)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
""",conn)
print(df_five_reverse)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID
FROM employess
""",conn)
print(df_alias)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
SELECT
    employeeNumber,
    lastName,
    jobTitle,
    CASE
      WHEN jobTitle = "President,
       OR jobTitle = "VP Sales,
       OR jobTitle = "VP Marketing",
       THEN "EXCUTIVE"
      ELSE "Not Excutive"
    END AS role
FROM employees
""",conn)
print(df_executive)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""
SELECT LENGHT(lastName AS name_length
FROM employees
""",conn)
print(df_name_length)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2)AS short_title
FROM employees
""",conn)
print(df_short_title)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""
SELECT ROUND(priceEach * quantityOrdered, 2)AS total_price
FROM orderDetails
""",conn).sum()
print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
SELECT 
    orderDate,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%y', orderDate) AS year
FROM orderDetails
""", conn)
print(df_first_five)
conn.close()