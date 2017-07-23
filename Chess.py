# Sarah Dettloff
# July 23rd 2017
# Chess Console Application
# This program displays the potential moves on chessboard by piece type and coordinates.

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
    
def newgame():
    clear = lambda: os.system('cls')
    clear()

def run():
    board = [[0] * 8 for x in xrange(8)]
    pieceType=raw_input("Enter the type of the piece: \n")
    pieceLocation=raw_input("Enter the location of that piece: \n")
    if (pieceLocation[0] == "a") or (pieceLocation[0] == "b") or (pieceLocation[0] == "c") or (pieceLocation[0] == "d") or (pieceLocation[0] == "e") or (pieceLocation[0] == "f") or (pieceLocation[0] == "g") or (pieceLocation[0] == "h"):
        if (pieceLocation[1] == "9") or (pieceLocation[1] == "0"):
            print("The maximum number that can be entered is '8'.\nThe lowest number that can be entered is '1'.")
            newgame()
            main()
        else:
            while len(pieceLocation) < 3:
                if (pieceType == "rook") or (pieceType == "Rook"):
                    print ("Possible Rook Moves", sorted(possibleRookMoves(pieceLocation, board)))
                    print(chessPieceDict["Rook"])
                    break
                elif (pieceType == "knight") or (pieceType == "Knight"):
                    print ("Possible Knight Moves ", sorted(possibleKnightMoves(pieceLocation, board)))
                    print(chessPieceDict["Knight"])
                    break
                elif (pieceType == "queen") or (pieceType == "Queen"):
                    print ("Possible Queen Moves ", sorted(possibleQueenMoves(pieceLocation, board)))
                    print(chessPieceDict["Queen"])
                    break
                elif (pieceType == "bishop") or (pieceType == "Bishop"):
                    print ("Possible Bishop Moves", sorted(possibleBishopMoves(pieceLocation, board)))
                    print(chessPieceDict["bishop"])
                    break
                elif (pieceType == "pawn") or (pieceType == "Pawn"):
                    print ("Possible Pawn Moves", sorted(possiblePawnMoves(pieceLocation, board)))
                    print(chessPieceDict["Pawn"])
                    break
                elif (pieceType == "king") or (pieceType == "King"):
                    print ("Possible King Moves", sorted(possibleKingMoves(pieceLocation, board)))
                    print(chessPieceDict["King"])
                    break
                    
                else:
                    print("Please enter a valid chess piece.\nExample: Rook, Knight, Queen, Bishop, Pawn, or King.")
                    break   
            else:
                print("Please enter one letter(a-h) and one digit(1-8).")
                main()
    else:
        print("Please enter a valid coordinates.\nThe first digit must be a letter a-h.")
        newgame()
        main()
    main()

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
       tryMove = board[x + 1][y + 2]
       possibleMoves.append([x + 1, y + 2])
    except:
        pass
    try:
        tryMove = board[x - 1][y - 2]
        possibleMoves.append([x - 1, y - 2])
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
        tryMove = board[x + 2][y - 1]
        possibleMoves.append([x + 2, y - 1])
    except:
        pass
    try:
        tryMove = board[x + 2][y + 1]
        possibleMoves.append([x + 2, y + 1])
    except:
        pass
    tryMove = [x for x in possibleMoves if x[0] >=0 and x[1] >=0]
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
       tryMove = board[x + 1][y - 1]
       possibleMoves.append([x + 1, y - 1])
    except:
        pass
    try:
       tryMove = board[x + 1][y + 1]
       possibleMoves.append([x + 1, y + 1])
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
            try:
                tryMove = board[x + 1][y - 1]
                possibleMoves.append([x + 1, y - 1])
            except:
                pass
            try:
                tryMove = board[x + 1][y]
                possibleMoves.append([x + 1, y])
            except:
                pass
            try:
                tryMove = board[x - 1][y - 1]
                possibleMoves.append([x - 1, y - 1])
            except:
                pass
            try:
                tryMove = board[x - 1][y]
                possibleMoves.append([x - 1, y])
            except:
                pass
        else:
            try:
                tryMove = board[x + 1][y]
                possibleMoves.append([x + 1, y])
            except:
                pass
    tryMove = [x for x in possibleMoves if x[0] >=0 and x[1] >=0]
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
    allPossibleMoves = ["".join([indextoMatrix[x[1]], str(x[0] + 1)]) for x in tryMove]
    return allPossibleMoves

def main():
    run()
    newgame()

if __name__ == '__main__':
    main()
