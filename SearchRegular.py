import re

def search(str, word):
    patt = re.compile(fr'\b{re.escape(word)}\b')
    
    if patt.search(str):
        print("The word exists in the string.")
        return True
    else:
        print("The word does not exist in the string.") 
        return False


