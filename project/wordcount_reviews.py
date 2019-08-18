import sys
import codecs
import datetime as dt
import numpy as np
from scipy import sparse
import re
import string
from nltk import word_tokenize

#review_words matrix.
#number of words in each review written.

def WordCount_reviews(reviewFile, outFile):

    with codecs.open(reviewFile, 'r', 'utf-8') as f:
        data1 = f.readlines()
    f.close()

    output = codecs.open(outFile, 'a', 'utf-8')
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    for line in data1:
        count = re.split("\s+", line, 1)[0]
        if len(re.split("\s+", line, 1)) > 1:
            line = re.split("\s+", line, 1)[1]
            words = word_tokenize(line)
            word = []
            temp = ""
            c = 0
            for w in words:
                c = c + 1
                if w in string.punctuation:
                    temp = temp+w
                    if c < len(words):
                        continue
                if len(temp) > 1:
                    word.append(temp)
                temp = ""
                new_token = regex.sub(u'', w)
                if not new_token == u'':
                    word.append(new_token)
            #print(count+' '+str(len(word))+'\n')
            output.write(count+' '+str(len(word))+'\n')
    output.close()

review_file = "/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/data/raw/reviewContent"

review_words = "review_words"
try:
    file = open(review_words, 'r')
except IOError:
    file = open(review_words, 'w')

WordCount_reviews(review_file, review_words)