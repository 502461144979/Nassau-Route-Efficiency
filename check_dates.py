
import pandas as pd

df = pd.read_csv("Nassau Candy Distributor.csv")

df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%d-%m-%Y", errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="%d-%m-%Y", errors="coerce"
)

# Compare each ship date with its order date
df["Lead Time"] = (df["Ship Date"] - df["Order Date"]).dt.days

print("===== LEAD TIME GROUPS =====")
print(
    df.groupby("Ship Mode")["Lead Time"]
    .agg(["min", "median", "max"])
)

print("\n===== ORDER AND SHIP DATE YEARS =====")
print("Order date years:")
print(df["Order Date"].dt.year.value_counts().sort_index())

print("\nShip date years:")
print(df["Ship Date"].dt.year.value_counts().sort_index())

print("\n===== SAME ORDER ID, MULTIPLE DATES =====")
print(
    df.groupby("Order ID")
    .agg(
        rows=("Row ID", "count"),
        order_dates=("Order Date", "nunique"),
        ship_dates=("Ship Date", "nunique")
    )
    .describe()
)
