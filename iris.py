import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
import json

# raw_iris = datasets.load_iris()
# df = pd.DataFrame(raw_iris['data'])
# df_answer = pd.DataFrame(raw_iris['target'])
# dfall = pd.concat([df, df_answer], axis=1)
# print(dfall)
# dfall.to_csv('iris_all.csv')
# print(df)
# print(df_answer)


# # . dataframe 轉 json
def df_to_json(data):
    data.to_json("iris.json")


df_to_json(df)

# import_json 轉 dataframe


def import_json(data):

    data1 = json.load(open(data))
    df = pd.DataFrame(data1)
    print(df)


import_json("iris.json")
