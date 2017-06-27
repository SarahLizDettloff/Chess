# chess
# Move
This chess project tackles the movement of chess pieces concerning algebraic notation. <br />
It allows you to type in any chess piece name in all lower case along with the coordinates of that particular piece to retrieve all possible moves for that piece assuming no other pieces are on the board. <br />
Example: <br />
Output: Type in the name of the piece you want to see the potential moves of. <br />
input: knight <br />
Output: Enter the location of that piece:  <br />
input: d3 <br />
output: ('Possible Knight Moves ', ['b4', 'c5', 'e5', 'f4', 'f2', 'e1', 'c1', 'b2']) <br />

# Installing
This program was created in Python Shell 2.7.11 <br />
To download Python 2.7.11 follow the link below:  <br />
https://www.python.org/downloads/release/python-2711/ <br />
Step 1: Download Python 2.7.11 installer<br />
Step 2: Open IDLE(Python GUI)<br />
Step 3: Save file as .py<br />
Step 4: Run and enjoy!<br />

# Debugging Coverage
Line 17: <br />
	print ("Possible Rook Moves" + possibleRookMoves(pieceLocation, board)) <br />
	strRookMoves = possibleRookMoves(pieceLocation, board) <br />
	print ("Possible Rook Moves" + strRookMovs) <br />
Line 135: <br />
	if board[x+2][y] == "" and x== 1 and board[x+1][y] == "" <br />
        	possibleMoves.[[x+1],[y-2]] <br />
Line 110{ <br />
indextoMatrix{ <br />
   0 == "a", <br />
   1 == "b", <br />
   2 == "c", <br />
   3 == "d", <br />
   4 == "e", <br />
   5 == "f", <br />
   6 == "g", <br />
   7 == "h" <br />
} <br />
# Works Cited: <br />
David Moeser, ASCII Chess Pieces, http://www.chessvariants.com/d.pieces/ascii.html(1996) <br />
