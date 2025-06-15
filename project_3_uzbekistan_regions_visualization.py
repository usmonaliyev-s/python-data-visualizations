import matplotlib.pyplot as plt

import polars as pl

df = pl.read_csv("Databases/uzbekistan.csv")

labels = df["Boʻlinishi"]
sizes = df["Maydoni (kv.km)"]

plt.figure(figsize = (8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("O'zbekiston Respublikasi viloyat maydonlari")

plt.show()