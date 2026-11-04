
import pandas as pd

df = pd.read_csv("Nassau Candy Distributor.csv")

# Remove leading and trailing spaces from geographic labels
df["State/Province"] = (
    df["State/Province"].astype("string").str.strip()
)

df["Region"] = (
    df["Region"].astype("string").str.strip()
)

print("===== UNIQUE STATES / PROVINCES =====")
states = sorted(df["State/Province"].dropna().unique())
print("Number of unique states/provinces:", len(states))
print(states)

print("\n===== REGIONS =====")
print(df["Region"].value_counts(dropna=False))

print("\n===== COUNTRIES / REGIONS =====")
print(df["Country/Region"].value_counts(dropna=False))

print("\n===== MISSING GEOGRAPHIC VALUES =====")
print(
    df[["State/Province", "Region", "City", "Country/Region"]]
    .isna()
    .sum()
)

print("\n===== TOP 10 CUSTOMER STATES =====")
print(
    df["State/Province"]
    .value_counts()
    .head(10)
)
