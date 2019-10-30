import os
from nltk.corpus import webtext
# use to find bigrams, which are pairs of words
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords

ROOT_DIR = os.path.dirname(os.path.abspath(
    __file__))  # This is your Project Root

# Loading the data
words = [w.lower() for w in webtext.words(ROOT_DIR+'/data/testdata.txt')]

stopset = set(stopwords.words('english'))


def filter_stops(w): return len(w) < 3 or w in stopset


biagram_collocation = BigramCollocationFinder.from_words(words)
biagram_collocation.apply_word_filter(filter_stops)
a = biagram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 15)
print(a)
