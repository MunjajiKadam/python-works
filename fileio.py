import pandas as pd
df = pd.read_csv("../sql-ultimate-course-main/datasets/Customers.csv.csv")
df2 = pd.read_csv("../sql-ultimate-course-main/datasets/Orders.csv")  # Corrected file path
df3 = pd.read_csv("../sql-ultimate-course-main/datasets/Products.csv.csv")
df4 = pd.read_csv("../sql-ultimate-course-main/datasets/OrderArchive.csv.csv")
print(df.head())
print(df2.head())
print(df3.head())
print(df4.head())