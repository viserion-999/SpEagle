import numpy as np
from RD import *

def DEV(prodId, ratings):

    RD_reviews = RD(prodId, ratings)
    beta1 = 0.63
    DEV_reviews = np.zeros((len(ratings),))
    normRD = RD_reviews/4
    DEV_reviews[normRD > beta1] = 1
    return DEV_reviews