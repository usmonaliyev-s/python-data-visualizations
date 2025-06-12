import polars as pl

import matplotlib.pyplot as plt


df = pl.read_csv("Databases/covid_19.csv")

# print(df.head())
# print(df.columns)
# print(df.shape)

uzbekistan_df = df.filter(pl.col("Country/Region") == "Uzbekistan")

uzbekistan_df = uzbekistan_df.with_columns(
    pl.col("Date").str.strptime(pl.Date, "%Y-%m-%d")
)


uzbekistan_grouped = (
    uzbekistan_df
    .group_by("Date")
    .agg([
        pl.col("Confirmed").sum().alias("Confirmed"),
        pl.col("Deaths").sum().alias("Deaths"),
        pl.col("Recovered").sum().alias("Recovered"),
    ])
    .sort("Date")
)


df_pd = uzbekistan_grouped.to_pandas()

plt.figure(figsize=(12, 6))

plt.plot(df_pd["Date"], df_pd["Confirmed"], label="Confirmed", color="blue")
plt.plot(df_pd["Date"], df_pd["Deaths"], label="Deaths", color="red")
plt.plot(df_pd["Date"], df_pd["Recovered"], label="Recovered", color="green")

plt.xlabel("Date")
plt.ylabel("Cases")
plt.title("COVID-19 Trends in Uzbekistan")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
