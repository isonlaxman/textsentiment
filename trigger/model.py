
#%%
import json
import pandas as pd
import os


from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier

import numpy as np


#%%
ask = pd.read_csv("../data/final_ask.csv", header=None)
ask = ask.iloc[1:].drop_duplicates(subset=[0])
college = pd.read_csv("../data/college_csv.csv", header=None).drop_duplicates(subset=[0])
combined = pd.read_csv("../data/combined_csv.csv", header=None).drop_duplicates(subset=[0])


#%%
print(combined)


#%%
support = pd.read_csv("../data/support_csv.csv", header=None).drop_duplicates(subset=[0])


#%%
df = pd.concat([ask, college, support, combined])


#%%
df = df.sample(frac=1).reset_index(drop=True)


#%%
ask = pd.DataFrame({0 : ['hello hello my name is', 'a'], 1: [0, 1]})


#%%
# print(type(ask.iloc[0,1]))
# twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
# print(twenty_test.data[0])


#%%
count_vect = CountVectorizer(stop_words='english')


#%%
X_train_counts = count_vect.fit_transform(df.iloc[0:400000, 0])
# print(X_train_counts)


#%%
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)


#%%
clf = MultinomialNB().fit(X_train_tfidf, df.iloc[0:400000, 1])


#%%
predicted = clf.predict(count_vect.transform(df.iloc[400001:, 0]))
print(predicted)


#%%
np.mean(predicted == df.iloc[400001:, 1])


#%%


