import numpy as np

#feature 13

#RD: Absolute rating deviation from product's avg. this we get for all products

#Inputs: 1) product id
#          2)rating given fro each product

#output:
#       absolute rating dev for each product.

def RD(prodID,ratings):

    unique_prod, index_prod = np.unique(prodID, return_inverse=True)
    #first create a avg rating matrix of zeroes[1,2,3,4,....len(ratings)]

    avg = np.zeros((len(ratings),))

    #for each of the unique products
    #take their indicies, get their ratings and avg in each iteration whenever found..
    for k in range(len(unique_prod)):
        index = index_prod ==k
        if any(index):
            rating = ratings[index]
            #average them here...
            avg[index_prod == k] = np.sum(rating)/len(rating)

    return np.abs(ratings - avg)
