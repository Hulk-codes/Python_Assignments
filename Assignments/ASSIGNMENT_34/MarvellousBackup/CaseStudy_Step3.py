import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score, 
    confusion_matrix, 
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-" * 40

##############################################################################
# Step 1 : Load the Dataset
##############################################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

Datasetpath = "iris.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets Loaded Successfully")
print("Initial enteries from Dataset : ")
print(df.head())

##############################################################################
# Step 2 : Data Analysis (EDA)
##############################################################################

print(Border)
print("Step 2 : Data Analysis ")
print(Border)

print("Shape of Dataset : ", df.shape)
print("Column Names : ", list(df.columns))

print("Missing Values (Per Column) :")
print(df.isnull().sum())

print("Classs distribution (Species Count) :")
print(df["species"].value_counts())

print("Statistical Report of Dataset :")
print(df.describe())

##############################################################################
# Step 3 : Decide Independent and Dependent Variables
##############################################################################

print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

# X : Independent Variables / Features
# Y : Dependent Variables / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"  
]

X = df[feature_cols]
Y = df["species"]

print("X Shape : ", X.shape)
print("Y Shape: ", Y.shape)