import json
import urllib.request
from imageio import imread
from sklearn.svm import SVR
import numpy
import pickle


# INPUT: training data (rgb map)
# OUTPUT: trained model


def preprocess_data():
    with open('data.txt') as json_file:
        data = json.load(json_file)

    features = []
    labels = []

    for video in data:
        features.append(imread(data[video][2]))
        ratio = int(data[video][3]) / int(data[video][1])
        labels.append(ratio)

    return features, labels


def train_model():
    features, labels = preprocess_data()
    regr = SVR(kernel='linear')
    regr.fit(features, labels)
    pickle.dump(regr, open('models/img_model.sav', 'wb'))


def test_model():
    model = pickle.load(open('models/img_model.sav', 'rb'))
    prediction = model.predict(img)
    print(prediction)


def main():
    preprocess_data()
    train_model()
    test_model()


if __name__ == "__main__":
    main()
