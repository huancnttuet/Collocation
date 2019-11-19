# coding=utf-8
import nltk
import pandas as pd
import os
from nltk.corpus import webtext, stopwords
from read_multi_files import load_data
trigrams = nltk.collocations.TrigramAssocMeasures()

ROOT_DIR = os.path.dirname(os.path.abspath(
    __file__))  # This is your Project Root

# Loading the data
words = load_data("/data/data/*.txt")

trigramFinder = nltk.collocations.TrigramCollocationFinder.from_words(words)

# get english stopwords
en_stopwords = set(stopwords.words('english'))
# function to filter for ADJ/NN bigrams


def rightTypesTri(ngram):
    if '-pron-' in ngram or '' in ngram or ' 'in ngram or '  ' in ngram or 't' in ngram:
        return False
    for word in ngram:
        if word in en_stopwords:
            return False
    first_type = ('JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS')
    third_type = ('JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS')
    tags = nltk.pos_tag(ngram)
    if tags[0][1] in first_type and tags[2][1] in third_type:
        return True
    else:
        return False


#########Phuong phap tan so (Frequency)#########
# bigrams
trigram_freq = trigramFinder.ngram_fd.items()
trigramFreqTable = pd.DataFrame(list(trigram_freq), columns=[
                                'trigram', 'freq']).sort_values(by='freq', ascending=False)
# filter bigrams
filtered_tri = trigramFreqTable[trigramFreqTable.trigram.map(
    lambda x: rightTypesTri(x))]
# result
print(filtered_tri)
###################################################

########Phuong phap PMI(Mutual information )#######
trigramFinder.apply_freq_filter(20)
trigramPMITable = pd.DataFrame(list(trigramFinder.score_ngrams(trigrams.pmi)), columns=[
                               'trigram', 'PMI']).sort_values(by='PMI', ascending=False)

print(trigramPMITable)
###################################################

#########Phuong phap t-test##########
trigramTtable = pd.DataFrame(list(trigramFinder.score_ngrams(trigrams.student_t)), columns=[
                             'trigram', 't']).sort_values(by='t', ascending=False)
# filters
filteredT_tri = trigramTtable[trigramTtable.trigram.map(
    lambda x: rightTypesTri(x))]
print(filteredT_tri)
######################################

######## Chi-Square ##################
trigramChiTable = pd.DataFrame(list(trigramFinder.score_ngrams(trigrams.chi_sq)), columns=[
                               'trigram', 'chi-sq']).sort_values(by='chi-sq', ascending=False)
print(trigramChiTable)
######################################

######## Likelihood ##################
trigramLikTable = pd.DataFrame(list(trigramFinder.score_ngrams(trigrams.likelihood_ratio)), columns=[
                               'trigram', 'likelihood ratio']).sort_values(by='likelihood ratio', ascending=False)
filteredLik_tri = trigramLikTable[trigramLikTable.trigram.map(
    lambda x: rightTypesTri(x))]
print(filteredLik_tri)
######################################


################## So sanh 5 phuong phap (Bigram Comparison) #################
freq_tri = filtered_tri[:20].trigram.values
pmi_tri = trigramPMITable[:20].trigram.values
t_tri = filteredT_tri[:20].trigram.values
chi_tri = trigramChiTable[:20].trigram.values
lik_tri = filteredLik_tri[:20].trigram.values

trigramsCompare = pd.DataFrame([freq_tri, pmi_tri, t_tri, chi_tri, lik_tri]).T
trigramsCompare.columns = ['Frequency With Filter', 'PMI',
                           'T-test With Filter', 'Chi-Sq Test', 'Likeihood Ratio']
print(trigramsCompare)
