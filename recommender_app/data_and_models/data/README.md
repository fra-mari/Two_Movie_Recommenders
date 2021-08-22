## Content of This Folder
This folder contains both **[the MovieLens 100k Dataset](./MovieLensDataset/)** and a subfolder `preprocessed` with the `ready_dataset.csv` file on which the recommender systems have been trained and from which the webapp draws information on the movies. This file results from the cleaning of the raw data, which also implied the choice of a strategy to provide values for ratings that were missing in the original dataset. This task is handled by the module `mice_imputer.py`. You may found a description of the MICE imputer [in the next paragraph](https://github.com/fra-mari/two_movie_recommendation_engines/blob/main/recommender_app/data_and_models/data/README.md#basic-functioning-of-mice).<br><br> 
🔴 Whenever run, the `mice_imputer` module shows some plots of the MovieLens raw data and then starts the MICE imputer, eventually producing a new `ready_dataset.csv` file in the `preprocessed` folder. **Depending on your CPU, the whole process may take hours!** Run at your own risk. 

### Basic Functioning of MICE 
MICE (Multivariate Imputation by Chained Equations) is an **imputation algorithm** which replaces missing data values in a dataset under the assumption that the data are missing at random in one or more of the variables.<br><br>
MICE cycles multiple times (e.g. 10) through the following steps:
1. It imputes the missing values in each variable with temporary “place holder” values derived solely from the non-missing values available for that variable (e.g. the mean).
2. It sets back to missing the “place holder” imputations for one variable only. This way, the current data copy contains missing values for a single variable, but not the others.
3. It regresses the missing-values-featuring variable (dependent) on the other previously incomplete ones (independent) via a linear model (in our case, a RF Regressor).
4. It uses the fitted linear model to predict the missing values of the variable.
5. It repeats steps 2–4 separately for each variable that has missing data.

Cycling through Steps 1-5 once for each of the variables constitutes one cycle. At the end of one cycle all of the missing values have been replaced with predictions from regressions that reflect the relationships observed in the data. The process is repeated for the set number of cycles, with the imputations being updated at each cycle.
Ideally, by the end of the cycles, the distribution of the parameters governing the imputations (e.g. the coefficients in the regression models) should have converged towards stability.<br><br>
*Refer [here](https://stats.stackexchange.com/questions/421545/multiple-imputation-by-chained-equations-mice-explained) for more details and references.*
