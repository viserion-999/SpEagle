import sys
import codecs
import datetime as dt
import numpy as np
from scipy import sparse
#feature 2 & 3: PR & NR
#finds the ratio of positive reviews. That is, reviews rated 4 & 5 stars.

# Inputs:
# a)can be users or products
# b)ratings given to the reviews

#Output:
# ratios of positive reviews per user/per product.


def PR_NR(user_prod, ratings, pn):
    # print(type(pn))

    unique_prus, index_prus = np.unique(user_prod, return_inverse=True)

    # we use histograms to group reviews per product or user
    # yet to try with groupby..find an easier way....

    # first make bins for histogram
    bins = np.arange(len(unique_prus) + 1)
    # print("bins are: ",bins)
    hist, bin_edges = np.histogram(index_prus, bins=bins)

    # print(hist.shape)
    # print("bin edges:",bin_edges)

    if (pn == 'PR'):
        # print("inside if")
        # print(index_prus)
        pos_hist, pos_edges = np.histogram(index_prus[ratings > 3], bins=bins)
        # print("positive hist edges",pos_edges.shape)
        # print("positive histogram",pos_hist.shape)

        return pos_hist / hist

    elif (pn == 'NR'):
        # print("inside else")
        neg_hist, neg_edges = np.histogram(index_prus[ratings < 3], bins=bins)
        return neg_hist / hist