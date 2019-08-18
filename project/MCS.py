import numpy as np
import math as m


def MCS(upId, TFIDF):
    # from numpy import linalg as LA
    import math as m

    """Avg./Max. content similarity.
    Parameters
    ----------
    upId : (R,) array of int
            user/prod Ids.
    TFIDF : (R, nfeatures) scipy.sparse.csr.csr_matrix of float
            TFIDF of each review.
    Returns
    -------
    ACS_up : (U/P,) array of float
            Avg. content similarity.
    MCS_up : (U/P,) array of float
            Max. content similarity.
    """
    uup, ind_up = np.unique(upId, return_inverse=True)
    MCS_up = -np.ones((len(uup),))  # initialise the array

    for i in range((len(uup))):
        ind = ind_up == i  # fetch the indexes from unique user id and populate for the existing dataset
        nreview = np.sum(ind)  # see the number of repeating indexes
        if nreview > 1:
            upT = TFIDF[ind, :]  # TFIDF matrix for the user/product with index i
            npair = nreview * (nreview - 1) / 2  # see the number of review pairs (for the reviews given by same user)
            # npair=m.factorial(nreview)/(2*m.factorial(nreview-2))
            sim_score = np.zeros((int(npair),))  # initialize the similarity score
            # sim_score=[0]*int(npair)

            count = 0  # index store the pairwise similarities in sim_score

            for j in range(int(nreview - 1)):
                for k in range(j + 1, nreview):
                    x, y = upT[j, :].toarray()[0], upT[k, :].toarray()[0]  # store TFIDF of two rewiews
                    xdoty = np.dot(x, y)  # Calculate the dot product of two review matrices
                    if xdoty == 0:
                        sim_score[count] = xdoty
                    else:
                        sim_score[count] = xdoty / (
                                    np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))  # calculate the cosine similarity
                    count += 1
            MCS_up[i] = np.max(
                sim_score)  # Calculate the max similarity score for the user/product among his/it's reviews
    return MCS_up