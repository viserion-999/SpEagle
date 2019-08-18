# Calculating priors: combining all features with different scalling to a
# single number as prior

#input:
#features: Each column contains a feature vector
#featurePoles: 1 means high is suspicious, 0 means low is suspicious

#output:
#prior: prior calculated from F features (user features, product features, review features)

import numpy as np
from scipy import sparse
from Feature_suspiciousness_pole import *



# features is a df.
def prior(features, featurepoles):
    n = features.shape[0]
    # print("number of  rows is:",n)

    numfeatures = features.shape[1]

    #print("number of features are:", numfeatures)
    s = (n, numfeatures)

    comp = np.ones(s) * 0.5
    # print(comp)

    for k in range(0, numfeatures):
        # print("k is",k)
        f = features[features.columns[k]]

        sf = f.sort_values()
        for i in range(0, n):
            if (f[i] == -1): continue  # prior remains unbiased

            ind = sf == f[i]
            # print(ind)
            if (featurepoles[k]):
                # print("inside if")
                NCDF = ind[1] / n

                comp[i, k] = 1 - NCDF  # if high is suspicious
                # print(comp[i,k])
            else:
                NCDF = ind.iloc[-1] / n;
                comp[i, k] = NCDF;  # if low is suspicious
                # print(comp[i,k])

    #print(comp)
    prior = 1 - (np.sum(np.square(comp), axis=1) / numfeatures)
    print(prior)

    prior[prior == 1] = 0.999;
    prior[prior == 0] = 0.001;

    return prior


