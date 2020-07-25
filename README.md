# kmeans_bigdata
Bag of words classification using kmeans algorithm with map-reduce method ..

#### dataset used in this work is NYTimes news articles
Dataset can be found at: https://archive.ics.uci.edu/ml/datasets/Bag+of+Words

#### run this command in your terminal after downloading the dataset to working directory:
cat docword.nytimes.txt | python mapper.py | python reducer.py
