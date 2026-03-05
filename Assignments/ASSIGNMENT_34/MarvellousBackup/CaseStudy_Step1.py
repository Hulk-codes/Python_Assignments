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