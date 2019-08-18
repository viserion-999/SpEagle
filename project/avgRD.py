import numpy as np
from RD import *
#feature 4:avgRD

#avg RD - finds the average rating deviation of ratings of users/products

#Input:
#       a) userid
#       b) product id
#       b) ratings given by user id to the product id
#       d) userid or product ?

#Output:
#      a)avg rating deviation of ratings.

def avgRD(userID, prodID, ratings,us_pr):
    unique_user, index_user = np.unique(userID, return_inverse=True)
    unique_prod, index_prod = np.unique(prodID, return_inverse=True)

    # YET TO DO RATING DEVIATION RD (RATING DEVIATION FROM PRODUCT'S AVG RATING.
    # REMEMBER! RD IS CALCULATED FOR EACH PRODUCT
    # AVG RD IS CALCULATED ON THE WHOLE FOR ALL PRODUCTS.....

    RD_ = RD(prodID, ratings)

    avgRDprod = np.zeros((len(unique_prod),))
    avgRDuser = np.zeros((len(unique_user),))

    # avg RD for products

    for i in range(len((unique_user))):
        ind = index_user == i
        if any(ind):
            r = RD_[ind]
            avgRDuser[i] = np.sum(r) / len(r)
    # avg RD for users.
    for i in range(len((unique_prod))):
        ind = index_prod == i
        if any(ind):
            r = RD_[ind]
            avgRDprod[i] = np.sum(r) / len(r)
    if(us_pr == "user"):
        return avgRDuser
    elif(us_pr == "product"):
        return avgRDprod
    #return avgRDuser, avgRDprod
