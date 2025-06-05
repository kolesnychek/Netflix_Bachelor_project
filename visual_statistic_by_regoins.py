import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('D:/4 YEAR 2 SEMESTER/Дипломна Робота/netflix_ready.xlsx')

rating_labels = {
    0: "TV-MA+", 1: "G", 2: "TV-Y", 3: "TV-Y7", 4: "PG",
    5: "TV-G", 6: "TV-PG", 7: "PG-13", 8: "TV-14", 9: "R",
    10: "TV-MA", 11: "NC-17"
}

regions = df['region'].unique()

for region in regions:
    region_data = df[df['region'] == region]
    rating_counts = region_data['rating_score'].value_counts().sort_index()

    labels = [rating_labels.get(i, str(i)) for i in rating_counts.index]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=labels, y=rating_counts.values, palette='viridis')
    plt.title(f'Розподіл рейтингів для регіону: {region}', fontsize=14)
    plt.xlabel('Рейтинг контенту', fontsize=12)
    plt.ylabel('Кількість серіалів та фільмів', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


if 'main_genre' not in df.columns:
    print("Увага: відсутня колонка main_genre!")
else:
    regions = df['region'].unique()

    for region in regions:
        region_data = df[df['region'] == region]
        genre_counts = region_data['main_genre'].value_counts().sort_values(ascending=False)

        plt.figure(figsize=(10, 6))
        sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='magma')
        plt.title(f'Розподіл жанрів у регіоні: {region}', fontsize=14)
        plt.xlabel('Кількість серіалів та фільмів', fontsize=12)
        plt.ylabel('Жанри', fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

