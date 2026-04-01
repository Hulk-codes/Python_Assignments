import numpy as np
import math

def EuclidDist(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

def KneighbourClassifier():
    Border = "-" * 50
    data = [
                {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
                {'point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
                {'point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
                {'point' : 'D', 'X' : 6, 'Y' : 5, 'label' : 'Blue'}
            
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
    X_new = int(input("Enter New X point : "))
    Y_new = int(input("Enter New Y point : "))

    
    new_point = {'X' : X_new, 'Y' : Y_new} 
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

    k = 1
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
