import pandas as pd

df = pd.read_excel("netflix_titles.xlsx")

print("Розмір до очищення:", df.shape)

df_cleaned = df.drop_duplicates()

print("Розмір після очищення:", df_cleaned.shape)

df_cleaned.to_excel("netflix_cleaned.xlsx", index=False)

print("Збережено у файл netflix_cleaned.xlsx")
