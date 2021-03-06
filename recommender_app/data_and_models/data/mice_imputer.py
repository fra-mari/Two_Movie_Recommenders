"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
This module performs the data preparation on the MovieLens dataset for
the Movie Recommendation engines to work. 

Missing data in the rating table are filled up using 
  MICE (Multivariate Imputation by Chained Equations)
an imputation method featuring a RandomForest Regressor as an estimator.

Moreover, in order to remove noise from the data, movies featuring less
than 10 ratings as well as users with less than 50 rated movies are 
deleted from the dataset.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import os
import logging
import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor

init()

logging.basicConfig(level=logging.INFO, format="%(message)s")

PATH = "preprocessed_for_nmf/"
MICE_FUNCTIONING = (
    Style.BRIGHT
    + """
BASIC FUNCTIONING OF MICE (Multivariate Imputation by Chained Equations):\n"""
    + Style.RESET_ALL
    + """MICE is an imputation algorithm which replaces missing data values in a dataset under the assumption that the data are missing at random in one or more of the variables.

MICE cycles multiple times (e.g. 10) through the following steps:
1. It imputes the missing values in each variable with temporary “place holder” values derived solely from the non-missing values available for that variable (e.g. the mean).
2. It sets back to missing the “place holder” imputations for one variable only. This way, the current data copy contains missing values for a single variable, but not the others.
3. It regresses the missing-values-featuring variable (dependent) on the other previously incomplete ones (independent) via a linear model (in our case, a RF Regressor).
4. It uses the fitted linear model to predict the missing values of the variable.
5. It repeats steps 2–4 separately for each variable that has missing data.

Cycling through Steps 1-5 once for each of the variables constitutes one cycle. At the end of one cycle all of the missing values have been replaced with predictions from regressions that reflect the relationships observed in the data. The process is repeated for the set number of cycles, with the imputations being updated at each cycle.
Ideally, by the end of the cycles, the distribution of the parameters governing the imputations (e.g. the coefficients in the regression models) should have converged towards stability.
"""
)


def visualise_data(users, movies):
    """Provides optional visualisations of the movie ratings
    ---
    ARGUMENTS: 1) A user ratings table as reshaped in line 2 of the noise_reducer() function;
               2) A movie ratings table as reshaped in line 3 of the noise_reducer() function
    """
    question = input('The reasons underlying such a massive cleaning may be better understood by means of visualisation.\nTwo scatterplots are available. Press "Y" to print them on the screen; press "N" to skip.\n')
    while True:
        if question.upper() == "Y":
            plt.figure(figsize=(16, 4))
            plt.scatter(users.index, users, color="green")
            plt.axhline(y=10, color="r")
            plt.xlabel("MovieId")
            plt.ylabel("No. of users who voted")
            plt.show()

            plt.figure(figsize=(16, 4))
            plt.scatter(movies.index, movies, color="green")
            plt.axhline(y=50, color="b")
            plt.xlabel("UserId")
            plt.ylabel("No. of votes by user")
            plt.show()

            logging.info("Resuming the data preparation process...")
            break
        elif question.upper() == "N":
            logging.info("All right. Starting the data preparation process...")
            break
        else:
            question = input(
                Fore.RED
                + 'Please make sure to answer only "Y" or "N" (case insensitve). Try again:\nPress "Y" to print them on the screen; press "N" to skip: '
                + Style.RESET_ALL)
            continue


def noise_reducer(ratings_table):
    """Removes noise from the data:
    To qualify a movie, a minimum of 10 users should have voted a movie;
    To qualify a user, a minimum of 50 movies should have been voted by the user.
    -----
    ARGUMENTS: the loaded ratings.csv file from the MovieLens Dataset
    """

    df = pd.pivot_table(ratings_table, values="rating", index="movieId", columns="userId")

    users_rating = ratings_table.groupby("movieId")["rating"].agg("count")
    movies_rating = ratings_table.groupby("userId")["rating"].agg("count")

    df_m = df.loc[users_rating[users_rating > 10].index, :]

    logging.info(
        Fore.YELLOW
        + "Now starting to clean the noise from the dataset:\n– To qualify a movie, a minimum of 10 users should have voted a movie. Otherwise the record will be deleted;\n– To qualify a user, a minimum of 50 movies should have been voted by the user. Otherwise the record will be deleted.\n"
        + Style.RESET_ALL)
    visualise_data(users_rating, movies_rating)

    df_final = df_m.loc[:, movies_rating[movies_rating > 50].index]
    logging.info(
        Fore.GREEN
        + "\nAll movies featuring less than 10 ratings, as well as all users with less than 50 rated movies have been deleted from the dataset.\nContinuing with the inputation process..."
        + Style.RESET_ALL)

    return df_final


def mice_inputation(df_to_be_filled):
    """
    Fills missing data in the rating table using MICE (Multivariate Imputation by Chained Equations).
    ---
    ARGUMENT: the df output by the noise_reducer() function
    """

    imp = IterativeImputer(estimator=RandomForestRegressor(),
        initial_strategy="mean",
        max_iter=10,
        tol=1e-10,
        random_state=0,)

    logging.info(
        Fore.YELLOW
        + "\nNow starting the inputation process with MICE.\nWARNING: This may take a long time, be patient..."
        + Style.RESET_ALL)

    print(MICE_FUNCTIONING)
    
    df_filled = imp.fit_transform(df_to_be_filled)
    logging.info(
        Fore.GREEN
        + "All right, done! Now converting the data and saving them to a CSV file..."
        + Style.RESET_ALL)

    df_clean = pd.DataFrame(
        data=df_filled[0:, 0:],
        index=[i for i in range(df_filled.shape[0])],
        columns=["U_" + str(i) for i in range(df_filled.shape[1])])

    # replacing the movieId with ordinal index
    df_clean.index = df_to_be_filled.index

    # Transposing the matrix X-Axis-> movieID, Y-Axis-> userId
    df_final = df_clean.T

    return df_final


if __name__ == "__main__":

    logging.info(
        Fore.BLUE
        + "Welcome to the data preparation module for the Statistically Significant Movie Recommender.\n\nThis module will first remove some noise from the MovieLensDataset on the top of which the Recommendation engines have been built,\nthen will use a MICE imputer for filling the residual gaps in the data."
        + Style.RESET_ALL)

    # Loading the dataset
    ratings = pd.read_csv("MovieLensDataset/ratings.csv")
    movies = pd.read_csv("MovieLensDataset/movies.csv")

    # Applying the changes
    df_with_nans = noise_reducer(ratings)

    ready_dataset = mice_inputation(df_with_nans)

    # Writing the ready dataset to a new .csv file

    if not os.path.exists(PATH):
        os.makedirs(PATH)

    ready_dataset.to_csv(f"{PATH}/ready_dataset.csv", index=False)
    logging.info(
        Fore.BLUE
        + f'The file "ready_dataset.csv", containing the preprocessed MovieLens dataset now ready to be used by the Recommandation engines is now in the folder "data_and_models/data/{PATH}.\nThank you for your patience and good bye.'
        + Style.RESET_ALL)
