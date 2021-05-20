# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Example:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

import string as str

def to_jaden_case(string):
    # ...
    # count = 0
    # for i in range(len(string)):
        
    #     if (count == 0):
    #         string[i].upper()
    #         count +=1
    #         i +=1
    #     elif (string[i] == " "):
    #         count = 0
    #         i += 1
    
    
    #   ============[using the list indecies to title the words, and join them]===============
    # myList = string.split(' ')
    # for i in myList:
    #     myList[i][0].upper()
    #     myList[i][1::].lower() 
    # # reString = myList.join(' ')
    # # return reString
    # return myList
    
    
    # ================[Trying the sting.capwords idea]======================

    return str.capwords(string)

print(to_jaden_case("how can mirrors be real if our eyes aren't real"))