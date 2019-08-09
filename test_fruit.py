import numpy as py
import matplotlib as plt
import pandas as pd 

from sklearn.model_selection import train_test_split

fruits = pd.read_table('fruit_data_with_colors.txt')

fruits.head()

fruits.shape 

X = fruits[['mass', 'width', 'height']]
Y = fruits['fruit_label']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state = 0)

