####Sarah Dettloff

###June 26th 2017


import os
import sys


chessPieceDict = {
    "Rook": """
 WWWWWW
  |  |
  |  | 
  |__|
 (____)
(______)
    """,
    "Pawn": """
  __
 (  )   
  ||   
 (__)  
(____)
    """,
    "Queen": 
    """
    ()   
  <~~~~>  
   \__/    
  (____)   
   |  | 
   |  | 
   |__|  
  (____)  
 (______) 
(________)  
    """,
    "Knight":
"""

 __/''')
]___ 0  } 
    /   }
   /~    }
   \____)
   /____)
  (______)
    """,
    "bishop": 
"""
  <>_ 
 (\)  )
 (____)   
  \__/ 
 (____)
  |  |
  |__|   
 (____)
(______) """,
    "King": """
    .::.          
    _::_  
  _/____\_  
  \      /   
   \____/   
   (____)  
    |  |   
    |__| 
   /    )
  (______) 
 (________)
 (________) 
    """}

def newgame():
    clear = lambda: os.system('cls')
    clear()

def run():
    board = [[0] * 8 for x in xrange(8)]
    pieceType=raw_input("Type in the name of the piece you want to see the potential moves of.\n")
    pieceLocation=raw_input("Enter the location of that piece: \n")
    if pieceLocation[1] == "9":
        print("The maximum number that can be entered is '8'.")
        newgame()
        main()
    else:
        while len(pieceLocation) < 3:
            if (pieceType == "rook"):
                print ("Possible Rook Moves", possibleRookMoves(pieceLocation, board))
                print(chessPieceDict["Rook"])
                break
            elif (pieceType == "knight"):
                print ("Possible Knight Moves ", possibleKnightMoves(pieceLocation, board))
                print(chessPieceDict["Knight"])
                break
            elif (pieceType == "queen"):
                print ("Possible Queen Moves ", possibleQueenMoves(pieceLocation, board))
                print(chessPieceDict["Queen"])
                break
            elif (pieceType == "bishop"):
                print ("Possible Bishop Moves", possibleBishopMoves(pieceLocation, board))
                print(chessPieceDict["bishop"])
                break
            elif (pieceType == "pawn"):
                print ("Possible Pawn Moves", possiblePawnMoves(pieceLocation, board))
                print(chessPieceDict["Pawn"])
                break
            elif (pieceType == "king"):
                print ("Possible King Moves", possibleKingMoves(pieceLocation, board))
                print(chessPieceDict["King"])
                break
            else:
                print("Please enter a valid chess piece.\nExample: rook, knight, queen, bishop, pawn, king")
                clear = lambda: os.system('cls')
                clear()
                break
                newgame()
                
        else:
            print("Please enter one letter and one digit.")
            newgame()
        main()

def Matrix():
    global indextoMatrix
    indextoMatrix = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h",
}
    global matrixtoIndex
    matrixtoIndex = {
   "a" : 0,
   "b" : 1,
   "c" : 2,
   "d" : 3,
   "e" : 4,
   "f" : 5,
   "g" : 6,
   "h" : 7,
}
    
def possibleKnightMoves(position, board):
    possibleMoves = []
    Matrix()
    yCoordinates, xCoordinates = list(position.strip().lower())
    xCoordinates = int(xCoordinates) - 1
    yCoordinates = matrixtoIndex[yCoordinates]
    x,y = xCoordinates, yCoordinates
    try:
        tryMove = board[x + 1][y - 2]
        possibleMoves.append([x + 1, y - 2])
    except:
        pass
    try:
        tryMove = board[x + 2][y - 1]
        possibleMoves.append([x + 2, y - 1])
    except:
        pass
    try:
        tryMove = board[x + 2][y + 1]
        possibleMoves.append([x + 2, y + 1])
    except:
        pass
    try:
       tryMove = board[x + 1][y + 2]
       possibleMoves.append([x + 1, y + 2])
    except:
        pass
    try:
        tryMove = board[x - 1][y + 2]
        possibleMoves.append([x - 1, y + 2])
    except:
        pass
    try:
        tryMove = board[x - 2][y + 1]
        possibleMoves.append([x - 2, y + 1])
    except:
        pass
    try:
        tryMove = board[x - 2][y - 1]
        possibleMoves.append([x - 2, y - 1])
    except:
        pass
    try:
        tryMove = board[x - 1][y - 2]
        possibleMoves.append([x - 1, y - 2])
    except:
        pass
    
    tryMove = [x for x in possibleMoves if x[0] >=0 and x[1] >=0]
    allPossibleMoves = tryMove
    allPossibleMoves = ["".join([indextoMatrix[x[1]], str(x[0] + 1)]) for x in tryMove]
    return allPossibleMoves
    


