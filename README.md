# Movie Recommender
* Build a movie recommender website using 'MovieLens' Dataset
* Two recommender models has been used for providing the recommendations
    + 1. Collaborative Filtering With Non-negative Matrix Factorization (NMF)
    + 2. Item-based Collaborative Filtering (find similar movies instead of similar users) using CSR matrix and KNN with 'cosine similarity' as the method
* Contributors: [Francesco Mari](https://github.com/fra-mari) and [Laura Bertolini](https://github.com/Rellino)
### Movie Recommender Website
![movie recommender](recommender.gif)

## Repo Structure

### 1. Webapp
#### 1.1 models
* Stored version of KNN model -> [knn.pickle](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/models/knn.pickle)
* Stored version of NMF model -> [NMF_model.pickle](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/models/NMF_model.pickle) and [NMF_R.pickle](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/models/NMF_R.pickle)

#### 1.2 Static
* Website simple Design -> [styles.css](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/static/css/styles.css9

#### 1.3 templates
* HTML files -> [knn_recommender.html](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/templates/knn_recommender.html), [main_knn.html](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/templates/mian_knn.html), [main.html](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/templates/mian.html), [recommender.html](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/templates/recommender.html)

#### 1.4 Models and Web application
* Website structure -> [app.py](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/app.py)
* Collaborative Filtering model (NMF) > [recommending_engine.py](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/recommending_engine.py)
* Item-based Collaborative Filtering model (KNN) > [knn_recommending_engine.py](https://github.com/behzad1195/Movie-Recommender/blob/master/webapp/knn_recommending_engine.py)

### 2. Data
* Raw data from MovieLens -> [links.csv](https://github.com/behzad1195/Movie-Recommender/blob/master/data/raw/links.csv), [movies.csv](https://github.com/behzad1195/Movie-Recommender/blob/master/data/raw/movies.csv), [ratings.csv](https://github.com/behzad1195/Movie-Recommender/blob/master/data/raw/ratings.csv), [tags.csv](https://github.com/behzad1195/Movie-Recommender/blob/master/data/raw/tags.csv)
* Info about the content of data -> [README.txt](https://github.com/behzad1195/Movie-Recommender/blob/master/data/raw/README.txt)
* Final data after merge and imputation on missing values -> [df_final.csv](https://github.com/behzad1195/Movie-Recommender/blob/master/data/preprocessed/df_final.csv)

### 3. Files 
* MICE model (Multivariate Imputation by Chained Equations) for filling the missing value [MICE_imputer.py](https://github.com/behzad1195/Movie-Recommender/blob/master/MICE_imputer.py)
* Environment specs -> [requirements.txt](https://github.com/behzad1195/Movie-Recommender/blob/master/requirements.txt) 
