import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("D:/4 YEAR 2 SEMESTER/Дипломна Робота/netflix_ready.xlsx")

features = df.groupby("region").agg({
    "rating_score": "mean",                      
    "duration_num": "mean",                     
    "main_genre": pd.Series.nunique,             
    "release_year": lambda x: (x >= 2018).sum()  
}).reset_index()

features.columns = ['region', 'avg_rating', 'avg_duration', 'genre_variety', 'recent_production']

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features[['avg_rating', 'avg_duration', 'genre_variety', 'recent_production']])

inertia = []
K_range = range(1, 6)

for k in K_range:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(scaled_features)
    inertia.append(model.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, marker='o', linestyle='-')
plt.title('Метод ліктя для визначення оптимальної кількості кластерів')
plt.xlabel('Кількість кластерів (k)')
plt.ylabel('Інерція')
plt.grid(True)
plt.tight_layout()
plt.show()

optimal_k = 3
model = KMeans(n_clusters=optimal_k, random_state=42)
features['cluster'] = model.fit_predict(scaled_features)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=features,
                x='avg_duration',
                y='avg_rating',
                hue='cluster',
                palette='Set2',
                s=150)

for i in range(features.shape[0]):
    plt.text(x=features.avg_duration[i] + 1,
             y=features.avg_rating[i] + 0.01,
             s=features.region[i],
             fontsize=9)

plt.title('Кластеризація регіонів Netflix за характеристиками контенту')
plt.xlabel('Середня тривалість (хв)')
plt.ylabel('Середній рейтинг')
plt.grid(True)
plt.tight_layout()
plt.show()

print("Результати кластеризації:")
print(features[['region', 'avg_rating', 'avg_duration', 'genre_variety', 'recent_production', 'cluster']])
