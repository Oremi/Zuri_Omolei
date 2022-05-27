# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

#code by Godwin Remilekun Omolei
#Student ID: 14G021587MXP

def find_anagram(word, anagram):
    # sort the word and anagram for comparison
    if(sorted(word) == sorted(anagram)):
        return True
    else:
        return False
