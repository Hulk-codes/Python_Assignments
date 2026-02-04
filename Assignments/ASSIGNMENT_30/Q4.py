import sys

def main():
    FileName = sys.argv[1]
    try:
        fobj = open(FileName, "w+")
        print("File gets successfully open")
        
        fobj.write("Python : Automation and Machine learning by BABA\n")
        fobj.seek(0)
        Data = fobj.read()

        Nobj=open("Demo.txt", "a")
        Nobj.write(Data)
        
        fobj.close()
        Nobj.close()
    
    finally:
        print("End of Application")
        
    

if __name__ == "__main__":
    main()