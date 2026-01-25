
def CheckVowel(char):
    
    if char in  ("a","e","i","i","o","u"):
        print("this is vowel")
    else:
        print("not a vowel")



def main():
    ch = input("enter a aplhabet: ")
    CheckVowel(ch)

if __name__ == "__main__":
    main()