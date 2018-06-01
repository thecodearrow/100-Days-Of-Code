# May Lunchtime 2018 Division 2  » Count Substrings 

#PARTIALLY SOLVED!

from collections import defaultdict
 
def substrK(s,k):
    
    l=len(s)
    res=[]
    for i in range(0,l):
        substr={}
        decider=0
        substr=defaultdict(lambda:0,substr)
        distcount=0
        for j in range(i,l):
            if(substr[s[j]]==0):
                distcount+=1 
            substr[s[j]]+=1
            if(distcount>=k):
                decider=substr[s[i]]
                word=s[i:j+1]
                dontAdd=True
                for char in word:
                    if(substr[char]!=decider):
                        dontAdd=False
                        break
                
                if(dontAdd):
                    res.append(word)
                    
                
    
    return res 