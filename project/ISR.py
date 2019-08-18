import numpy as np
#feature 17: ISR

# is it the sole review of the user.
#input:
# userid
#output
# 1 if singleton else 0.

def ISR(userID):
    unique_user, index_user = np.unique(userID, return_inverse=True)
    # output
    isr = np.zeros((len(userID),))

    for i in range(len(userID)):
        index = index_user == i
        # print(np.sum(index))
        if np.sum(index) == 1:
            isr[index] = 1
    return isr

