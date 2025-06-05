import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from collections import Counter

df = pd.read_excel('D:/4 YEAR 2 SEMESTER/Дипломна Робота/netflix_ready.xlsx')

df['desc_length'] = df['description'].fillna('').apply(lambda x: len(x.split()))

df = df.dropna(subset=['release_year', 'duration_num', 'rating_score', 'region'])

df_series = df[df['type'] == 'TV Show']

def extract_top(df_region, top_genres_n=10, top_directors_n=10, top_actors_n=20):
    genre_counts = df_region['main_genre'].value_counts()
    top_genres = genre_counts.nlargest(top_genres_n).index.tolist()
    if len(top_genres) == 0:
        top_genres = genre_counts.index.tolist()
    top_directors = df_region['director'].dropna().value_counts().nlargest(top_directors_n).index.tolist()
    actors = []
    for cast in df_region['cast'].dropna():
        actors += [actor.strip() for actor in cast.split(',')]
    top_actors = [actor for actor, _ in Counter(actors).most_common(top_actors_n)]
    return top_genres, top_directors, top_actors

def run_linear_regression(df):
    output_rows = []

    for region in ['США', 'Інші', 'Азія', 'Європа', 'Латинська Америка']:
        df_r = df[df['region'] == region]
        if len(df_r) < 20:
            continue

        top_genres, top_directors, top_actors = extract_top(df_r)

        df_r = df_r.copy()
        df_r['genres_top'] = df_r['main_genre'].apply(lambda x: 1 if x in top_genres else 0)
        df_r['director_top'] = df_r['director'].apply(lambda x: 1 if x in top_directors else 0)
        df_r['actors_top'] = df_r['cast'].apply(
            lambda x: 1 if pd.notna(x) and any(actor.strip() in top_actors for actor in x.split(',')) else 0
        )

        X = df_r[['release_year', 'duration_num', 'genres_top', 'desc_length', 'director_top', 'actors_top']]
        y = df_r['rating_score']

        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)

        coefs = dict(zip(X.columns, model.coef_))

        row = {
            'region': region,
            'const': round(model.intercept_, 4),
            'R_squared': round(r2_score(y, y_pred), 4),
            'release_year': round(coefs.get('release_year', 0), 4),
            'duration_num': round(coefs.get('duration_num', 0), 4),
            'genres_top': round(coefs.get('genres_top', 0), 4),
            'desc_length': round(coefs.get('desc_length', 0), 4),
            'director_top': round(coefs.get('director_top', 0), 4),
            'actors_top': round(coefs.get('actors_top', 0), 4),
        }

        output_rows.append(row)

    return pd.DataFrame(output_rows)

results_series = run_linear_regression(df_series)

pd.set_option('display.max_columns', None)
print("\nТаблиця результатів для серіалів по регіонах (звичайна регресія):\n")
print(results_series.to_string(index=False))
