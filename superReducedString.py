#!/bin/python3
"""

HACKERRANK PRACTICE STRINGS

Sample Input 0

aaabccddd

Sample Output 0

abd

Sample Case 0

Steve can perform the following sequence of operations to get the final string:

aaabccddd → abccddd
abccddd → abddd
abddd → abd
Thus, we print abd.

"""
import sys
from collections import OrderedDict

s = input().strip()
letters= sorted(set(s))
boo=True

def Checker(string):
    for char in letters:
        if(string.count(char+char)):
            return(True)
    return False
    
def super_reduced_string(s):
    # Complete this function
   
    
    while(Checker(s)):   
        for char in letters:
            occur=char+char
            s=s.replace(occur,'')


        if(len(s)!=0):
            result=s
        else:
            result="Empty String"
    
    return(result)

result = super_reduced_string(s)
print(result)