def possibleQueenMoves(position, board): 
    possibleMoves = []
    Matrix()
    yCoordinates, xCoordinates = list(position.strip().lower())
    xCoordinates = int(xCoordinates) - 1
    yCoordinates = matrixtoIndex[yCoordinates]
    x,y = xCoordinates, yCoordinates
    try:
       tryMove = board[x + 1][y + 1]
       possibleMoves.append([x + 1, y + 1])
    except:
        pass
    try:
       tryMove = board[x - 1][y - 2]
       possibleMoves.append([x - 1, y - 2])
    except:
        pass
    try:
       tryMove = board[x - 1][y - 1]
       possibleMoves.append([x - 1, y - 1])
    except:
        pass
    try:
       tryMove = board[x - 1][y + 1]
       possibleMoves.append([x - 1, y + 1])
    except:
        pass
    try:
        tryMove = board[x + 2][y + 2]
        possibleMoves.append([x + 2, y + 2])
    except:
        pass
    try:
       tryMove = board[x + 2][y - 2]
       possibleMoves.append([x + 2, y - 2])
    except:
        pass
    try:
        tryMove = board[x - 2][y + 2]
        possibleMoves.append([x - 2, y + 2])
    except:
        pass
    try:
       tryMove = board[x - 2][y - 2]
       possibleMoves.append([x - 2, y - 2])
    except:
        pass
    try:
        tryMove = board[x + 3][y + 3]
        possibleMoves.append([x + 3, y + 3])
    except:
        pass
    try:
       tryMove = board[x + 3][y - 3]
       possibleMoves.append([x + 3, y - 3])
    except:
        pass
    try:
        tryMove = board[x - 3][y + 3]
        possibleMoves.append([x - 3, y + 3])
    except:
        pass
    try:
       tryMove = board[x - 3][y - 3]
       possibleMoves.append([x - 3, y - 3])
    except:
        pass
    try:
        tryMove = board[x + 4][y + 4]
        possibleMoves.append([x + 4, y + 4])
    except:
        pass
    try:
       tryMove = board[x + 4][y - 4]
       possibleMoves.append([x + 4, y - 4])
    except:
        pass
    try:
       tryMove = board[x - 4][y - 4]
       possibleMoves.append([x - 4, y - 4])
    except:
        pass
    try:
        tryMove = board[x + 5][y + 5]
        possibleMoves.append([x + 5, y + 5])
    except:
        pass
    try:
       tryMove = board[x + 5][y - 5]
       possibleMoves.append([x + 5, y - 5])
    except:
        pass
    try:
        tryMove = board[x - 5][y + 5]
        possibleMoves.append([x - 5, y + 5])
    except:
        pass
    try:
       tryMove = board[x - 5][y - 5]
       possibleMoves.append([x - 5, y - 5])
    except:
        pass
    try:
        tryMove = board[x + 6][y + 6]
        possibleMoves.append([x + 6, y + 6])
    except:
        pass
    try:
       tryMove = board[x + 6][y - 6]
       possibleMoves.append([x + 6, y - 6])
    except:
        pass
    try:
       tryMove = board[x - 6][y - 6]
       possibleMoves.append([x - 6, y - 6])
    except:
        pass
    try:
       tryMove = board[x - 6][y + 6]
       possibleMoves.append([x - 6, y + 6])
    except:
        pass
    try:
        tryMove = board[x + 7][y + 7]
        possibleMoves.append([x + 7, y + 7])
    except:
        pass
    try:
       tryMove = board[x + 7][y - 7]
       possibleMoves.append([x + 7, y - 7])
    except:
        pass
    try:
       tryMove = board[x - 7][y - 7]
       possibleMoves.append([x - 7, y - 7])
    except:
        pass
    try:
       tryMove = board[x - 7][y + 7]
       possibleMoves.append([x - 7, y + 7])
    except:
        pass
    try:
        for y in xrange(8):
            if y != yCoordinates:
                possibleMoves.append((xCoordinates, y))
        for x in xrange(8):
            if x != xCoordinates:
                possibleMoves.append((x, yCoordinates))
    except:
        pass
    
    tryMove = [x for x in possibleMoves if x[0] >=0 and x[1] >=0]
    allPossibleMoves = tryMove
    allPossibleMoves = ["".join([indextoMatrix[x[1]], str(x[0] + 1)]) for x in tryMove]
    return allPossibleMoves

