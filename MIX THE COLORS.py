# March Challenge 2018 DIV 2 

"""
Chef likes to mix colors a lot. Recently she was gifted N colors by her friend. This is given to you by an array A of size N, where Ai denotes the value of the i-th color, which is a number from 1 to 109.

Chef wants to make all her color values distinct as they will then look stunningly beautiful. For achieving that, she can perform the following mixing operation zero or more times.

Choose any two colors in the array. Let their values be x and y. Mix the color with value x into the color with value y. After the mixing, the value of the first color stays x itself, but that of the second color changes to x + y.
Find the minimum number of mixing operations Chef needs to do to make her colors beautiful.


"""

t=int(input())

while(t!=0):
    t=t-1
    n=int(input())
    colors=[int(x) for x in input().strip().split()]
    set_colors=set(colors) #distinct colors
    print(len(colors)-len(set_colors)) 
