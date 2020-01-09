import string
user_text=open("new.txt",'r')
d = dict()
for line in user_text:
    line=line.strip()
    line=line.lower()
    line=line.translate(line.maketrans("","",string.punctuation))
    words=line.split(" ")
     
     
    for word in words:
        
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=1
        
    
for key in list(d.keys()):
    print(key,":",d[key])