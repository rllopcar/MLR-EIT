import os
import csv
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer
import numpy as np
import pandas as pd


# DATA LOAD AND CLEANING
PREFIX = "./Data/"
d_aux_1 = []
d_aux_2 = []
data_clean = []

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
    features = []
    
    q_token = list(map(str.lower,tokenize(query)))
    q_length = len(q_token)
    
    n = 0
    f_percentage = 0
    f_1 = []
    f_2 = 0
    f_3 = 0
    for doc in data_clean:
        aux_doc_0 = list(map(str.lower,tokenize(doc[0])))
        aux_doc_1 = list(map(str.lower,tokenize(doc[1])))
        aux_doc_2 = list(map(str.lower,tokenize(doc[2])))
        for token in q_token:
            token_aux = ' '+token
            doc[0] = ' '+doc[0]+' ' 
            doc[1] = ' '+doc[1]+' '
            doc[2] = ' '+doc[2]+' '
            # First feature --> % of the words contain in the query that are in the name
            if token in doc[0]:
                n = n+1
            # Second feature --> Yes/No depending if a word of the query is in the attribute component
            if token_aux in doc[1]:
                f_2=1
            # Third feature --> Yes/No depending if a word of the query is in the attribute system
            if token_aux in doc[2]:
                f_3=1
        f_1_aux = n/q_length
        features.append([f_1_aux,f_2,f_3])
        n = 0
        f_2 = 0
        f_3 = 0
        
    return features
    
features_glucose = feature_extractor(q_1)
# # Load relevance
moderate_relevance = pd.read_csv(PREFIX+'dataset_moderate_relevance.csv')
strong_relevance = pd.read_csv(PREFIX+'dataset_strong_relevance.csv').values


features_bilirubin = feature_extractor(q_2)
features_white = feature_extractor(q_3)
head = 'perc_in_name,in_component,in_system,Relevance,long_common_name,query,component,system'
with open('final_features.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["perc_in_name","in_component","in_system"])
    writer.writerows(features_bilirubin)
    writer.writerows(features_glucose)
    writer.writerows(features_white)
csvFile.close()


with open('features_glucose.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["perc_in_name","in_component","in_system"])
    writer.writerows(features_glucose)
csvFile.close()

with open('features_bilirubin.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["perc_in_name","in_component","in_system"])
    writer.writerows(features_bilirubin)
csvFile.close()

with open('features_white.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["perc_in_name","in_component","in_system"])
    writer.writerows(features_white)
csvFile.close()