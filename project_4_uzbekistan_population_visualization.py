import matplotlib.pyplot as plt

import polars as pl

df = pl.read_csv("Databases/uzbekistan.csv")

labels = df["Boʻlinishi"]
sizes = df["Aholisi"]

plt.figure(figsize = (8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("O'zbekiston Respublikasi viloyatlaridagi aholi")

plt.show()