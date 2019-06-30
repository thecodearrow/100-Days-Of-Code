#Write a function that takes two strings and returns True only if they are one edit away from each other! 

#CAN BE MODULARISED BETTER! 

def is_one_away(s1, s2):
    l1=len(s1)
    l2=len(s2)
    if(abs(l1-l2)>1): # Case 1
        return False 
    if(l1==l2): #Case 2
        off_count=0
        for i in range(l1):
            if(s1[i]!=s2[i]):
                off_count+=1
                
        if(off_count>1):
            return False
        return True
    else:  #Case 3
        if(l1<l2):
            s1+="*"
        else:
            s2+="*"
        off_count=0
        for i in range(l1):
            if(s1[i]!=s2[i]):
                off_count+=1
            if(i<l1-1):
                if(s1[i]==s2[i+1] or s2[i]==s1[i+1]):
                    off_count-=1
                    
        if(off_count>1):
            return False
        return True
                
        
            
    
    

# NOTE: The following input values will be used for testing your solution.
is_one_away("abcde", "abcd")  # should return True
is_one_away("abde", "abcde")  # should return True
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
is_one_away("aaa", "abc")  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False
