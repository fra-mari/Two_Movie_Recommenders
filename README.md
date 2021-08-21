# The Statistically Significant Movie Recommender
_A webapp for movie recommendations made via two different models (NMF and KNN)_

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)

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

---
### How To Use This Code
#### On UNIX Systems

If you use MacOs or Linux, clone this repository and `cd` into the folder `recommender_app`. Then follow these simple steps:
1. Install the required Python libraries with `pip install -r requirements.txt`.
2. Generate the trained models by running `python movie_recommender.py`. The process may take a few minutes, but the module also takes care of starting the webapp once the training phase:
   - When you Terminal prints `Now starting the Flask app`, open the address `http://localhost:5000` in your browser for using the webapp, then **follow the instructions on the CLI** to decide whether to enable the automatic retraining of the models based on the ratings provided by the app's users or not.<small><br> <br>**Note**: on some Linux versions, you may need to `apt install lsof` before running the `movie_recommender`module.</small>
3. Once the files containing the model generated, you can always access the webapp running `python movies_app.py`.

**P.S.**: If you prefer to `Docker`, just follow the instructions in the following paragraph.



#### On Windows
You may recur to `WSL`, but the simplest way is probably to use `Docker`. All you have to do is:

- `cd` into the folder `recommender_app`.

- Build the image from the provided Dockerfile by running `docker build . -t movies`.

- Create and start a container by running `docker run -ti -p 5000:5000 --name recommender movies`. You will get access to the container's Bash Command Line.

- Run `python movie_recommender.py`. <u>Refer to point 2 of the previous paragraph</u> for the next steps and options. The webapp will be available at `http://localhost:5000`.

- To quit the container's environment and CLI, you may use the command `exit`.

  


---
### Credits
The code in this repository is an extended and reworked version of the original project developed in collaboration with [Behzad Azarhoushang](https://github.com/behzad1195) and [Laura Bartolini](https://github.com/Rellino).

---
### To Do:
- Improve the CSS of the website
- Show the movie posters of the recommended movies.
