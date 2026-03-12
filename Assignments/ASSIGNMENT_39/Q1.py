import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, 
    confusion_matrix, 
    classification_report,
    ConfusionMatrixDisplay
)



def LoadingDataset(DataPath):
    Border = "-" * 40
    print(Border)
    print("Loading the datset")
    print(Border)

    df = pd.read_csv(DataPath)

    print("First five record : ")
    print(df.head())
    print(Border)

    print("Last five records : ")
    print(df.tail())
    print(Border)

    print("Total number of rows and columns : ")
    print(df.shape)
    print(Border)

    print("List of column names : ", list(df.columns))
    print(type(df.columns))
    print(Border)

    print(Border)
    print("Student Statistics")
    print(Border)

    # Total number of students
    total_students = len(df)
    print("Total number of students :", total_students)

    # Count Passed students
    passed_students = df[df["FinalResult"] == 1].shape[0]
    print("Number of students Passed :", passed_students)

    # Count Failed students
    failed_students = df[df["FinalResult"] == 0].shape[0]
    print("Number of students Failed :", failed_students)

    print(Border)
    print("Pandas Calculations")
    print(Border)

    # Average Study Hours:
    avg_studyhours = df["StudyHours"].mean()  
    print("Average Study Hours : ", avg_studyhours) 

    # Average Attendace:
    avg_attendace = df["Attendance"].mean()
    print("Average Attendance : ", avg_attendace)

    # Maximum PreviousScore :
    maximum_prevscore = df["PreviousScore"].max()
    print("Maximum PreviousScore : ", maximum_prevscore)

    # Minimum Sleephours : 
    minimum_sleep = df["SleepHours"].min()
    print("Minimum Sleep Hours : ", minimum_sleep)

    print(Border)
    print("Higher Study Hours increases the chance of passing")
    print("Higher attendance aslo increases the chance of passing")
    print(Border)

    # Plotting of Histogram 
    df["StudyHours"].hist()

    plt.title("Histogram of Study Hours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    plt.show()



    # Plotting of scatter plot
    plt.scatter(df["StudyHours"] , df["PreviousScore"])
    plt.title("StudyHours v/s PreviousScore")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.show()


    # Plotting BoxPlot for Attendance
    plt.boxplot(df["Attendance"])
    plt.title("Boxplot for Attendance")
    plt.ylabel("Attendance")
    plt.show()
    
    # Plot for Relationship between Assignments Completed And FinalResults
    plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])

    plt.title("Assignments Completed vs Final Result")
    plt.xlabel("Assignments Completed")
    plt.ylabel("Final Result")
    plt.show()

    # Plot for Sleep Hours against FinalResult
    plt.scatter(df["SleepHours"], df["FinalResult"])

    plt.title("Sleep Hours vs Final Result")
    plt.xlabel("Sleep Hours")
    plt.ylabel("Final Result")

    plt.show()

    
    X = df[['StudyHours','Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']]
    Y = df['FinalResult']


    

    X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)

    model = DecisionTreeClassifier( criterion="gini",max_depth=None,random_state=42)
    model.fit(X_train,Y_train)

    print("Testing the model")
    Y_pred = model.predict(X_test)
    print(Border)
   
    print("Comapring Actual Values to Predicted Values")

    result = pd.DataFrame({
        'Actual Values' : Y_test , 
        'Predicted Values' : Y_pred
        })
    
    print(result.head())
    print(Border)


    print("Calculate Model Accuracy")

    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of the model is : ", accuracy * 100)
    print(Border)

    print("Confusion Matrix")
    cm = confusion_matrix(Y_test,Y_pred)
    print("Confusion Matrix is:")
    print(cm)
    print(Border)

    print("Plotting Confusion Matrix: ")
    data = ConfusionMatrixDisplay(confusion_matrix=cm , display_labels=model.classes_)
    data.plot()
    plt.title("Confusion Matrix of Student Performance Dataset")
    plt.show()



def main():
    Border = "-"*40
    print(Border)
    print("Student Performace Predictor")
    print(Border)

    LoadingDataset("student_performance_ml.csv")

if __name__ == "__main__":
    main()