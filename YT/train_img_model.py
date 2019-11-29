import json
import urllib.request
from imageio import imread


# INPUT: training data (rgb map)
# OUTPUT: trained model


def prepare_data():
    with open('data.txt') as json_file:
        data = json.load(json_file)

    features = []
    labels = []

    for video in data:
        # thumbnail = urllib.request.urlopen(data[video][2])
        # print(urllib.request.urlretrieve(data[video][2]))
        image = imread(data[video][2])
        print(image)


def train_model():
    prepare_data()


def main():
    train_model()


if __name__ == "__main__":
    main()
