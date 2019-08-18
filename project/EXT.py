import numpy as np
#feature 14: EXT

#extremity of the review
# 1 if ratings is {1,5}
# 0 otherwise

def EXT(rating_array):
    extr_ratings = np.zeros((len(rating_array),))

    extr_ratings[np.logical_or(rating_array == 5, rating_array == 1)] = 1
    return extr_ratings