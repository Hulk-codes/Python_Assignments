import sys
import DirectoryModuleQ1

def main():
    DirectoryModuleQ1.Logfile("Automation Script started")
    
    

    try:
        if len(sys.argv) != 3:
            DirectoryModuleQ1.Logfile("Invalid number of arguments")
            DirectoryModuleQ1.Logfile("Usage: DirectoryFileSearch.py <DirectoryName> <Extension>")
            return

        DirectoryName = sys.argv[1]
        Extension = sys.argv[2]

        if DirectoryModuleQ1.DirectoryScanner(DirectoryName):
            DirectoryModuleQ1.DirectoryFileWithExtension(DirectoryName, Extension)

    except Exception as e:
        DirectoryModuleQ1.Logfile("Unexpected error occurred")

    finally:
        DirectoryModuleQ1.Logfile("Automation Script Ended")


if __name__ == "__main__":
    main()