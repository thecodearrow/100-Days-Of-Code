
#Matrix Game Problem Code: ICL1801

"""
2 players, Cyborg and Geno are playing a game on a matrix. In each turn, the player choses a number from the matrix which is not selected yet and adds the number to his sum. In the end, the player with the largest sum wins the game.

Assuming both players play optimally and Cyborg starts the game, predict who will be the winner of the game. Assume that the initial sum is 0 for both the players.

"""

t=int(input())
while(t!=0):
    t=t-1
    [n,m]=input().strip().split(" ")
    [n,m]=[int(n),int(m)]
    
    list=[]
    for i in range(n):
        row=input().strip().split(" ")
        row=[int(x) for x in row]
        list.append(row)
    
    def maxEleIndex():
        maxim=0
        for i in range(n):
            ele=max(list[i])
            if(ele>=maxim):
                maxim=ele
                index=i
                pos=list[i].index(ele)
        return([maxim,index,pos])
    cyborg=0
    geno=0
    for i in range(n*m):
        maximum,r,c=maxEleIndex()
        if(i%2==0):
            cyborg=cyborg+maximum
        else:
            geno=geno+maximum
        list[r][c]=0
    if(cyborg>geno):
        print("Cyborg")
    elif(geno>cyborg):
        print("Geno")
    else:
        print("Draw")
        