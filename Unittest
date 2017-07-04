##Sarah Dettloff
## July 4th

from Chess import *
import unittest

listKingMovesTest = {
    "a1" : ['a2', 'b2', 'b1'],
    "h1" : ['h2', 'g2', 'g1'],
    "a8" : ['b8', 'a7', 'b7'],
    "h8" : ['g8', 'h7', 'g7'],
    "d4" : ['d5', 'e5', 'c5', 'e4', 'c4', 'd3', 'e3', 'c3'],
    "e4" : ['e5', 'f5', 'd5', 'f4', 'd4', 'e3', 'f3', 'd3']
    }

listQueenMovesTest = {
    "a1" : ['b2', 'c3', 'd4', 'e5', 'f6', 'c3', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
    "h1" : ['g2', 'f3', 'e4', 'd5', 'd6', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
    "a8" : ['b7', 'c6', 'd5', 'f3', 'g2', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'],
    "h8" : ['g7', 'f7', 'f6', 'e5', 'd4', 'c3', 'b2', 'a1', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
    "d4" : ['e5', 'c3', 'e3', 'f6', 'b6', 'g7', 'a7', 'b3', 'f2', 'b2', 'g1', 'a1', 'a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8'],
    "e4" : ['f5', 'd3', 'f3', 'g6', 'c6', 'b7', 'a8', 'c3', 'g2', 'c2', 'b1', 'a4', 'b4', 'c4', 'd4', 'f4', 'g4', 'h4', 'e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8']
    }
listBishopMovesTest = { 
    "a1" : ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
    "h1" : ['g2', 'f3', 'e4', 'd5', 'c6', 'b7', 'a8'],
    "a8" : ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'],
    "h8" : ['g8', 'h7', 'g7'],
    "d4" : ['c3', 'e5', 'c5', 'e3', 'f6', 'b6', 'f2', 'b2', 'g7', 'a7', 'g1', 'a1', 'h8'],
    "e4" : ['d3', 'f5', 'd5', 'f3', 'g6', 'c6', 'g2', 'c2', 'h7', 'b7', 'h1', 'b1', 'a8']
    } 
listRookMovesTest = { 
    "a1" : ['b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
    "h1" : ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
    "a8" : ['b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'],
    "h8" : ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
    "d4" : ['a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8'],
    "e4" : ['a4', 'b4', 'c4', 'd4', 'f4', 'g4', 'h4', 'e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8']
    }
listKnightMovesTest = { 
    "a1" : ['b3', 'c2'],
    "h1" : ['f2', 'g3'],
    "a8" : ['b8', 'a7', 'b7'],
    "h8" : ['g6', 'f7'],
    "d4" : ['b5', 'c6', 'e6', 'f5', 'f3', 'e2', 'c2', 'b3'],
    "e4" : ['c5', 'd6', 'f6', 'g5', 'g3', 'f2', 'd2', 'c3']
    }


locationCoordinates = {
    0 : "a1",
    1 : "h1",
    2 : "a8",
    3 : "h8",
    4 : "d4",
    5 : "e4"
    }


class moveValidationTest(unittest.TestCase):
    testOutcome = []
    def setup(testOutcome):
        pass
    
    def test_possibleKingMoves(testOutcome):
        testOutcome = []
        count = 0
        while count < 5:
            count += 1
            try:
                for position in possibleKingMoves == locationCoordinates[0] in possibleKingMoves:
                    if possibleKingMoves(listKingMovesTest[locationCoordinates[0]]) == True:
                        testOutcome.assertEqual(listKingMovesTest[locationCoordinates[0]])
                        return testOutcome(True)
                    else:
                        possibleKingMoves == False
                        return testOutcome(False)
            except:
                pass
            locationCoordinates[0] += locationCoordinates[0 + 1]

    
    def test_possibleQueenMoves(testOutcome):
        testOutcome = []
        count = 0
        while count < 5:
            count += 1
            try:
                for position in possibleQueenMoves == locationCoordinates[0] in possibleQueenMoves:
                    if possibleQueenMoves(listQueenMovesTest[locationCoordinates[0]]) == True:
                        testOutcome.assertEqual(listQueenMovesTest[locationCoordinates[0]])
                        return testOutcome(True)
                    else:
                        possibleQueenMoves == False
                        return testOutcome(False)
            except:
                pass
            locationCoordinates[0] += locationCoordinates[0 + 1]
            
    def test_possibleBishopMoves(testOutcome):
        testOutcome = []
        count = 0
        while count < 5:
            count += 1
            try:
                for position in possibleBishopMoves == locationCoordinates[0] in possibleBishopMoves:
                    if possibleBishopMoves(listBishopMovesTest[locationCoordinates[0]]) == True:
                        testOutcome.assertEqual(listBishopMovesTest[locationCoordinates[0]])
                        return testOutcome(True)
                    else:
                        possibleBishopsMoves == False
                        return testOutcome(False)
            except:
                pass
            locationCoordinates[0] += locationCoordinates[0 + 1]
            
    def test_possibleRookMoves(testOutcome):
        testOutcome = []
        count = 0
        while count < 5:
            count += 1
            try:
                for position in possibleRookMoves == locationCoordinates[0] in possibleRookMoves:
                    if possibleRookMoves(listRookMovesTest[locationCoordinates[0]]) == True:
                        testOutcome.assertEqual(listRookMovesTest[locationCoordinates[0]])
                        return testOutcome(True)
                    else:
                        possibleRookMoves == False
                        return testOutcome(False)
            except:
                pass
            locationCoordinates[0] += locationCoordinates[0 + 1]
            
    def test_possibleKnightMoves(testOutcome):
        testOutcome = []
        count = 0
        while count < 5:
            count += 1
            try:
                for position in possibleKnightMoves == locationCoordinates[0] in possibleKnightMoves:
                    if possibleKnightMoves(listKnightMovesTest[locationCoordinates[0]]) == True:
                        testOutcome.assertEqual(listKnightMovesTest[locationCoordinates[0]])
                        return testOutcome(True)
                    else:
                        possibleKnightMoves == False
                        return testOutcome(False)
            except:
                pass
            locationCoordinates[0] += locationCoordinates[0 + 1]

            
def testPrintsTrue(testOutcome):
    testOutcome.assertTrue(True)
    
if __name__ == '__main__':
    unittest.main()

