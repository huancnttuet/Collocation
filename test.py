# import os
# import pandas as pd
# from nltk.corpus import webtext
# # use to find bigrams, which are pairs of words
# from nltk.collocations import BigramCollocationFinder
# from nltk.metrics import BigramAssocMeasures
# from nltk.corpus import stopwords
# # Trigram
# from nltk.collocations import TrigramCollocationFinder
# from nltk.metrics import TrigramAssocMeasures

# ROOT_DIR = os.path.dirname(os.path.abspath(
#     __file__))  # This is your Project Root

# # Loading the data
# # words = [w.lower() for w in webtext.words(
# #     ROOT_DIR+'/data/newstest.txt')]

# words = [w.lower() for w in webtext.words('grail.txt')]
# stopset = set(stopwords.words('english'))


# def filter_stops(w): return len(w) < 3 or w in stopset


# biagram_collocation = BigramCollocationFinder.from_words(words)
# biagram_collocation.apply_word_filter(filter_stops)
# a = biagram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 1500)
# table = pd.DataFrame(list(a), columns=[
#     'bigram', 'none'])
# print(table)
# print(a)
# trigram_collocation = TrigramCollocationFinder.from_words(words)
# trigram_collocation.apply_word_filter(filter_stops)


# b = trigram_collocation.nbest(TrigramAssocMeasures.likelihood_ratio, 15)
# print(b)

# # bigrams
# bigram_freq = biagram_collocation.ngram_fd.items()
# bigramFreqTable = pd.DataFrame(list(bigram_freq), columns=[
#                                'bigram', 'freq']).sort_values(by='freq', ascending=False)
# print(bigramFreqTable)
# print(bigram_freq)
# # trigrams
# trigram_freq = trigram_collocation.ngram_fd.items()
# trigramFreqTable = pd.DataFrame(list(trigram_freq), columns=[
#                                 'trigram', 'freq']).sort_values(by='freq', ascending=False)

# print(trigramFreqTable)
# trigramFreqTable.dropna(inplace = True)
# data_dict = trigramFreqTable.to_dict()
# print(data_dict)
# # # filter for only those with more than 20 occurences
# # bigramFinder.apply_freq_filter(20)
# # trigramFinder.apply_freq_filter(20)
# # bigramPMITable = pd.DataFrame(list(bigramFinder.score_ngrams(bigrams.pmi)), columns=[
# #                               'bigram', 'PMI']).sort_values(by='PMI', ascending=False)
# # trigramPMITable = pd.DataFrame(list(trigramFinder.score_ngrams(trigrams.pmi)), columns=[
# #                                'trigram', 'PMI']).sort_values(by='PMI', ascending=False)


import pandas as pd
import xlsxwriter

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
