from Feature_Extraction import *
from Feature_suspiciousness_pole import *
from priors import *
from homophily_matrix import *
from SpEagle import *
import time





def main():


    metadata = "/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/data/raw/metadata"
    review_content = "/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/data/raw/reviewContent"


    #read the metadata file:
    userId, prodId, date, ratings, recommend = read_metadata(path = metadata,N = 1000)

    #read the reviewcontent file
    review_text = read_review_content(review_content,N = 1000, sep='\t')


    #review_words number of words in each review. Seperately calculated and saved.
    #to create this, run wordcount_reviews file..
    review_words = np.loadtxt("/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/data/raw/review_words")

    start = time.time()

    #comment after features are built.

    #read user features
    # make_user_features(userId,prodId,date,ratings,recommend,review_words,review_text)
    # end = time.time()
    # print("time taken to build user features:",end-start)

    #read product features
    start = time.time()

    # #read user features
    # make_prod_features(userId,prodId,date,ratings,recommend,review_words,review_text)
    # end = time.time()
    # print("time taken to build user features:",end-start)

    # read review features.
    #sandy is yet to give..


    #read adjacency list.
    adjlist = np.loadtxt("/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/data/raw/reviewGraph")


    #reading our features.[this wont work for 6lakh rows?]
    user_features = pd.read_csv("/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/feature_csvs/user_features_1.csv")
    prod_features = pd.read_csv("/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/feature_csvs/prod_features.csv")
    #review_priors = pd.read_csv("")


    #Calculating priors.


    #calculate priors for users.
    user_priors = pd.DataFrame()
    uprior = prior(user_features[user_features.columns[1:]],isHighUser)
    user_priors.insert(0,"1-prior",1-uprior)
    user_priors.insert(1,"prior",uprior)
    user_priors.to_csv("/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/prior_csvs/user_priors.csv",index=None,header=True)


    #calculate prior for products
    prod_priors = pd.DataFrame()
    pprior = prior(prod_features[prod_features.columns[1:]],isHighProd)
    prod_priors.insert(0,"1-prior",1-pprior)
    prod_priors.insert(1,"prior",pprior)
    prod_priors.to_csv("/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/prior_csvs/prod_priors.csv",index=None,header=True)


    #calculate priors for reviews -
    review_priors = pd.DataFrame()
    #rprior = prior(review_features[review_features.columns[1:]],isHighReview)
    #review_priors.insert(0,"1-prior",1-rprior)
    #review_priors.insert(1,"prior",rprior)
    #review_priors.to_csv("/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/prior_csvs/review_priors.csv",index=None,header=True)


    #read these before calling..speagle : upriors.csv,ppriors.csv,rpriors.csv
    #upriors = pd.read_csv("/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/prior_csvs/user_priors.csv")
    #ppriors = pd.read_csv("/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/prior_csvs/prod_priors.csv")
    #rpriors =pd.read_csv("/Users/anaghakaranam/Desktop/Opinion_Spam/coding-playground/prior_csvs/review_priors.csv")
    #Calling the SP Eagle function.

    #beliefsUser, beliefsProd, beliefsReview = SpEagle(adjlist, upriors, ppriors, rpriors, edgep, 100)



if __name__ == "__main__":
    main()