import json
import nltk
from nltk.corpus import stopwords
from sklearn import linear_model
from sklearn.feature_extraction.text import CountVectorizer

# regressor will be trained here

# INPUT: training data (dictionary)
# OUTPUT: trained model


def prepare_data():
    with open('data.txt') as json_file:
        data = json.load(json_file)

    features = []
    labels = []

    for video in data:
        features.append(data[video][0].lower())
        ratio = int(data[video][3]) / int(data[video][1])
        labels.append(ratio)

    ngram_vectorizer = CountVectorizer()
    fit_vectorizer = ngram_vectorizer.fit_transform(features)

    # print(ngram_vectorizer.get_feature_names())
    features = fit_vectorizer.toarray()

    return features, labels, ngram_vectorizer


def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return filtered_sentence


def train_model():
    features, labels, vectorizer = prepare_data()
    print(features, labels)
    regr = linear_model.LinearRegression()
    regr.fit(features, labels)

    test = vectorizer.transform(['awersesf'])
    print(regr.predict(test))


def main():
    train_model()


if __name__ == "__main__":
    main()


'''
stop words remove
part of speech tagging
'''