import pandas as pd

input_file = "netflix_converted.xlsx"
output_file = "netflix_titles.xlsx"

df = pd.read_excel(input_file)

rating_map = {
    'G': 1, 'TV-Y': 1, 'TV-Y7': 2, 'PG': 3, 'TV-G': 3, 'TV-PG': 4,
    'PG-13': 5, 'TV-14': 6, 'R': 7, 'TV-MA': 8, 'NC-17': 9
}

df['rating'] = df['rating'].fillna('Unknown')
df['rating_score'] = df['rating'].apply(lambda x: rating_map.get(x, 0))

def convert_duration(x):
    try:
        if 'Season' in x:
            num = int(x.split()[0])
            return num * 10 * 45
        elif 'min' in x:
            return int(x.split()[0])
        else:
            return None
    except:
        return None

df['duration_num'] = df['duration'].apply(lambda x: convert_duration(str(x)))

df.to_excel(output_file, index=False)

print("Таблиця збережена як", output_file)
