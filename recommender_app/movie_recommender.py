"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
This module controls the workflow of the movie recommender. 
It trains the NFM model based on the (updating) data and saves
it in order for the recommendation engine to import it;
Moreover, it runs the webapp and keeps it on unless the user decides
otherwise.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import logging
import sys
from colorama import Fore, Style, init
import os
import pandas as pd
import pickle
from time import sleep
from sklearn.decomposition import NMF

logging.basicConfig(format="%(asctime)s: %(message)s")

init()


def create_update_model(df):
    """
    trains the model based on the latest input
    ARGUMENT: The pandas dataframe containing the recommandations
    """

    # Changing dataframe to numpy ndarray for building R matrix
    R = pd.DataFrame(df, index=df.index, columns=df.columns).values

    # create a model and set the hyperparameters
    model = NMF(n_components=126, init="random", random_state=1, max_iter=100000, solver="cd")

    # fitting the model to R
    fit_model = model.fit(R)

    return fit_model, R


if __name__ == "__main__":

    try:
        PATH = "data_and_models/models/"
        if not os.path.exists(PATH):
            os.makedirs(PATH)

        print(Fore.BLUE
            + "Welcome to the Statistically Significant Movie Recommender!\n\nThis module will train a Non-Negative Matrix Factorization Model (NFM) on the MovieLensDataset and launch the webapp for interacting with it.\n"
            + Style.RESET_ALL)
        print(Fore.WHITE
            + Style.BRIGHT
            + "STEP 1: "
            + Style.NORMAL
            + "Traing the NMF model on the MovieLens dataset. The webapp will be launched as soon as the training is completed.\nThis will take a little time, though..."
            + Style.RESET_ALL)

        df_final = pd.read_csv("data_and_models/data/preprocessed/ready_dataset.csv")
        logging.warning("The file ready_dataset.csv has been loaded. Starting the creation of the NMF model...")
        nmf, R_nmf = create_update_model(df_final)
        logging.warning(Fore.GREEN + "Model correctly updated!" + Style.RESET_ALL)

        # saving the model
        with open("data_and_models/models/NMF_model.pickle", "wb") as f:
            pickle.dump(nmf, f)
        logging.warning('NMF trained model saved in the folder "data_and_models/models/".')
        with open("data_and_models/models/NMF_R.pickle", "wb") as f2:
            pickle.dump(R_nmf, f2)
        logging.warning('R matrix for the NMF model saved in the folder "data_and_models/models/".')

        print(Fore.WHITE
            + Style.BRIGHT
            + "STEP 2: "
            + Style.NORMAL
            + "Now starting the Flask app run by the module `movies_app.py` IN THE BACKGROUND. In a few seconds, the website will be accessible at"
            + Fore.YELLOW
            + Style.BRIGHT
            + " http://localhost:5000 "
            + Fore.WHITE
            + Style.NORMAL
            + "in your browser.\n"
            + "The Log for the app may be found in the file"
            + Fore.YELLOW
            + Style.BRIGHT
            + " RecommenderLog.log"
            + Fore.WHITE
            + Style.NORMAL
            + "."
            + Style.RESET_ALL)
        
        os.system("/bin/bash run_app.sh")
        sleep(10)

        print(Fore.WHITE
            + "\nIf you wish, this module can now remain up to update the NMF Recommendation model every 12 hours."
            + Style.RESET_ALL)
        keep_going = input(Fore.YELLOW
            + 'Do you wish to keep the script up for cyclically updating the NMF model? Press any key to continue OR press "Q" to quit: '
            + Style.RESET_ALL).upper()
        if keep_going == "Q":
            kill = input(Fore.BLUE
                + 'Do you wish to kill both the NMF updater and the webapp? Press "Y" for killing both modules, or any other key for only killing the NMF updater: '
                + Style.RESET_ALL).upper()
            if kill == "Y":
                os.system("/bin/bash kill_app.sh")
                print("All right, the NMF updater and the webapp have been killed. Bye bye!")
                sys.exit()
            else:
                print("Quitting this module and stopping the live update of the NMF.\n"
                    + Fore.RED
                    + "The webapp is still up and running! To shut it down, you should use the command: "
                    + Fore.WHITE
                    + "kill -9 `lsof -i:5000 -t`"
                    + Fore.RED
                    + " in your Terminal.\n"
                    + Style.RESET_ALL)
                
                sys.exit()
                

        else:
            print(Fore.WHITE
                + "All right then. Keeping the NMF updater up. You can exit from it anytime with CTRL+C.\n"
                + Style.RESET_ALL)

            while True:

                sleep(60 * 60 * 12)

                logging.warning(
                    "Running the cyclical update of the NMF model based on the most recent recommandation provided by the website users..."
                )

                df_final = pd.read_csv("data_and_models/data/preprocessed/ready_dataset.csv")
                logging.warning("The file ready_dataset.csv has been loaded. Starting the update of the NMF model...")
                nmf, R_nmf = create_update_model(df_final)
                logging.warning("Model correctly updated!")

                with open("data_and_models/models/NMF_model.pickle", "wb") as f:
                    pickle.dump(nmf, f)
                logging.warning('New version of the NMF trained model saved in the folder "data_and_models/models/".')
                with open("data_and_models/models/NMF_R.pickle", "wb") as f2:
                    pickle.dump(R_nmf, f2)
                logging.warning('New version of the R matrix for the NMF model saved in the folder "data_and_models/models/".')

    except KeyboardInterrupt:
        print(" Quitting...\n"
            + Fore.RED
            + "N.B.: To quit this module will not stop the webapp if it is running! To shut it down, you should use the command: "
            + Fore.WHITE
            + "kill -9 `lsof -i:5000 -t`"
            + Fore.RED
            + " in your Terminal.\n"
            + Style.RESET_ALL)

