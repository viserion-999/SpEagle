import numpy as np
#feature 6: BST

# Burstiness
#intution: Spammers are often short term members of the site.
#in this function we trace such users.
# Input:
#      dates
#        user id

# Output:
#    0 if (date(last_review) - date(first_review) > threshold)
#    1-(date(last_review) - date(first_review)/threshold), otherwise

#here we consider threshold as 28 days.

def BST_user(userID, dates):
    # convert dates to ordinal.
    dates1 = np.array([date.toordinal() for date in dates])

    # getting unique users like we always did.
    unique_user, index_user = np.unique(userID, return_inverse=True)

    # threshold
    threshold = 28

    # output
    BST_values = np.ones((len(unique_user),))

    for k in range(len(unique_user)):
        index = index_user == k

        if (np.sum(index) > 1):
            # print("index is",index)
            temp = dates1[index]
            # print("dates are:",temp)
            # print("max day is",temp.max())
            # print("min day is",temp.min())
            np_days = temp.max() - temp.min()
            if np_days > threshold:
                # print("inside if")
                BST_values[k] = 0
                # print("should print 0 here",BST_values[k])
            else:
                # print("np_days",np_days)

                # print("inside else..calculating..",np_days/threshold)
                BST_values[k] = 1 - np_days / threshold
                # print("calculated value is:",BST_values[k])
    return BST_values