import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
       return data[w]
    elif w.upper() in data:
       return data[w.upper()]
    elif w.title() in data:
       return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
         yn = input("Do you mean %s ?, If YES then Enter Y/y, if NO then Enter N/n: " % get_close_matches(w,data.keys())[0])
         if yn == "Y" or yn == "y":
            return data[get_close_matches(w,data.keys())[0]]
         elif yn== "N" or yn=="n":
             return("The word is not included in the dictionary")
         else:
               return("Please Enter Y or N Only!")
    else:
         return("Word Does not exist, please check again!")
word=input("Enter the Word to be Searched: ")

output=translate(word)
if type(output) == list:
    for item in output:

            print("*"+item )
else:
    print(output)
