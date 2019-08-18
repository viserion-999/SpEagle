# return [userFeatures, prodFeatures, reviewFeatures, adjlist, label]


import sys
import unicodedata
import codecs
import datetime as dt
import numpy as np
from scipy import sparse
import re
import string
import pandas as pd
from nltk import word_tokenize
import csv
from MNR import *
from PR_NR import *
from avgRD import *
from BST import *
from RL import *
from MCS import *
from ACS import *
from ETF import *
from Rank import *
from EXT import *
from DEV import *
from ISR import *
from Feature_suspiciousness_pole import *
from priors import *
from Feature_suspiciousness_pole import *
from sklearn.feature_extraction.text import TfidfVectorizer


#reads the metadatafile
def read_metadata(path , N =2000):
    metadata_file = path

    user_features = "user_features.csv"
    try:
        file = open(user_features, 'r')
    except IOError:
        file = open(user_features, 'w')


    reviewId, userId, prodId, date, ratings, recommend = [], [], [], [], [], []
    reviewId0 = 1

    with codecs.open(metadata_file, 'r', 'utf-8') as fr:
        for line in fr:
            if reviewId0 <= N:
                userId0, prodId0, rating0, recommend0, date0 = line.rstrip().split('\t')
                reviewId.append(reviewId0)
                userId.append(userId0)
                prodId.append(prodId0)
                date.append(date0)
                ratings.append(rating0)
                recommend.append(recommend0)
                reviewId0 += 1

    # we have reviewId, userId, prodId, date, rating, recommend
    # convert date from string to required format
    ratings = np.array(ratings, dtype=np.float32)
    recommend = np.array(recommend, dtype=np.float32)

    dateformat = '%Y-%m-%d'
    date = [dt.datetime.strptime(d, dateformat) for d in date]

    # example metadata
    # 5044	0	1.0	-1	2014-11-16
    # 5045	0	1.0	-1	2014-09-08
    return userId,prodId,date,ratings,recommend

#reads the review content file
def read_review_content(filename, N=2000, sep = '\t'):

        """Read reviews (format: userId prodId date reviewtxt).
        """
        reviewIdr, reviewtxt = [], []
        reviewIdr0 = 1
        with codecs.open(filename, 'r', 'utf-8') as fr:
            for line in fr:
                if reviewIdr0 <= N:
                    reviewtxt0 = ' '.join(line.rstrip().split(sep)[3:])
                    reviewtxt0 = unicodedata.normalize('NFKD', reviewtxt0)
                    reviewIdr.append(reviewIdr0)
                    reviewtxt.append(reviewtxt0)
                    reviewIdr0 += 1
        return reviewtxt


#makes user features and stores in a csv
def make_user_features(userId,prodId,date,ratings,recommend, review_words,review_text):
    user_features = pd.DataFrame()

    unique_user = list(np.unique(userId))
    user_features.insert(0, "userId",unique_user)
    # 1. MNR
    user_features.insert(1,"mnr", MNR(userId,date))
    #2. PR
    user_features.insert(2,"PR", PR_NR(userId,ratings ,"PR"))
    #3. NR
    user_features.insert(3, "NR",PR_NR(userId,ratings,"NR"))

    #4. avgRD
    user_features.insert(4,"avgRD",avgRD(userId,prodId,ratings,us_pr="user"))

    #5. WRD
    #did not do.

    #6. BST
    user_features.insert(5,"BST",BST_user(userId,date))

    #7. ERD
    #did not do.

    #8. ETG
    #did not do.

    #9. RL
    #use review_text
    #remove 0:2000 later...

    user_features.insert(6,"RL",RL(userId, review_words[0:3000]))


    #uses review content to find TFIDF.

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=2000,
                                 stop_words='english')


    # Max Features would mean
    # creating a feature matrix out of the most 2000 frequent words accross text documents.
    TFIDF = vectorizer.fit_transform(review_text)

    #10. ACS
    user_features.insert(7,"ACS",ACS(userId,TFIDF))


    #11. MCS
    user_features.insert(8,"MCS",MCS(userId,TFIDF))

    #write to a csv file and exit the function
    user_features.to_csv('/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/feature_csvs/user_features.csv',
                         index=None, header=True)



#makes product features and stores in a csv
def make_prod_features(userId,prodId,date,ratings,recommend,review_words,review_text):
    unique_prod = list(np.unique(prodId))

    prod_features = pd.DataFrame()


    prod_features.insert(0,"prodId",unique_prod)

    #1. MNR
    prod_features.insert(1,"mnr",MNR(prodId,date))

    #2. PR
    prod_features.insert(2,"PR",PR_NR(prodId,ratings,"PR"))

    #3. NR
    prod_features.insert(2, "NR", PR_NR(prodId, ratings, "NR"))

    #4. avgRD
    prod_features.insert(4,"avgRD",avgRD(userId,prodId,ratings,us_pr="product"))

    #5. WRD
    #did not do

    #6. ERD
    #did not do.

    #7. ETG
    #did not do.

    #8. RL
    #later remove 3000.....
    prod_features.insert(5, "RL", RL(prodId, review_words[0:1000]))

    # uses review content to find TFIDF.

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=1000,
                                 stop_words='english')

    # Max Features would mean
    # creating a feature matrix out of the most 2000 frequent words accross text documents.
    TFIDF = vectorizer.fit_transform(review_text)

    # 9. ACS
    prod_features.insert(6, "ACS", ACS(prodId, TFIDF))

    # 10. MCS
    prod_features.insert(7, "MCS", MCS(prodId, TFIDF))



    # write to a csv file and exit the function
    prod_features.to_csv('/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/feature_csvs/prod_features.csv',
                         index=None, header=True)


#makes the review features and stores in a csv
#yet to add all text features.
def make_review_features(userId,prodId,date,ratings,recommend,review_words,review_text):
    review_features = pd.DataFrame()

    #1. Rank
    review_features.insert(0,"Rank",Rank(prodId,date))

    #2. RD
    review_features.insert(1,"RD",RD(prodId,date))

    #3. EXT
    review_features.insert(2,"EXT",EXT(ratings))


    #4. DEV
    review_features.insert(3,"DEV",DEV(prodId,ratings))

    #5 ETF
    review_features.insert(4,"ETF",ETF(userId,prodId,ratings,date))

    #6. ISR
    review_features.insert(5,"ISR",ISR(userId))




#doubt over here..
#yet to test. Pending since we may not need to do this way...
def make_adj_matrix(userId,prodId,ratings):
    unique_user, index_user = np.unique(userId, return_inverse=True)
    unique_prod, index_prod = np.unique(prodId, return_inverse=True)

    adjlist = [unique_user, unique_prod, ratings]

    print("till here")
    return adjlist




