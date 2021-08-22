# The Statistically Significant Movie Recommender
_A webapp for movie recommendations made via two different models (NMF and KNN)_

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)



### The Idea

Build a movie recommender website using 'MovieLens' Dataset

* Two recommender models has been used for providing the recommendations
  + 1. Collaborative Filtering With Non-negative Matrix Factorization (NMF)
  + 2. Item-based Collaborative Filtering (find similar movies instead of similar users) using CSR matrix and KNN with 'cosine similarity' as the method



| ![gif](./StatSigRec.gif) |
| :---: |

#### Data Set
fff

#### Tech Stack
- d
- d
- d

---
### How To Use This Code
#### On UNIX Systems

If you use MacOs or Linux, clone this repository and `cd` into the folder `recommender_app`. Then follow these simple steps:
1. Install the required Python libraries with `pip install -r requirements.txt`.

2. Generate the trained models by running `python movie_recommender.py`. The process may take a few minutes, but the module also takes care of starting the webapp once the training phase:
   - When you Terminal prints `Now starting the Flask app`, open the address `http://localhost:5000` in your browser for using the webapp, then **follow the instructions on the CLI** to decide whether to enable the automatic retraining of the models based on the ratings provided by the app's users or not.
   
   ⚠️⚠️ On some Linux versions, you may need to `apt install lsof` before running the `movie_recommender` module.
   
3. Once the files containing the model generated, you can always access the webapp running `python movies_app.py`.

**P.S.**: If you prefer to `Docker`, just follow the instructions [in the following paragraph](https://github.com/fra-mari/two_movie_recommendation_engines#on-windows).



#### On Windows
You may recur to `WSL`, but the simplest way is probably to use `Docker`. All you have to do is:

- `cd` into the folder `recommender_app`.

- Build the image from the provided Dockerfile by running `docker build . -t movies`.

- Create and start a container by running `docker run -ti -p 5000:5000 --name recommender movies`. You will get access to the container's Bash Command Line.

- Run `python movie_recommender.py`. **Refer to [point 2](https://github.com/fra-mari/two_movie_recommendation_engines/blob/main/README.md#how-to-use-this-code) of the previous paragraph** for the next steps and options. The webapp will be available at `http://localhost:5000`.

- To quit the container's environment and CLI, you may use the command `exit`.

  


---
### Credits
The code in this repository is an extended and reworked version of the original project developed in collaboration with [Behzad Azarhoushang](https://github.com/behzad1195) and [Laura Bartolini](https://github.com/Rellino).

---
### To Do:
- Improve the CSS of the website
- Show the movie posters of the recommended movies.
- Tests
