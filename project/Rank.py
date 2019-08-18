import numpy as np
def Rank(prodId, dates):

    int_dates = dates
    udates, ind_dates = np.unique(int_dates, return_inverse=True)
    uprod, ind_prod = np.unique(prodId, return_inverse=True)
    rank = np.zeros((len(prodId),))
    for i in range(len(uprod)):
        ind = ind_prod==i        # ind is an array and it will give true for the value of i present in ind_prod
        if any(ind):             # this will check if true is present in the array ind
            d = ind_dates[ind]   # d will get thevalues of all the ind_dates according to the truth value present in ind
            if len(d)>1:
                ud = np.unique(d)
                f, edges = np.histogram(d, bins=np.append(ud,ud.max()+1)) #getting the frequency count of the dates for the product
                m, r = 0, np.zeros((len(d),))
                for j in range(len(ud)):
                    r[d==ud[j]] = m + 1 #calculating the rank of the product based on the number of reviews/dates
                    m += f[j]  #changing the productid
                rank[ind] = r
            else:             #product with lower reviews will have lower  rank
                r = 1
                rank[ind] = r  #produc with one or no reviews will have rank 1

    return rank
