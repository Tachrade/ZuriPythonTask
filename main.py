
  

def find_anagrams(word,word2):
    # [assignment] Add your code here
    
     if(sorted(word) == sorted(word2)):
         print("True")
       
     else:
         print("False")
     
word = input("Enter First Word :")
word2 = input("Enter Second word :")
find_anagrams(word,word2)  

