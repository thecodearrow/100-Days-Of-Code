#https://www.hackerrank.com/contests/university-codesprint-5/challenges/exceeding-speed-limit

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if(s<=90):
        print("0 No punishment")
    elif(s>90 and s<=110):
        fine=(s-90)*300
        print(fine,"Warning")
        
    elif(s>110):
        fine=(s-90)*500
        print(fine,"License removed")
        

if __name__ == '__main__':
    s = int(input().strip())

    solve(s)

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if(s<=90):
        print("0 No punishment")
    elif(s>90 and s<=110):
        fine=(s-90)*300
        print(fine,"Warning")
        
    elif(s>110):
        fine=(s-90)*500
        print(fine,"License removed")
        

if __name__ == '__main__':
    s = int(input().strip())

    solve(s)
