# calculate prior for users
# for some features higher is more anomalous and for others lower
# MNR - H , PR - H, NR - H, avgRD - H, WRD - H, BST - H, ERD - L, ETG - L, RL - L, ACS - H, MCS - H

isHighUser = [1 ,1, 1, 1, 1, 1, 0, 0, 0, 1, 1] #according to suspiciousness pole (high vs low) of user
#priorU = priors(userFeatures, isHighUser)

# calculate prior for products
#for some features higher is more anomalous and for others lower
# MNR - H , PR - H, NR - H, avgRD - H, WRD - H, ERD - L, ETG - L, RL - L, ACS - H, MCS - H

isHighProd = [1, 1, 1, 1, 1, 0, 0, 0, 1, 1] #according to suspiciousness pole (high vs low) of product features
#priorP = priors(prodFeatures,isHighProd);

# calculate prior for reviews
# for some features higher is more anomalous and for others lower
# Rank - L, RD - H, EXT - H, DEV - H, ETF - H, ISR - H, PCW - H, PC - H,
# L - L, PP1 - L, RES - H, SW - H, OW - L, F - H, DL_u - L, DL_b - L

isHighReview = [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1 ,0, 1, 0, 0] #according to suspiciousness pole (high vs low) of reviews features
#priorR = priors(reviewFeatures, isHighReview);