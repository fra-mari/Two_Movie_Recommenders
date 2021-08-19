FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app 

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000
ADD . /app 

CMD ["python", "movie_recommender.py"]