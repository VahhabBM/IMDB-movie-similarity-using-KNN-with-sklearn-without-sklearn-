# this is the bonous level, which we should calculate all of the algorithms with nltk and sci libraries...
# so we import all of the libraries we need!
import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
import csv
import numpy as np
# opening the csv file of dirty:
with open('dirty_datas.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    dirty_datas = dict(csv_reader)

dirty_datas['movie'] =input('enter your plot summery : ')
# taking input from user and putting it in a dictionary as a value of the 'movie' key
text= []
for i in dirty_datas:
    text.append(dirty_datas[i])
# putting dirty datas from a dictionary to a list.
vectorizer = TfidfVectorizer(max_df=1.0, min_df=1, stop_words='english',norm = None)
#sets the "calculating tf_idf" function.
X = vectorizer.fit_transform(text)
mat = X.todense().tolist()
# using the "calculating tf_idf" function.
m = dict()
for i , j in enumerate(mat):
    v1 = mat[250]
    v2 = j
    m[i]=np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
sorted_dict = dict(sorted(m.items(), key=lambda x: x[1] ,reverse=True))
# this is the 'cosine similarity calculating' part of the project!
for i,j in enumerate(list(sorted_dict)[2:7]):
    for k,h in enumerate(dirty_datas):
        if k == j:print(f'{i+1}. {h} : {sorted_dict[j]}')
# and at the end, we print 5 similar movie to the inputed movie's plot summary by a sorted list which includes the tf_idf value for each movie's words!