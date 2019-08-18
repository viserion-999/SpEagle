import numpy as np

#feature 9: RL
## Average Review length in number of words
## Inputs:
#       a)can be users or products
#       b)wordcount for each review....comes from a file called review_words
        #YET TO WRITE REVIEW_WORDS.

## Outputs:
#       a)avg review length for each product or user..

#reading review_words file before running this..

def RL(user_prod, review_words):

    unique_prus, index_prus = np.unique(user_prod, return_inverse=True)

    avg = np.zeros((len(unique_prus),))
    #print("length to fill",len(avg))

    for k in range((len(unique_prus))):
        index = index_prus==k
        if any(index):
            #yet to write wordcount array..........
            m = review_words[index,1]
            avg[k] = np.sum(m)/len(m)
    return avg