def possibleBishopMoves(position,board):
    possibleMoves = []
    Matrix()
    yCoordinates, xCoordinates = list(position.strip().lower())
    xCoordinates = int(xCoordinates) - 1
    yCoordinates = matrixtoIndex[yCoordinates]
    x,y = xCoordinates, yCoordinates
    try:
       tryMove = board[x - 1][y - 1]
       possibleMoves.append([x - 1, y - 1])
    except:
        pass
    try:
       tryMove = board[x + 1][y + 1]
       possibleMoves.append([x + 1, y + 1])
    except:
        pass
    try:
       tryMove = board[x + 1][y - 1]
       possibleMoves.append([x + 1, y - 1])
    except:
        pass
    try:
       tryMove = board[x - 1][y + 1]
       possibleMoves.append([x - 1, y + 1])
    except:
        pass
    try:
        tryMove = board[x + 2][y + 2]
        possibleMoves.append([x + 2, y + 2])
    except:
        pass
    try:
       tryMove = board[x + 2][y - 2]
       possibleMoves.append([x + 2, y - 2])
    except:
        pass
    try:
        tryMove = board[x - 2][y + 2]
        possibleMoves.append([x - 2, y + 2])
    except:
        pass
    try:
       tryMove = board[x - 2][y - 2]
       possibleMoves.append([x - 2, y - 2])
    except:
        pass
    try:
        tryMove = board[x + 3][y + 3]
        possibleMoves.append([x + 3, y + 3])
    except:
        pass
    try:
       tryMove = board[x + 3][y - 3]
       possibleMoves.append([x + 3, y - 3])
    except:
        pass
    try:
        tryMove = board[x - 3][y + 3]
        possibleMoves.append([x - 3, y + 3])
    except:
        pass
    try:
       tryMove = board[x - 3][y - 3]
       possibleMoves.append([x - 3, y - 3])
    except:
        pass
    try:
        tryMove = board[x + 4][y + 4]
        possibleMoves.append([x + 4, y + 4])
    except:
        pass
    try:
       tryMove = board[x + 4][y - 4]
       possibleMoves.append([x + 4, y - 4])
    except:
        pass
    try:
       tryMove = board[x - 4][y - 4]
       possibleMoves.append([x - 4, y - 4])
    except:
        pass
    try:
       tryMove = board[x - 4][y + 4]
       possibleMoves.append([x - 4, y + 4])
    except:
        pass
    try:
        tryMove = board[x + 5][y + 5]
        possibleMoves.append([x + 5, y + 5])
    except:
        pass
    try:
       tryMove = board[x + 5][y - 5]
       possibleMoves.append([x + 5, y - 5])
    except:
        pass
    try:
        tryMove = board[x - 5][y + 5]
        possibleMoves.append([x - 5, y + 5])
    except:
        pass
    try:
       tryMove = board[x - 5][y - 5]
       possibleMoves.append([x - 5, y - 5])
    except:
        pass
    try:
        tryMove = board[x + 6][y + 6]
        possibleMoves.append([x + 6, y + 6])
    except:
        pass
    try:
       tryMove = board[x + 6][y - 6]
       possibleMoves.append([x + 6, y - 6])
    except:
        pass
    try:
       tryMove = board[x - 6][y - 6]
       possibleMoves.append([x - 6, y - 6])
    except:
        pass
    try:
       tryMove = board[x - 6][y + 6]
       possibleMoves.append([x - 6, y + 6])
    except:
        pass
    try:
        tryMove = board[x + 7][y + 7]
        possibleMoves.append([x + 7, y + 7])
    except:
        pass
    try:
       tryMove = board[x + 7][y - 7]
       possibleMoves.append([x + 7, y - 7])
    except:
        pass
    try:
       tryMove = board[x - 7][y - 7]
       possibleMoves.append([x - 7, y - 7])
    except:
        pass
    try:
       tryMove = board[x - 7][y + 7]
       possibleMoves.append([x - 7, y + 7])
    except:
        pass
    try:
        tryMove = board[x + 8][y + 8]
        possibleMoves.append([x + 8, y + 8])
    except:
        pass
    try:
       tryMove = board[x + 8][y - 8]
       possibleMoves.append([x + 8, y - 8])
    except:
        pass
    try:
       tryMove = board[x - 8][y - 8]
       possibleMoves.append([x - 8, y - 8])
    except:
        pass
    try:
       tryMove = board[x - 8][y + 8]
       possibleMoves.append([x - 8, y + 8])
    except:
        pass
    
    tryMove = [x for x in possibleMoves if x[0] >=0 and x[1] >=0]
    allPossibleMoves = tryMove
    allPossibleMoves = ["".join([indextoMatrix[x[1]], str(x[0] + 1)]) for x in tryMove]
    return allPossibleMoves

