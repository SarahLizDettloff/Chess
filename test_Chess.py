# Sarah Dettloff
# July 23rd 2017
# Unit Test for Chess.py

from Chess import *
import unittest

listQueenMovesTest = {
    "a1" : ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
    "h1" : ['g2','f3', 'e4', 'd5', 'c6', 'b7', 'a8', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
    "a8" : ['b7', 'c6', 'd5', 'f3', 'g2', 'h1', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'],
    "h8" : ['g7', 'f6', 'e5', 'd4', 'c3', 'b2', 'a1', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
    "d4" : ['e5', 'c5', 'b6', 'c3', 'e3', 'f6', 'f2', 'b2', 'g7', 'a7', 'g1', 'a1', 'h8', 'a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8'],
    "e4" : ['d5', 'f5', 'd3', 'f3', 'g6', 'c6', 'g2', 'c2', 'h7', 'b7', 'h1', 'b1', 'a8', 'a4', 'b4', 'c4', 'd4', 'f4', 'g4', 'h4', 'e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8']
    }
listRookMovesTest = { 
    "a1" : ['b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
    "h1" : ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
    "a8" : ['b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'],
    "h8" : ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
    "d4" : ['a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8'],
    "e4" : ['a4', 'b4', 'c4', 'd4', 'f4', 'g4', 'h4', 'e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8']
    }
listBishopMovesTest = { 
    "a1" : ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
    "h1" : ['g2', 'f3', 'e4',# Sarah Dettloff
# July 22nd 2017
# Test for chess console application

from Chess import *
import unittest

listQueenMovesTest = {
    "a1" : ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
    "h1" : ['g2','f3', 'e4', 'd5', 'c6', 'b7', 'a8', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
    "a8" : ['b7', 'c6', 'd5', 'f3', 'g2', 'h1', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'],
    "h8" : ['g7', 'f6', 'e5', 'd4', 'c3', 'b2', 'a1', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
    "d4" : ['e5', 'c5', 'b6', 'c3', 'e3', 'f6', 'f2', 'b2', 'g7', 'a7', 'g1', 'a1', 'h8', 'a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8'],
    "e4" : ['d5', 'f5', 'd3', 'f3', 'g6', 'c6', 'g2', 'c2', 'h7', 'b7', 'h1', 'b1', 'a8', 'a4', 'b4', 'c4', 'd4', 'f4', 'g4', 'h4', 'e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8']
    }
listRookMovesTest = { 
    "a1" : ['b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
    "h1" : ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
    "a8" : ['b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'],
    "h8" : ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
    "d4" : ['a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8'],
    "e4" : ['a4', 'b4', 'c4', 'd4', 'f4', 'g4', 'h4', 'e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8']
    }
listBishopMovesTest = { 
    "a1" : ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
    "h1" : ['g2', 'f3', 'e4', 'd5', 'c6', 'b7', 'a8'],
    "a8" : ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'],
    "h8" : ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'],
    "d4" : ['c3', 'e5', 'c5', 'e3', 'f6', 'b6', 'f2', 'b2', 'g7', 'a7', 'g1', 'a1', 'h8'],
    "e4" : ['d3', 'f5', 'd5', 'f3', 'g6', 'c6', 'g2', 'c2', 'h7', 'b7', 'h1', 'b1', 'a8']
    } 

listKingMovesTest = {
    "a1" : ['a2', 'b2', 'b1'],
    "h1" : ['h2', 'g2', 'g1'],
    "a8" : ['b8', 'a7', 'b7'],
    "h8" : ['g8', 'h7', 'g7'],
    "d4" : ['d5', 'e5', 'c5', 'e4', 'c4', 'd3', 'e3', 'c3'],
    "e4" : ['e5', 'f5', 'd5', 'f4', 'd4', 'e3', 'f3', 'd3']
    }


listKnightMovesTest = { 
    "a1" : ['b3', 'c2'],
    "h1" : ['f2', 'g3'],
    "a8" : ['c7', 'b6'],
    "h8" : ['g6', 'f7'],
    "d4" : ['b5', 'c6', 'e6', 'f5', 'f3', 'e2', 'c2', 'b3'],
    "e4" : ['c5', 'd6', 'f6', 'g5', 'g3', 'f2', 'd2', 'c3']
    }

class moveValidationTest(unittest.TestCase):
    
    def setUp(self):
        self.board = [[0] * 8 for x in xrange(8)]
        pass 'd5', 'c6', 'b7', 'a8'],
    "a8" : ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'],
    "h8" : ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'],
    "d4" : ['c3', 'e5', 'c5', 'e3', 'f6', 'b6', 'f2', 'b2', 'g7', 'a7', 'g1', 'a1', 'h8'],
    "e4" : ['d3', 'f5', 'd5', 'f3', 'g6', 'c6', 'g2', 'c2', 'h7', 'b7', 'h1', 'b1', 'a8']
    } 

listKingMovesTest = {
    "a1" : ['a2', 'b2', 'b1'],
    "h1" : ['h2', 'g2', 'g1'],
    "a8" : ['b8', 'a7', 'b7'],
    "h8" : ['g8', 'h7', 'g7'],
    "d4" : ['d5', 'e5', 'c5', 'e4', 'c4', 'd3', 'e3', 'c3'],
    "e4" : ['e5', 'f5', 'd5', 'f4', 'd4', 'e3', 'f3', 'd3']
    }


listKnightMovesTest = { 
    "a1" : ['b3', 'c2'],
    "h1" : ['f2', 'g3'],
    "a8" : ['c7', 'b6'],
    "h8" : ['g6', 'f7'],
    "d4" : ['b5', 'c6', 'e6', 'f5', 'f3', 'e2', 'c2', 'b3'],
    "e4" : ['c5', 'd6', 'f6', 'g5', 'g3', 'f2', 'd2', 'c3']
    }

class moveValidationTest(unittest.TestCase):
    
    def setUp(self):
        self.board = [[0] * 8 for x in xrange(8)]
        pass
    
    def test_possibleQueenMoves(self):
        print ("Testing Queen Moves")
        for position, expected_moves in listQueenMovesTest.iteritems():
            result = possibleQueenMoves(position, self.board)
            self.assertEqual(sorted(expected_moves), sorted(result),'For position {0}, expected {1} but received {2}'.format(position, expected_moves, result))
            print ('For position {0}, expected {1} but received from Chess,py {2}'.format(position, expected_moves, result))
            
    def test_possibleRookMoves(self):
        print ("Testing Rook Moves")
        for position, expected_moves in listRookMovesTest.iteritems():
            result = possibleRookMoves(position, self.board)
            self.assertEqual(sorted(expected_moves), sorted(result),'For position {0}, expected {1} but received {2}'.format(position, expected_moves, result))
            print ('For position {0}, expected {1} but received from Chess.py {2}'.format(position, expected_moves, result))
            
    def test_possibleBishopMoves(self):
        print ("Testing Bishop Moves")
        for position, expected_moves in listBishopMovesTest.iteritems():
            result = possibleBishopMoves(position, self.board)
            self.assertEqual(sorted(expected_moves), sorted(result),'For position {0}, expected {1} but received {2}'.format(position, expected_moves, result))
            print ('For position {0}, expected {1} but received from Chess.py {2}'.format(position, expected_moves, result))
            
    def test_possibleKingMoves(self):
        print ("Testing King Moves")
        for position, expected_moves in listKingMovesTest.iteritems():
            result = possibleKingMoves(position, self.board)
            self.assertEqual(sorted(expected_moves), sorted(result),'For position {0}, expected {1} but received {2}'.format(position, expected_moves, result))
            print ('For position {0}, expected {1} but received from Chess.py {2}'.format(position, expected_moves, result))
   
    def test_possibleKnightMoves(self):
        print ("Testing Knight Moves")
        for position, expected_moves in listKnightMovesTest.iteritems():
            result = possibleKnightMoves(position, self.board)
            self.assertEqual(sorted(expected_moves), sorted(result),'For position {0}, expected {1} but received {2}'.format(position, expected_moves, result))
            print ('For position {0}, expected {1} but received from Chess.py {2}'.format(position, expected_moves, result))

def testPrintsTrue(self):
    testOutcome.assertTrue(True)
    
if __name__ == '__main__':
    unittest.main()
