import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("Dataset for Data Analytics (Project-2).xlsx")

# Display dataset
print("First 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataset Information:")
df.info()

print("\nShape of Dataset:")
print(df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Mean
print("\nMean:")
print(df.mean(numeric_only=True))

# Median
print("\nMedian:")
print(df.median(numeric_only=True))

# Count
print("\nCount:")
print(df.count())

# Product count
if "Product" in df.columns:
    print("\nOrders for Each Product:")
    print(df["Product"].value_counts())

# Payment method count
if "PaymentMethod" in df.columns:
    print("\nOrders by Payment Method:")
    print(df["PaymentMethod"].value_counts())

# Order status count
if "OrderStatus" in df.columns:
    print("\nOrders by Status:")
    print(df["OrderStatus"].value_counts())

# Product-wise quantity
if "Product" in df.columns and "Quantity" in df.columns:
    print("\nTotal Quantity Sold for Each Product:")
    print(df.groupby("Product")["Quantity"].sum())

# Total sales by payment method
if "PaymentMethod" in df.columns and "TotalPrice" in df.columns:
    print("\nTotal Sales by Payment Method:")
    print(df.groupby("PaymentMethod")["TotalPrice"].sum())

# Visualizations Product wise Sales
product_sales = df.groupby("Product")["TotalPrice"].sum()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Visualizations Payment Method 
df["PaymentMethod"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.show()

# Order Status 
df["OrderStatus"].value_counts().plot(kind="bar")
plt.title("Order Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.show()

# Sales trend
df["Date"] = pd.to_datetime(df["Date"])

daily_sales = df.groupby("Date")["TotalPrice"].sum()

plt.figure(figsize=(10,5))
daily_sales.plot()
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()