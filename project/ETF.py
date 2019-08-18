import numpy as np
from scipy import sparse


def ETF(userId, prodId, ratings, dates):

    int_dates = np.array([date.toordinal() for date in dates])
    uuser, ind_users = np.unique(userId, return_inverse=True)
    uprod, ind_prods = np.unique(prodId, return_inverse=True)
    udates, ind_dates = np.unique(int_dates, return_inverse=True)
    P, U = len(uprod), len(uuser)
    HRMat = sparse.csr_matrix((np.ones((len(ind_prods))),(ind_prods,ind_users)),shape=(P,U))
    x, y = HRMat.nonzero()
    firstReviewDate = []
    for i in range(P):
        ind = ind_prods==i
        d = int_dates[ind]
        firstReviewDate.append(d.min())
    delta, beta2 = 7*30, 0.69
    F, ETF_reviews = np.zeros((len(ind_prods),)), np.zeros((len(ind_prods),))
    for i in range(len(x)):
        ind = np.logical_and(ind_prods==x[i],ind_users==y[i])
        d = int_dates[ind]
        deltaD = d.max() - firstReviewDate[x[i]]
        if deltaD <= delta:
            F[ind] = 1 - deltaD/delta
    ETF_reviews[F>beta2] = 1
    return ETF_reviews