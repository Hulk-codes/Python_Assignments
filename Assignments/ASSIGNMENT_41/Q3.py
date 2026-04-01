import numpy as np
import math

def EuclidDist(P1,P2):
    Ans = math.sqrt((P1['StudyHours'] - P2['StudyHours'])**2 + (P1['Attendance'] - P2['Attendance'])**2)
    return Ans

def KneighbourClassifier():
    Border = "-" * 50
    data = [
                {'point' : 'A', 'StudyHours' : 2, 'Attendance' : 60, 'label' : 'Fail'},
                {'point' : 'B', 'StudyHours' : 5, 'Attendance' : 80, 'label' : 'Pass'},
                {'point' : 'C', 'StudyHours' : 6, 'Attendance' : 85, 'label' : 'Pass'},
                {'point' : 'D', 'StudyHours' : 1, 'Attendance' : 50, 'label' : 'Fail'}
            
            ]
    print(Border)
    print("Marvellous UserDefined KNN")
    print(Border)

    print(Border)
    print("Training Data Set")
    print(Border)

    for i in data:
        print(i)

    print(Border)
    X_new = int(input("Enter Study Hours : "))
    Y_new = int(input("Enter Attendance : "))

    
    new_point = {'StudyHours' : X_new, 'Attendance' : Y_new} 
    for d in data:
        d['distance'] = EuclidDist(d,new_point)

    print(Border)
    print("Calculated Distances are: ")
    print(Border)

    for d in data:
        print(d)

    sorted_data = sorted(data, key=lambda item : item['distance'])

    print(Border)
    print("Sorted Data is : ")
    print(Border)

    for d in sorted_data:
        print(d)

    k = 3
    nearest = sorted_data[:k]

    print(Border)
    print("Nearest 3 elements are: ")
    print(Border)

    for d in nearest:
        print(d)

    # Voting
    votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label, 0) + 1

    print(Border)
    print("Voting result is : ")
    print(Border)

    for d in votes:
        print("Name : ",d, "Number of Votes : ",votes[d])
        
    print(Border)

    predicted_class = max(votes, key=votes.get)

    print("Predicted Class of (3,3) is : ",predicted_class)


def main():
    KneighbourClassifier()

if __name__ == "__main__":
    main()
