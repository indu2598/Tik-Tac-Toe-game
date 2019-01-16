#draw boardfor tik tak toe game
import time
board = [""," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
ocount = 0
xcount = 0
count = 1
def for_space(n=10):
        for i in range(1,n):
            print(" ", end=" ")
 

def draw_board():
    for_space(7)
    print("MY TIK TAK TOE BOARD")
    for_space()
    print( board[1] +" | " +board[2] +"| "+ board[3] +"| " +board[4])
    for_space()
    print("--" + "|"+"--"+"|"+"--" + "|"+"--")
    for_space()
    print( board[5] +" | " +board[6] +"| "+ board[7]+"| " +board[8])
    for_space()
    print("--" + "|"+"--"+"|"+"--"+"|"+"--")
    for_space()
    print( board[9] +" | " +board[10] +"| "+ board[11]+"| " +board[12])
    for_space()
    print("--" + "|"+"--"+"|"+"--"+"|"+"--")
    for_space()
    print( board[13] +" | " +board[14] +"| "+ board[15]+"| " +board[16])

def isWinner(board,u):
    if ((board[1] == u and board[2]== u  and board[3]== u  and board[4]== u) or 
        (board[5] == u  and board[6]== u  and board[7]== u and board[8]== u ) or 
        (board[9] == u  and board[10]== u  and board[11]== u and board[12]== u) or 
        (board[13] == u  and board[14]== u  and board[15]== u and board[16]== u) or 
        (board[1] == u  and board[5]== u  and board[9]== u and board[13]== u) or 
        (board[2] == u  and board[6]== u  and board[10]== u and board[14]== u) or 
        (board[3] == u  and board[7]== u  and board[11]== u and board[15]== u) or 
        (board[4] == u  and board[8]== u  and board[12]== u and board[16]== u) or
        (board[1] == u  and board[6]== u  and board[11]== u and board[16]== u) or
        (board[4] == u  and board[7]== u  and board[10]== u and board[14]== u)
        ):
        return True
    else:
        return False
    
def isBoardFull(board):
    if " " in board:
        return False
    else:
        return True

    
    
while True:

    
    while True:
        if count == 1:
            count +=1
            draw_board()
        else:
            pass    
        break

    #Gets input for X
    while True:
        
        value = int(input("Enter number for X:"))
        if board[value]==" ":
            board[value]="X"
            draw_board()
            break
              
        else:
            print("Oops, Space is not empty!")

    #For X wins
    if isWinner(board,"X"):
        print("X Winner..!")
        break
        
    
    #Check board is empty or not
    if isBoardFull(board):
        print("There is a TIE between X and O !")
        break
        
    #Gets input for O
    while True:
        value = int(input("Enter number for O:"))
        if board[value]==" ":
            board[value]="O"
            draw_board()
            break  
        else:
            print("Oops, Space is not empty!")
        

    #For O wins
    
    if isWinner(board,"O"):
        print("O Winner..!")
        break
        

   #Check board is empty or not
    if isBoardFull(board):
        print("There is a TIE between X and O !")
        break