import numpy as np
import pickle  # Сереализация (рассол, соленье)
import re
from Stemmer import Stemmer  # Получение правильной формы слова
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline


def text_cleaner(text: str):
    text = text.lower()
    stemmer = Stemmer("russian")  # Выбор языка на котором будут входные данные
    text = " ".join(stemmer.stemWords(text.split()))
    text = re.sub(r"\b\d+\b", "digit", text)  # По идее заменяет цифры ! (на что пока не понял)
    return text


def get_data():  # Загружаем данные для обучения из файла
    data = {"text": [], "tag": []}
    for line in open("data2.txt"):
        if not("#" in line):
            row = line.split("@")
            data["text"] += [row[0]]
            data["tag"] += [row[1]]
    return data


def train(data, validation_split=0.1):  # Обучение нейросети
    data_len = len(data["text"])
    indices = np.arange(data_len)  # Нормально распределённые значения в диапазоне
    np.random.shuffle(indices)
    X = [data["text"][i] for i in indices]
    Y = [data["tag"][i] for i in indices]
    new_validation_split = int(validation_split * data_len)

    return {"train": {"x": X[:-new_validation_split], "y": Y[:-new_validation_split]},
            "test": {"x": X[-new_validation_split:], "y": Y[-new_validation_split:]}}


def openai():
    data = get_data()
    D = train(data)
    text_clf = Pipeline([("tfidf", TfidfVectorizer()), ("clf", SGDClassifier(loss="hinge")),])
    text_clf.fit(D["train"]["x"], D["train"]["y"])
    # predicted = text_clf.predict(D["train"]["x"])
    return text_clf


def save(model):
    pickle.dump(model, open("model2.sav", "wb"))


def load(file="model.sav"):
    return pickle.load(open(file, "rb"))


def main():
    text_clf = openai()  # Для обучения нейронки на наборе правильной информации
    # text_clf = load()  # Для продолжения работы с уже обученной нейронкой
    qwe = list()
    qwe.append("вернутся назад")
    predicted = text_clf.predict(qwe)
    print(predicted[0])
    save(text_clf)
    return


if __name__ == "__main__":
    main()
