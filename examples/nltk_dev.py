import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import CategorizedBracketParseCorpusReader
from nltk.corpus import ChunkedCorpusReader # May be a solid option for  me
from nltk.corpus import CategorizedTaggedCorpusReader # number 2 so far
from nltk.corpus import IEERCorpusReader # HOLD UP 
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Download the movie_reviews corpus if not already downloaded
nltk.download('movie_reviews')

# Define a function to extract features from text
def extract_features(text):
    words = word_tokenize(text)
    return {word: True for word in words}

# Load movie reviews and prepare the dataset
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents for randomness
random.shuffle(documents)

# Create feature sets and split the dataset
featuresets = [(extract_features(words), category) for (words, category) in documents]
train_set, test_set = featuresets[:1500], featuresets[1500:]

# Train a text classification model (SVM) using TF-IDF features
tfidf_vectorizer = TfidfVectorizer()
X_train = [tfidf_vectorizer.fit_transform([x[0]])[0] for x in train_set]
y_train = [x[1] for x in train_set]

svm_classifier = SklearnClassifier(SVC(kernel='linear'))
svm_classifier.train(list(zip(X_train, y_train)))

# Test the model
X_test = [tfidf_vectorizer.transform([x[0]])[0] for x in test_set]
y_test = [x[1] for x in test_set]

predictions = svm_classifier.classify_many(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Tokenize a sample sentence
sample_sentence = "NLTK is a powerful library for natural language processing."
tokens = word_tokenize(sample_sentence)
print("Tokenized Sentence:")
print(tokens)
