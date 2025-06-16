import matplotlib.pyplot as plt
import polars as pl

df = pl.read_csv("Databases/uzbekistan_population.csv")

uzbekistan_data = df.filter(pl.col("Klassifikator") == "O‘zbekiston Respublikasi")
year_columns = [str(y) for y in range(2010, 2026)]
yearly_data = uzbekistan_data.select(year_columns).melt(variable_name="Year", value_name="Population")
yearly_pd = yearly_data.to_pandas()

plt.figure(figsize=(12, 6))
plt.bar(yearly_pd["Year"], yearly_pd["Population"], color='skyblue')
plt.title("O'zbekiston Respublikasi aholi soni (2010–2025)")
plt.xlabel("Yil")
plt.ylabel("Aholi soni (minglarda)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
