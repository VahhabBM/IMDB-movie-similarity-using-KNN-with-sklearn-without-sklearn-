# First of all , we import all needed libraries!
import csv
# csv library is for handling the datas from the csv file which we earned them from imdb web scraping.
import numpy as np
# actually we use numpy arrays for our project! so we need it.
import string
# with the string library, we can access all of punctuations to remove them from summaries. 
from nltk.corpus import stopwords
# also we just need all of stopwords to remove them from summaries, so we can access all of them with nltk library!
import nltk
import math
# we need the math library because of calculating cosine between two vectors.
from nltk.stem.snowball import SnowballStemmer
# this library is used for finding the base form of a word. for example, it turns 'creating' to 'create'!
nltk.download('stopwords')
# downloads the stopwords
with open('dirty_datas.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    dirty_datas = dict(csv_reader)
# At the beggining of our project, we open csv file of dirty datas and read it and then we put them all to a dictionary.
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
# this function removes thhe punctuation.
def remove_stop_words(text):
    stemmer = SnowballStemmer("english")
    inli = list(text.split(' '))
    # we put all of the words to a list by using 'split()'
    out = []
    for i in inli:
        if i.lower() not in set(stopwords.words('english')) and stemmer.stem(i.lower()) not in out:
            out.append(stemmer.stem(i.lower()))
    return out
    # we remove the stop words and finally we append the base forms of the words to the out list and return it. 
def TF(term , duc):
    return duc.count(term)/len(duc)
def IDF(term , in_dict):
    x=0
    for i in in_dict:
        if term in in_dict[i]:
            x+=1
    return math.log10((250/x))+1
# according to the TF & IDF formula , we calculate both of them
def table_creation(in_dict , terms):
    out=[]
    for i in terms:
        Idf = IDF(i , in_dict)
        # We make the list of tf_idf for every word.
        tf_idf=[]
        for j in in_dict:
            tf_idf.append(TF(i , in_dict[j])*Idf)
        out.append(tf_idf)
        # here, we separate tf_idf of words by the movie names. it means each word , has a tf_idf value considering to a movie name.
    return np.transpose(np.array(out))
    # next , we put our list to a numpy array
def movie_similarity(a):
    dictionary = dict()
    for i,j in enumerate(a):
        v1=a[-1]
        v2=j
        cosine_similarity = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        dictionary[list(clean_datas)[i]] = cosine_similarity
        sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    for i,j in enumerate(list(sorted_dict.keys())[2:7]):
        print(f'{i+1}. {j} : {sorted_dict[j]}')
# and the last function is the 'cosine similarity calculating' function. it calculates the cosine of two movie(vector) by the dot of two arrays and deviding the result to the norm of the two vectors. If the cosine is near the 1, the movis have almost the same subject! and if it is near to 0 it means the movies aren't same!
clean_datas = dict()
for i in dirty_datas:
    clean_datas[i] = remove_stop_words(remove_punctuation(dirty_datas[i]))
    # callig remove stopwords fuction by each movie.
words_list = sorted(list(set([ i for summary in clean_datas.values() for i in summary])))
# this is the list of all of the words
clean_datas['movie'] = remove_stop_words(remove_punctuation(input('enter your plot summery : ')))
# taking input and calling the punctuation and stopword's function.
movie_similarity(table_creation(clean_datas , words_list))
# calling the movie_similarity function with the table of 'clean_datas' and the 'words_list'



