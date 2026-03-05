from sklearn.datasets import load_iris

def main():
    print("Iris Classification case Study")
    
    Dataset = load_iris()

    # MetaData of Dataset
    print("Independent Variables are : ")
    print(Dataset.feature_names)
    print("Length of Independent variables is : ", len(Dataset.feature_names))

    print("Dependent Variables are : " )
    print(Dataset.target_names)
    print("Length of dependent variables is : ", len(Dataset.target_names))

    
    
   
if __name__ == "__main__":
    main()