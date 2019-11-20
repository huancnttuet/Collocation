# coding=utf-8
import nltk
import pandas as pd
import os
from nltk.corpus import webtext, stopwords
from read_multi_files import load_data
import xlsxwriter

bigrams = nltk.collocations.BigramAssocMeasures()
pd.set_option('display.max_rows', 500)
ROOT_DIR = os.path.dirname(os.path.abspath(
    __file__))  # This is your Project Root
SUBJECT_NAME = 'music'
# Loading the data
words = load_data("/data/complex.com/{}/*.txt".format(SUBJECT_NAME))

bigramFinder = nltk.collocations.BigramCollocationFinder.from_words(words)

# get english stopwords
en_stopwords = set(stopwords.words('english'))
# function to filter for ADJ/NN bigrams


def rightTypes(ngram):
    if '-pron-' in ngram or 't' in ngram:
        return False
    for word in ngram:
        if word in en_stopwords or word.isspace():
            return False
    acceptable_types = ('JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS')
    second_type = ('NN', 'NNS', 'NNP', 'NNPS')
    tags = nltk.pos_tag(ngram)
    if tags[0][1] in acceptable_types and tags[1][1] in second_type:
        return True
    else:
        return False


#########Phuong phap tan so (Frequency)#########
# bigrams
bigram_freq = bigramFinder.ngram_fd.items()
bigramFreqTable = pd.DataFrame(list(bigram_freq), columns=[
                               'bigram', 'freq']).sort_values(by='freq', ascending=False)
# filter bigrams
filtered_bi = bigramFreqTable[bigramFreqTable.bigram.map(
    lambda x: rightTypes(x))]
# result
print(filtered_bi.head(100))
###################################################

########Phuong phap PMI(Mutual information )#######
bigramFinder.apply_freq_filter(20)
bigramPMITable = pd.DataFrame(list(bigramFinder.score_ngrams(bigrams.pmi)), columns=[
                              'bigram', 'PMI']).sort_values(by='PMI', ascending=False)

print(bigramPMITable.head(100))
###################################################

#########Phuong phap t-test##########
bigramTtable = pd.DataFrame(list(bigramFinder.score_ngrams(bigrams.student_t)), columns=[
                            'bigram', 't']).sort_values(by='t', ascending=False)
# filters
filteredT_bi = bigramTtable[bigramTtable.bigram.map(lambda x: rightTypes(x))]
print(filteredT_bi.head(100))
######################################

######## Chi-Square ##################
bigramChiTable = pd.DataFrame(list(bigramFinder.score_ngrams(bigrams.chi_sq)), columns=[
                              'bigram', 'chi-sq']).sort_values(by='chi-sq', ascending=False)
print(bigramChiTable.head(100))
######################################

######## Likelihood ##################
bigramLikTable = pd.DataFrame(list(bigramFinder.score_ngrams(bigrams.likelihood_ratio)), columns=[
                              'bigram', 'likelihood ratio']).sort_values(by='likelihood ratio', ascending=False)
filteredLik_bi = bigramLikTable[bigramLikTable.bigram.map(
    lambda x: rightTypes(x))]
print(filteredLik_bi.head(100))
######################################


################## So sanh 5 phuong phap (Bigram Comparison) #################
freq_bi = filtered_bi.bigram.values
pmi_bi = bigramPMITable.bigram.values
t_bi = filteredT_bi.bigram.values
chi_bi = bigramChiTable.bigram.values
lik_bi = filteredLik_bi.bigram.values

bigramsCompare = pd.DataFrame([freq_bi, pmi_bi, t_bi, chi_bi, lik_bi]).T
bigramsCompare.columns = ['Frequency With Filter', 'PMI',
                          'T-test With Filter', 'Chi-Sq Test', 'Likeihood Ratio']
print(bigramsCompare)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('{}.xlsx'.format(SUBJECT_NAME), engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
filtered_bi.to_excel(writer, sheet_name='Sheet1')
bigramPMITable.to_excel(writer, sheet_name='Sheet2')
filteredT_bi.to_excel(writer, sheet_name='Sheet3')
bigramChiTable.to_excel(writer, sheet_name='Sheet4')
filteredLik_bi.to_excel(writer, sheet_name='Sheet5')
bigramsCompare.to_excel(writer, sheet_name='Sheet6')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
