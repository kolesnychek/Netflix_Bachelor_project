import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_excel("D:/4 YEAR 2 SEMESTER/Дипломна Робота/netflix_titles.xlsx")

original_df = df.copy()

knn_df = df[['type', 'country', 'rating', 'duration']].copy()

label_cols = ['type', 'country', 'rating']
label_encoders = {}

for col in label_cols:
    le = LabelEncoder()
    knn_df[col] = le.fit_transform(knn_df[col].astype(str))
    label_encoders[col] = le

knn_df['duration'] = knn_df['duration'].str.extract('(\d+)').astype(float)

imputer = KNNImputer(n_neighbors=5)
knn_imputed = imputer.fit_transform(knn_df)

imputed_df = pd.DataFrame(knn_imputed, columns=knn_df.columns)

for col in label_cols:
    le = label_encoders[col]
    imputed_df[col] = le.inverse_transform(imputed_df[col].round().astype(int))

for col in ['country', 'duration', 'rating']:
    df[col] = imputed_df[col]

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['description'] = df['description'].fillna('No description provided')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].dt.strftime('%Y-%m-%d')

df.to_excel("D:/4 YEAR 2 SEMESTER/Дипломна Робота/netflix_knn_meanings.xlsx", index=False)

print("Збережено таблицю з імпутованими значеннями: netflix_knn_meanings.xlsx")