import sys
import codecs
import datetime as dt
import numpy as np
from scipy import sparse

# feature 1 MNR

#MNR: Maximum number of reviews written in a day.

#Inputs: a)can be users or products
#        b) the dates on which reviews are written for products or by users

#Outputs:
#        a) max of number of reviews of a product or a user.

def MNR(user_prod, dates):

    #first convert dates to numerical format
    dates2 = [date.toordinal() for date in dates]

    #find unique dates & then unique users...

    unique_dates, index_dates = np.unique(dates2, return_inverse=True)
    unique_prus, index_prus = np.unique(user_prod, return_inverse=True)


    len_d = len(unique_dates)
    len_up = len(unique_prus)
    #print(len(np.ones((len(unique_dates)))))
    #print("unique dates are",len_d)
    #print("unique products are",len_up)
    mnr = sparse.csr_matrix((np.ones((len(index_dates))),(index_dates,index_prus)),shape=(len_d,len_up)).toarray()
    #print(mnr)
    #Normalized MNR
    return mnr.max(axis=0)/mnr.max()
