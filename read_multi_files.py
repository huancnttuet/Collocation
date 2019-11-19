# coding=utf-8
import glob
import os
from nltk.corpus import webtext

ROOT_DIR = os.path.dirname(os.path.abspath(
    __file__))  # This is your Project Root

def load_data(folder_name):
    filter_list = ['nfsâ','â','nov','com','oct','octn','theâ','aimăš','maniăšre','cm','http','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    path_name_lists = glob.glob(ROOT_DIR + folder_name)
    results = []
    # Loading the data
    for path_name in path_name_lists:
        words = [w.lower() for w in webtext.words(path_name)]
        filter_words = [word for word in words if word not in filter_list and word.isalpha()]
        results.extend(filter_words)
    return results


print(len(load_data("/data/data/*.txt")))
