import sys
import DirectoryModuleForQ2

def main():
    DirectoryModuleForQ2.Logfile("Automation Script started")
    
    

    try:
        if len(sys.argv) != 4:
            DirectoryModuleForQ2.Logfile("Invalid number of arguments")
            DirectoryModuleForQ2.Logfile("Usage: DirectoryFileSearch.py <DirectoryName> <Extension> <ReplacedExtension2>")
            return

        DirectoryName = sys.argv[1]
        Extension1 = sys.argv[2]
        ReplaceExtension2 = sys.argv[3]

        if DirectoryModuleForQ2.DirectoryScanner(DirectoryName):
            
            DirectoryModuleForQ2.ReplaceExtensionDoc(DirectoryName, Extension1, ReplaceExtension2)

    except Exception as e:
        DirectoryModuleForQ2.Logfile("Unexpected error occurred")

    finally:
        DirectoryModuleForQ2.Logfile("Automation Script Ended")


if __name__ == "__main__":
    main()