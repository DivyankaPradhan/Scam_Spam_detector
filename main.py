import json
from detector import detect

with open("scan_keywords.json","r")as file:
    key=json.load(file)                                    #store the values of file
message=input("Enter a message: ")    

matches,risk_score,verdict=detect(message,key)                                #connects main with detector

'''Now bring the detect return value which is the 'whole' inner dicts'''

if matches:
    print("\nSuspicious patterns found!:\n")
    for match in matches:
        print(f"Key word :{match["p"]}")                      
        print(f"Weight :{match["w"]}")                    #prints until all the 'whole' inner dicts are over
        print(f"Reason:{match["r"]}\n")   
    
else:
    print("\nNo suspicious patterns found")  
print("----------------------------")    
print(f"\nTotal Risk Score : {risk_score}")   
print(f"Verdict:{verdict}")
