import os
import csv
from nltk.tokenize import wordpunct_tokenize
import numpy as np
import pandas as pd


# DATA LOAD AND CLEANING
PREFIX = "./Data/"
d_aux_1 = []
d_aux_2 = []
data_clean = []
features = []
# Load data.csv
data_aux = pd.read_csv(PREFIX+'data.csv')
data = np.array(data_aux)

def tokenize(name):
     return wordpunct_tokenize(name)    

def data_cleaner(data):
    for doc in data:
        d_aux_1 = [str.lower(doc[0]),str.lower(doc[1]), str.lower(doc[2])]
        d_aux_2.append(d_aux_1)

    return d_aux_2

data_clean = data_cleaner(data)

# FEATURE EXTRACTION
q_1 = "glucose in blood"
q_2 = "bilirubin in plasma"
q_3 = "White blood cells count"

def feature_extractor(query):
    q_token = list(map(str.lower,tokenize(query)))
    q_length = len(q_token)
    n = 0
    f_percentage = 0
    f_1 = []
    f_2 = 0
    f_3 = 0
    for doc in data_clean:
        for token in q_token:
            # First feature --> % of the words contain in the query that are in the name
            if token in doc[0]:
                n = n+1
            # Second feature --> Yes/No depending if a word of the query is in the attribute component
            if token in doc[1]:
                f_2=1
            # Third feature --> Yes/No depending if a word of the query is in the attribute system
            if token in doc[2]:
                f_3_=1
        f_1_aux = n/q_length
        features.append([f_1_aux,f_2,f_3])
        n = 0
        f_2 = 0
        f_3 = 0
    return features
    
feature_extractor(q_1)
feature_extractor(q_2)
feature_extractor(q_3)


