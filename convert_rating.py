import pandas as pd

input_file = "netflix_cleaned.xlsx"
output_file = "netflix_converted.xlsx"

df = pd.read_excel(input_file)

rating_map = {
    'G': 1,
    'TV-Y': 2,
    'TV-Y7': 3,
    'PG': 4,
    'TV-G': 5,
    'TV-PG': 6,
    'PG-13': 7,
    'TV-14': 8,
    'R': 9,
    'TV-MA': 10,
    'NC-17': 11
}

df['rating'] = df['rating'].fillna('Unknown')

df['rating_score'] = df['rating'].apply(lambda x: rating_map.get(x, 0))

df.to_excel(output_file, index=False)
print("Файл успішно збережено як", output_file)