
import pandas as pd

# Map each product to its assigned factory
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

df = pd.read_csv("Nassau Candy Distributor.csv")

df["Factory"] = df["Product Name"].map(factory_map)

print("===== FACTORY MAPPING CHECK =====")
print("Total rows:", len(df))
print("Products found in mapping:", df["Factory"].notna().sum())
print("Rows with unmapped products:", df["Factory"].isna().sum())

if df["Factory"].isna().any():
    print("\nUnmapped product names:")
    print(df.loc[df["Factory"].isna(), "Product Name"].unique())
else:
    print("\nAll products have a factory mapping!")

print("\n===== ROWS BY FACTORY =====")
print(df["Factory"].value_counts())
