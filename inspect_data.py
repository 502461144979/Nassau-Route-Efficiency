
import pandas as pd

# Load the dataset from the project folder
file_path = "Nassau Candy Distributor.csv"
df = pd.read_csv(file_path)

print("\n===== DATASET OVERVIEW =====")
print("Number of rows and columns:", df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATE FORMAT CHECK =====")

# Interpret dates as day-month-year
df["Order Date Parsed"] = pd.to_datetime(
    df["Order Date"], format="%d-%m-%Y", errors="coerce"
)

df["Ship Date Parsed"] = pd.to_datetime(
    df["Ship Date"], format="%d-%m-%Y", errors="coerce"
)

# Calculate the difference in days
df["Lead Time Days"] = (
    df["Ship Date Parsed"] - df["Order Date Parsed"]
).dt.days

print("Invalid order dates:", df["Order Date Parsed"].isna().sum())
print("Invalid ship dates:", df["Ship Date Parsed"].isna().sum())
print("Orders shipped before order date:", (df["Lead Time Days"] < 0).sum())

print("\n===== LEAD TIME SUMMARY =====")
print(df["Lead Time Days"].describe())

print("\n===== SAMPLE DATE CALCULATIONS =====")
print(
    df[
        ["Order Date", "Ship Date", "Order Date Parsed",
         "Ship Date Parsed", "Lead Time Days"]
    ].head(10).to_string(index=False)
)

print("\n===== DATE RANGE CHECK =====")

print(
    "Earliest order date:",
    df["Order Date Parsed"].min()
)

print(
    "Latest order date:",
    df["Order Date Parsed"].max()
)

print(
    "Earliest ship date:",
    df["Ship Date Parsed"].min()
)

print(
    "Latest ship date:",
    df["Ship Date Parsed"].max()
)

print("\n===== LEAD TIME FREQUENCY =====")
print(
    df["Lead Time Days"]
    .value_counts()
    .sort_index()
    .head(15)
)

print("\n===== SHIP MODE COUNTS =====")
print(df["Ship Mode"].value_counts())

print("\n===== DATE OFFSET INVESTIGATION =====")

# Compare the recorded lead time with a typical short shipping window
print("\nLead time grouped by ship mode:")
print(
    df.groupby("Ship Mode")["Lead Time Days"]
    .agg(["count", "min", "median", "mean", "max"])
    .round(2)
)

# Inspect unique lead times and their frequencies
print("\nMost common lead times:")
print(
    df["Lead Time Days"]
    .value_counts()
    .head(15)
    .to_string()
)

# Check whether order IDs contain years that differ from order dates
print("\nSample order IDs and dates:")
print(
    df[["Order ID", "Order Date", "Ship Date"]]
    .head(15)
    .to_string(index=False)
)

