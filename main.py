# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

#code by Godwin Remilekun Omolei
#Student ID: I4G021587MXP

def find_anagram(word, anagram):
    # sort the word and anagram for comparison
    if(sorted(word) == sorted(anagram)):
        return True
    else:
        return False

print("This is a program to find if a word matches an anagram\n")

word = input("please enter a word to check if it matches an anagram: ")
print("This is the word:", word)
    
anagram = input("please enter an anagram to check with the word: ")
print("This is the anagram:", anagram)

print(f"\nchecking... {word} and {anagram}")

print(f"checked\n")
print(f"Result: {find_anagram(word, anagram)}")