def possiblePawnMoves(position, board): 
    possibleMoves = []
    Matrix()
    yCoordinates, xCoordinates = list(position.strip().lower())
    xCoordinates = int(xCoordinates) - 1
    yCoordinates = matrixtoIndex[yCoordinates]
    x,y = xCoordinates, yCoordinates
    pawnFirst=raw_input("Is this the first move of the pawn? Enter 'y' for yes, or anything else for no. \n")
    if pawnFirst == "y":
        try:
            tryMove = board[x + 1][y]
            possibleMoves.append([x + 1, y])
        except:
            pass
        try:
            tryMove = board[x + 2][y]
            possibleMoves.append([x + 2, y])
        except:
            pass
    else:
        pawnAttack=raw_input("Does this pawn move consist of an taking a piece? Enter 'y' for yes, or anything else for no\n")
        if pawnAttack == "y":
            tryMove = board[x + 1][y - 1]
            possibleMoves.append([x + 1, y - 1])
            tryMove = board[x + 1][y]
            possibleMoves.append([x + 1, y])
            tryMove = board[x - 1][y - 1]
            possibleMoves.append([x - 1, y - 1])
            tryMove = board[x - 1][y]
            possibleMoves.append([x - 1, y])
        else:
            try:
                tryMove = board[x + 1][y]
                possibleMoves.append([x + 1, y])
            except:
                pass
            
    tryMove = [x for x in possibleMoves if x[0] >=0 and x[1] >=0]
    allPossibleMoves = tryMove
    allPossibleMoves = ["".join([indextoMatrix[x[1]], str(x[0] + 1)]) for x in tryMove]
    return allPossibleMoves

def possibleRookMoves(position, board):
    possibleMoves = []
    Matrix()
    yCoordinates, xCoordinates = list(position.strip().lower())
    xCoordinates = int(xCoordinates) - 1
    yCoordinates = matrixtoIndex[yCoordinates]
    x,y = xCoordinates, yCoordinates
    try:
        for y in xrange(8):
            if y != yCoordinates:
                possibleMoves.append((xCoordinates, y))
        for x in xrange(8):
            if x != xCoordinates:
                possibleMoves.append((x, yCoordinates))
    except:
        pass

    tryMove = [x for x in possibleMoves if x[0] >=0 and x[1] >=0]
    allPossibleMoves = tryMove
    allPossibleMoves = ["".join([indextoMatrix[x[1]], str(x[0] + 1)]) for x in tryMove]
    return allPossibleMoves

def possibleKingMoves(position, board):
    possibleMoves = []
    Matrix()
    yCoordinates, xCoordinates = list(position.strip().lower())
    xCoordinates = int(xCoordinates) - 1
    yCoordinates = matrixtoIndex[yCoordinates]
    x,y = xCoordinates, yCoordinates
    try:
        tryMove = board[x + 1][y]
        possibleMoves.append([x + 1, y])
    except:
        pass
    try:
        tryMove = board[x + 1][y + 1]
        possibleMoves.append([x + 1, y + 1])
    except:
        pass
    try:
       tryMove = board[x + 1][y - 1]
       possibleMoves.append([x + 1, y - 1])
    except:
        pass
    try:
       tryMove = board[x][y + 1]
       possibleMoves.append([x, y + 1])
    except:
        pass
    try:
       tryMove = board[x][y - 1]
       possibleMoves.append([x, y - 1])
    except:
        pass
    try:
       tryMove = board[x - 1][y]
       possibleMoves.append([x - 1, y])
    except:
        pass
    try:
       tryMove = board[x - 1][y + 1]
       possibleMoves.append([x - 1, y + 1])
    except:
        pass
    try:
       tryMove = board[x - 1][y - 1]
       possibleMoves.append([x - 1, y - 1])
    except:
        pass
                        
    tryMove = [x for x in possibleMoves if x[0] >=0 and x[1] >=0]
    allPossibleMoves = tryMove
    allPossibleMoves = ["".join([indextoMatrix[x[1]], str(x[0] + 1)]) for x in tryMove]
    return allPossibleMoves

def main():
    run()
    newgame()

if __name__ == '__main__':
    main()
