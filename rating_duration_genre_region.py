import pandas as pd

df = pd.read_excel("D:/4 YEAR 2 SEMESTER/Дипломна Робота/netflix_titles.xlsx")

df['rating'] = df['rating'].fillna('Unknown')

rating_map = {
    'G': 1, 'TV-Y': 2, 'TV-Y7': 3, 'PG': 4, 'TV-G': 5,
    'TV-PG': 6, 'PG-13': 7, 'TV-14': 8, 'R': 9,
    'TV-MA': 10, 'NC-17': 11
}
df['rating_score'] = df['rating'].apply(lambda x: rating_map.get(x, 0))

def convert_duration(x):
    try:
        if 'Season' in x:
            num = int(x.split()[0])
            return num * 10 * 45
        elif 'min' in x:
            return int(x.split()[0])
    except:
        return None

df['duration_num'] = df['duration'].astype(str).apply(convert_duration)

df['main_genre'] = df['listed_in'].astype(str).apply(lambda x: x.split(',')[0].strip())

df['country'] = df['country'].astype(str).apply(lambda x: x.split(',')[0].strip() if ',' in x else x.strip())

def map_region(country):
    europe = {"Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina",
              "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia",
              "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia",
              "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands",
              "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "San Marino", "Serbia", "Slovakia",
              "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "UK", "Vatican City"}

    latin_america = {"Argentina", "Belize", "Bolivia", "Brazil", "Chile", "Colombia", "Costa Rica", "Cuba",
                     "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Honduras", "Mexico",
                     "Nicaragua", "Panama", "Paraguay", "Peru", "Uruguay", "Venezuela"}

    asia = {"Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China",
            "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan",
            "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal",
            "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore",
            "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey",
            "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"}

    if country == "United States":
        return "США"
    elif country in europe:
        return "Європа"
    elif country in latin_america:
        return "Латинська Америка"
    elif country in asia:
        return "Азія"
    else:
        return "Інші"

df['region'] = df['country'].apply(map_region)

df.to_excel("D:/4 YEAR 2 SEMESTER/Дипломна Робота/netflix_ready.xlsx", index=False)

print("Дані оброблено та збережено у файл netflix_ready.xlsx")
