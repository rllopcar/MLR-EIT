import os
import csv
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import TweetTokenizer
import numpy as np
import pandas as pd


# DATA LOAD AND CLEANING
PREFIX = "./Data/"
d_aux_1 = []
d_aux_2 = []
data_clean = []

# Load data
data_aux = pd.read_csv(PREFIX+'data.csv')
bilirubin = pd.read_csv(PREFIX+'bilirubin in plasma-Tabla 1.csv', sep=';')
glucose = pd.read_csv(PREFIX+'glucose in blood-Tabla 1.csv', sep=';')
white = pd.read_csv(PREFIX+'White blood cells count-Tabla 1.csv', sep=';')

aux= np.array(bilirubin)
print(aux)
# data = np.append(bilirubin, glucose)
# data = np.append(data,white)


# # Load relevance
# moderate_relevance = pd.read_csv(PREFIX+'dataset_moderate_relevance.csv').values
# strong_relevance = pd.read_csv(PREFIX+'dataset_strong_relevance.csv').values

# print(moderate_relevance[3])


# # Append relevance to create strong and moderate datasets.
# data_moderate = np.append(data,moderate_relevance,axis=0)
# data_relevance = np.append(data,strong_relevance, axis=0)

# print(data_moderate)

# def tokenize(name):
#      return wordpunct_tokenize(name)    

# def data_cleaner(data):
#     for doc in data:
#         d_aux_1 = [str.lower(doc[0]),str.lower(doc[1]), str.lower(doc[2])]
#         d_aux_2.append(d_aux_1)

#     return d_aux_2

# data_clean = data_cleaner(data)

# # FEATURE EXTRACTION
# q_1 = "glucose in blood"
# q_2 = "bilirubin in plasma"
# q_3 = "White blood cells count"

# def feature_extractor(query):
#     features = []
#     # q_token = list(map(str.lower,tokenize(query)))
#     q_token = list(map(str.lower,TweetTokenizer().tokenize(query)))
    
#     q_length = len(q_token)
#     n = 0
#     f_percentage = 0
#     f_1 = []
#     f_2 = 0
#     f_3 = 0
#     for doc in data_clean:
#         aux_doc_0 = list(map(str.lower,tokenize(doc[0])))
#         aux_doc_1 = list(map(str.lower,tokenize(doc[1])))
#         aux_doc_2 = list(map(str.lower,tokenize(doc[2])))
#         print(aux_doc_0)
#         print(aux_doc_1)
#         print(aux_doc_2)
#         for token in q_token:
#             token=' '+token
#             # First feature --> % of the words contain in the query that are in the name
#             if token in doc[0]:
#                 n = n+1
#             # Second feature --> Yes/No depending if a word of the query is in the attribute component
#             if token in doc[1]:
#                 #print(q_token)
#                 f_2=1
#             # Third feature --> Yes/No depending if a word of the query is in the attribute system
#             if token in doc[2]:
#                 f_3=1
#         f_1_aux = n/q_length
#         features.append([f_1_aux,f_2,f_3])
#         n = 0
#         f_2 = 0
#         f_3 = 0
        
#     return features
    
# features_glucose = feature_extractor(q_1)
# features_bilirubin = feature_extractor(q_2)
# features_white = feature_extractor(q_3)


# with open('features_glucose.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(features_glucose)
# csvFile.close()

# with open('features_bilirubin.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(features_bilirubin)
# csvFile.close()

# with open('features_white.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(features_white)
# csvFile.close()