import numpy as np


class Knn:
    def __init__(self, k):
        self.k = k
        self.classes = {}
        pass

    def fit(self, X, y):
        for pair in zip(X, y):
            c = pair[1]
            if not self.classes.keys().__contains__(c):
                self.classes[c] = []
            self.classes[c].append(pair[0])

    def debug(self):
        for k in self.classes.keys():
            print(len(self.classes[k]))

    @staticmethod
    def most_frequent(List):
        counter = 0
        num = List[0]

        for i in List:
            curr_frequency = List.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                num = i

        return num

    def predict(self, X):
        output = []
        for element in X:
            d = []
            for c in self.classes.keys():
                for value in self.classes[c]:
                    d.append([np.linalg.norm(element - value), c])
            d.sort()
            classes = []
            for neighbor in d[:self.k]:
                classes.append(neighbor[1])
            most_common = self.most_frequent(classes)
            output.append(most_common)
        return output
