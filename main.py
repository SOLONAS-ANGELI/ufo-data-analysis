"""
UFO Sightings Data Analysis

- Data cleaning
- Time analysis
- Events per year visualization
- Top cities & shapes
"""


import pandas as pd

df = pd.read_csv("data/data.csv")

print(df.head())

print("\nINFO:")
print(df.info())

print("\nSTATS:")
print(df.describe())

print("\nMISSING VALUES:")
print(df.isnull().sum())

df = df.dropna()

print("\nAFTER CLEANING:")
print(df.isnull().sum())

df["Time"] = pd.to_datetime(df["Time"], errors="coerce")

df["Year"] = df["Time"].dt.year

print("\nYEARS:")
print(df["Year"].head())
events_per_year = df.groupby("Year").size()

print("\nEVENTS PER YEAR:")
print(events_per_year.head(10))
events_per_year = df.groupby("Year").size().sort_values(ascending=False)

print("\nTOP YEARS (MOST EVENTS):")
print(events_per_year.head(10))

import matplotlib.pyplot as plt

events_per_year_sorted = df.groupby("Year").size().sort_index()

plt.figure(figsize=(10,5))

events_per_year_sorted.plot(figsize=(10,5), linewidth=2)

max_year = events_per_year_sorted.idxmax()
max_value = events_per_year_sorted.max()

plt.scatter(max_year, max_value)

plt.annotate("Peak",
             (max_year, max_value),
             textcoords="offset points",
             xytext=(0,10),
             ha='center')

print("\nMOST ACTIVE YEAR:")
print(max_year, "->", max_value)

plt.title("Events per Year")
plt.xlabel("Year")
plt.ylabel("Number of Events")

plt.grid(True)
plt.show()

top_cities = df["City"].value_counts().head(10)

print("\nTOP CITIES:")
print(top_cities)

top_shapes = df["Shape Reported"].value_counts().head(10)

print("\nTOP SHAPES:")
print(top_shapes)