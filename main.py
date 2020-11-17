from quicksort import quicksort
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from knn import Knn


def main():
    col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    iris = pd.read_csv('./iris.data', header=None, names=col_names)
    iris_class = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    iris['species_num'] = [iris_class[i] for i in iris.species]
    X = iris.drop(['species', 'species_num'], axis=1).to_numpy()
    y = iris.species_num.to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    kr = Knn(3)
    # knn = KNeighborsClassifier(3)

    # model = knn.fit(X_train, y_train)
    kr.fit(X_train, y_train)

    # p = model.predict(X_test)
    p2 = kr.predict(X_test)
    correct = 0
    total = 0
    for pred in zip(p2, y_test):
        if pred[0] == pred[1]:
            correct += 1
        total += 1
    print("acc :", correct / total)


if __name__ == '__main__':
    main()
