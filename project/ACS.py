
import numpy as np
from numpy import linalg as LA

def ACS(upId, TFIDF):
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
    ACS_up = -np.ones((len(uup),))  # initialise the array

    for i in range((len(uup))):
        ind = ind_up == i  # fetch the indexes from unique user id and populate for the existing dataset
        nreview = np.sum(ind)  # see the number of repeating indexes
        if nreview > 1:
            upT = TFIDF[ind, :]  # TFIDF matrix for the user/product with index i
            npair = int(
                nreview * (nreview - 1) / 2)  # see the number of review pairs (for the reviews given by same user)
            sim_score = np.zeros((npair,))  # initialize the similarity score

            count = 0  # index store the pairwise similarities in sim_score

            for j in range(int(nreview - 1)):
                for k in range(j + 1, nreview):
                    x, y = upT[j, :].toarray()[0], upT[k, :].toarray()[0]  # store TFIDF of two rewiews
                    xdoty = np.dot(x, y)  # Calculate the dot product of two review matrices
                    if xdoty == 0:
                        sim_score[count] = xdoty
                    else:
                        sim_score[count] = xdoty / (LA.norm(x) * LA.norm(y))  # calculate the cosine similarity
                    count += 1
            ACS_up[i] = np.mean(sim_score)
    return ACS_up