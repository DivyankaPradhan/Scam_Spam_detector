import re
def detect(message,key):
    message=message.lower()
    matches=[]
    risk_score=0
    for category_nm, key_val in key.items():    #Key_val=value in key,items() gets all the key+values        
        for key_index in key_val :              #key_index=inner dict
            p=key_index["p"]                    #p=inner dicts value

            if p in message:
                matches.append(key_index)   #appended all the 'whole' inner dicts that contain the p
                risk_score+=key_index["w"]
    match=re.search(r"https?//\S+",message)    
    if match:
        url=match.group()
        url_match={
            "p":url,
            "w":25,
            "r":"URL detected in the message"}     
        matches.append(url_match)
        risk_score+=url_match["w"]  
    if risk_score<20:
        verdict="Safe"    
    elif risk_score<50:
        verdict="Suspicious"         
    else:
        verdict="Likely Scam"      
                    
    return matches,risk_score,verdict

