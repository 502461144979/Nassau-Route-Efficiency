
import pandas as pd

# Load the dataset
df = pd.read_csv("Nassau Candy Distributor.csv")

# Assign products to factories
factory_map = {
    "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
    "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
    "Laffy Taffy": "Sugar Shack",
    "SweeTARTS": "Sugar Shack",
    "Nerds": "Sugar Shack",
    "Fun Dip": "Sugar Shack",
    "Fizzy Lifting Drinks": "Sugar Shack",
    "Everlasting Gobstopper": "Secret Factory",
    "Hair Toffee": "The Other Factory",
    "Lickable Wallpaper": "Secret Factory",
    "Wonka Gum": "Secret Factory",
    "Kazookles": "The Other Factory",
}

df["Factory"] = df["Product Name"].map(factory_map)

# Build factory-to-customer-state routes
df["State/Province"] = (
    df["State/Province"].astype("string").str.strip()
)

route_summary = (
    df.groupby(["Factory", "State/Province"], dropna=False)
    .agg(
        Row_Count=("Row ID", "count"),
        Unique_Orders=("Order ID", "nunique"),
        Total_Sales=("Sales", "sum"),
        Total_Units=("Units", "sum")
    )
    .reset_index()
    .sort_values("Row_Count", ascending=False)
)

print("===== ROUTE ANALYSIS SUMMARY =====")
print("Number of factory-to-state routes:", len(route_summary))

print("\n===== TOP 10 ROUTES BY ROW COUNT =====")
print(route_summary.head(10).to_string(index=False))

print("\n===== NUMBER OF STATES SERVED BY FACTORY =====")
print(
    df.groupby("Factory")["State/Province"]
    .nunique()
    .sort_values(ascending=False)
)

# Save the route summary for later dashboard use
route_summary.to_csv("route_summary.csv", index=False)

print("\nSaved route summary to route_summary.csv")
