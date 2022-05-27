# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(firstword, secondword):
    # [assignment] Add your code here
    if len(firstword)==len(secondword):
   
        if (sorted(firstword)==sorted(secondword)):
            print("The strings are anagrams")   
        else:
             print("The strings are not anagrams")
        
    return True
firstword1=input("Enter first String\n")
secondword2=input("Enter Second string\n")
find_anagrams(firstword1,secondword2)
