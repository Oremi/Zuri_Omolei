# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#code by Godwin Remilekun Omolei
#Student ID: I4G021587MXP

def read_file_content(filename):
    
    with open(filename) as f:
        contents = f.read().splitlines()
    return contents

def count_words():
    unique_words = dict()
    text = read_file_content("./story.txt")    
    
    for unique in text:
        #remove new lines and extra space characters
        
        unique = unique.strip()
        
        unique = unique.lower()

        #seperating into key-value pair
        
        lines = unique.split()

        for line in lines:
            if line in unique_words:
                unique_words[line] = unique_words[line]+1
            else:
                unique_words[line] = 1
    
    return unique_words

