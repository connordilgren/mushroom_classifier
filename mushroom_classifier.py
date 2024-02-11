import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# read in data
df = pd.read_csv("mushrooms.csv")
# df.head()

# convert letters to numbers
df.replace({'class': {
                'e': 0,
                'p': 1},
            'cap-shape': {
                'b': 0,
                'c': 1,
                'x': 2,
                'f': 3,
                'k': 4,
                's': 5},
            'cap-surface': {
                'f': 0,
                'g': 1,
                'y': 2,
                's': 3},
            'cap-color': {
                'n': 0,
                'b': 1,
                'c': 2,
                'g': 3,
                'r': 4,
                'p': 5,
                'u': 6,
                'e': 7,
                'w': 8,
                'y': 9},
            'bruises': {
                't': 0,
                'f': 1},
            'odor': {
                'a': 0,
                'l': 1,
                'c': 2,
                'y': 3,
                'f': 4,
                'm': 5,
                'n': 6,
                'p': 7,
                's': 8},
            'gill-attachment': {
                'a': 0,
                'd': 1,
                'f': 2,
                'n': 3},
            'gill-spacing': {
                'c': 0,
                'w': 1,
                'd': 2},
            'gill-size': {
                'b': 0,
                'n': 1},
            'gill-color': {
                'k': 0,
                'n': 1,
                'b': 2,
                'h': 3,
                'g': 4,
                'r': 5,
                'o': 6,
                'p': 7,
                'u': 8,
                'e': 9,
                'w': 10,
                'y': 11},
            'stalk-shape': {
                'e': 0,
                't': 1},
            'stalk-root': {
                'b': 0,
                'c': 1,
                'u': 2,
                'e': 3,
                'z': 4,
                'r': 5,
                '?': 6},
            'stalk-surface-above-ring': {
                'f': 0,
                'y': 1,
                'k': 2,
                's': 3},
            'stalk-surface-below-ring': {
                'f': 0,
                'y': 1,
                'k': 2,
                's': 3},
            'stalk-color-above-ring': {
                'n': 0,
                'b': 1,
                'c': 2,
                'g': 3,
                'o': 4,
                'p': 5,
                'e': 6,
                'w': 7,
                'y': 8},
            'stalk-color-below-ring': {
                'n': 0,
                'b': 1,
                'c': 2,
                'g': 3,
                'o': 4,
                'p': 5,
                'e': 6,
                'w': 7,
                'y': 8},
            'veil-type': {
                'p': 0,
                'u': 1},
            'veil-color': {
                'n': 0,
                'o': 1,
                'w': 2,
                'y': 3},
            'ring-number': {
                'n': 0,
                'o': 1,
                't': 2},
            'ring-type': {
                'c': 0,
                'e': 1,
                'f': 2,
                'l': 3,
                'n': 4,
                'p': 5,
                's': 6,
                'z': 7},
            'spore-print-color': {
                'k': 0,
                'n': 1,
                'b': 2,
                'h': 3,
                'r': 4,
                'o': 5,
                'u': 6,
                'w': 7,
                'y': 8},
            'population': {
                'a': 0,
                'c': 1,
                'n': 2,
                's': 3,
                'v': 4,
                'y': 5},
            'habitat': {
                'g': 0,
                'l': 1,
                'm': 2,
                'p': 3,
                'u': 4,
                'w': 5,
                'd': 6}
            },
           inplace=True)

# df.head()

# initialize training, test sets
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:],
                                                    df['class'],
                                                    test_size=0.10,
                                                    random_state=28)

# initialize model
model = LogisticRegression()

# train model
model.fit(X_train, y_train)

# test model
model.score(X_test, y_test)  # r2 score

# get user data


# predict with model
model.predict([[1] * 22])

# return user data