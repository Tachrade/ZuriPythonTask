# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        lines = f.read()
        lines = read_file_content(filename)
        print(lines)
        return lines


def count_words():
 text = read_file_content("./story.txt").split()
# [assignment] Add your code here
#Create Empty Dictionary
 d = dict()
 #loop through each line
 for line in text:
     #remove
     line = line.strip( )
     line = line.lower()
     line = line.translate(str.maketrans('', '', string.punctuation))
     words = line.split(" ")
 for word in words:
    if word in d:
        d[word] = d[word] + 1
    else:
         d[word] = 1
    for key in list(d.keys()):
        print(key, ":", d[key])
        view = count_words()
        print(view)

