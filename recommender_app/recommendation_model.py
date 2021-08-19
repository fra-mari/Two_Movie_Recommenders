"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
This module trains the NFM model based on the (updating) data and saves
it in order for the recommendation engine to import it.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#import datetime as dt
import logging
import os
import pandas as pd
import pickle
from time import sleep
from sklearn.decomposition import NMF

logging.basicConfig(#filename='RecommenderLog.log',
                    format='%(asctime)s:%(levelname)s: %(message)s')


def update_model(df):
    """
    trains the model based on the latest input
    ARGUMENT: The pandas dataframe containing the recommandations
    """

    # Changing dataframe to numpy ndarray for building R matrix 
    R = pd.DataFrame(df, index=df.index, columns=df.columns).values

    #create a model and set the hyperparameters
    # 20 Genres (from EDA.py) + 106 years -> 126 number of components
    model = NMF(n_components=126, init='random', random_state=1, max_iter=100000, solver='cd')

    # fitting the model to R
    fit_model = model.fit(R)

    return fit_model, R 

if __name__ == '__main__':

    PATH = "data_and_models/models/"
    if not os.path.exists(PATH):
        os.makedirs(PATH)

    while True:

        # Loading the up to date preprocessed rating file
        # X-Axis -> userId , Y-Axis -> movieId
        df_final = pd.read_csv('data_and_models/data/preprocessed/ready_dataset.csv')
        nmf, R_nmf = update_model(df_final)

        # saving the model
        with open('data_and_models/models/NMF_model.pickle','wb') as f:
            pickle.dump(nmf, f)
        logging.warning('New version of the NMF trained model saved in the folder "data_and_models/models/".')
        with open('data_and_models/models/NMF_R.pickle','wb') as f2:
            pickle.dump(R_nmf, f2)
        logging.warning('New version of the R matrix for the NMF model saved in the folder "data_and_models/models/".')

        sleep(60*60*12)

