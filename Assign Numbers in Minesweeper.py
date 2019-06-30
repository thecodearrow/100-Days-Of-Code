#Assign Numbers in Minesweeper 

def mine_sweeper(bombs, num_rows, num_cols):
 
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    
    for b in bombs:
        x,y=b[0],b[1]
        field[x][y]=-1
        
    for b in bombs:
        x,y=b[0],b[1]
        for row in range(x-1,x+2):
            if(row>=0 and row<num_rows):
                for col in range(y-1,y+2):
                    if(col>=0 and col<num_cols):
                        if(field[row][col]!=-1): #NOT BOMB 
                            field[row][col]+=1
                
       
            
        
            
    
        
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
# mine_sweeper([[0, 2], [2, 0]], 3, 3) should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

# mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

# mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]