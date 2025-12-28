import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


class Recommender:
    def __init__(self, data_path: str):
        self.df = pd.read_csv(data_path)
        russian_stop_words = [
    "и", "в", "во", "не", "что", "он", "на", "я", "с", "со", "как", "а", 
    "то", "все", "она", "так", "его", "но", "да", "ты", "к", "у", "же", 
    "вы", "за", "бы", "по", "только", "ее", "мне", "было", "вот", "от",
    "меня", "еще", "нет", "о", "из", "ему", "теперь", "даже"
]
        # Создаём колонку description для TF-IDF
        self.df["description"] = self.df["description"].fillna("")  # на случай пропусков
        self.vectorizer = TfidfVectorizer(stop_words="russian_stop_words")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["description"])

    def recommend(self, title: str, top_n: int = 5):
        title = title.strip().lower()
        # Создаём колонку с чистым названием без года и в нижнем регистре
        self.df["title_clean"] = (self.df["title"].str.lower().str.strip())
        # Поиск по подстроке
        matches = self.df[self.df["title_clean"].str.contains(title)]
        if matches.empty:
            return "Фильм не найден в базе. Попробуйте другое название."
        idx = matches.index[0]
        # Косинусное сходство для рекомендаций
        cosine_sim = cosine_similarity(self.tfidf_matrix[idx], self.tfidf_matrix).flatten()
        similar_indices = cosine_sim.argsort()[::-1][1:top_n+1]
        recommended = self.df.iloc[similar_indices][["title", "description"]].to_dict(orient="records")
        return recommended

    def get_random(self, n: int = 1):
        return self.df.sample(n)[["title", "description"]].to_dict(orient="records")