import glob
import os
from nltk.corpus import webtext

ROOT_DIR = os.path.dirname(os.path.abspath(
    __file__))  # This is your Project Root

def load_data(folder_name):
    filter_list = ['<', '>', '</', '/>', ' ','brandâ','isnâ','z','cm','thereâ','doesnâ','canâ','didnâ','','+','â','ä','theyâ','šre','donâ','maniăšre','k', 'youâ','heâ','weâ','thatâ' ,'.', ',', '.&', ';&', 'nbsp', '://', '*', ',...','...', '!!!', '!', '?', '%','@','!!!),', '!!=)**', '."', 'da', 'awf', '(', ')', '"', '&', ';', '', ' ', 'itâ', 'iâ', '/', '!!', 'garçons', 'endommagés', 'lt', 'gt', 'w', 'o', 'http', 'www', 'ďťż', 'b', 'c', 'd','e', 'f', 'g', 'h', '58', '2004','02','00','2002','\'','-',':','a','30','am','pm','l','6','20','1','t','2000','01','18', '2003','2001', 's', ',"', '07']
    path_name_lists = glob.glob(ROOT_DIR + folder_name)
    results = []
    # Loading the data
    for path_name in path_name_lists:
        words = [w.lower() for w in webtext.words(path_name)]
        filter_words = [word for word in words if word not in filter_list]
        results.extend(filter_words)
    return results


print(len(load_data("/data/data/*.txt")))
