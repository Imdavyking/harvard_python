import nltk
import os
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage python sentiment.py corpus")
    positives, negatives = load_data(sys.argv[1])

    words = set()

    for document in positives:
        words.update(document)
    for document in negatives:
        words.update(document)

    training = []
    training.extend(generate_features(positives, words, 'Positive'))
    training.extend(generate_features(negatives, words, 'Negative'))

    classifier = nltk.NaiveBayesClassifier.train(training)

    s = input("s: ")
    result = (classify(classifier, s,words))

    for key in result.samples():
        print(f"{key}: {result.prob(key):.4f}")

    

def generate_features(documents, words, label):
    features = []
    for document in documents:
        features.append((extract_features(document, words), label))
    return features


def extract_features(document, words):
    document_words = set(document)
    features = {}
    for word in words:
        features[word] = (word in document_words)
    return features
    
def classify(classifier, s, words):
    return classifier.prob_classify(extract_features(s.split(), words))

def load_data(directory):
    positives = []
    # postives.txt
    with open(os.path.join(directory, 'positives.txt')) as f:
        for line in f:
            positives.append(line.strip().split())
    negatives = []
    with open(os.path.join(directory, 'negatives.txt')) as f:
        for line in f:
            negatives.append(line.strip().split())

    return positives, negatives


if __name__ == "__main__":
    main()