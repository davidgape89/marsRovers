import unittest
from MarsRovers import *

class TestPoint(unittest.TestCase):
    def testConstructor(self):
        point = Point()
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)
        point = Point(1,2)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)
    
    def testSum(self):
        point = Point(1,1)
        point2 = Point(3,4)
        point3 = point + point2
        self.assertEqual(point3.x, 4)
        self.assertEqual(point3.y, 5)

    def testEq(self):
        point = Point(1,1)
        point2 = Point(1,1)
        self.assertEqual(point,point2)

class TestPlateau(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(2,1)
        self.assertEqual(plateau.maxX, 2)
        self.assertEqual(plateau.maxY, 1)
        self.assertEqual(plateau.minY, 0)
        self.assertEqual(plateau.minX, 0)
        plateau = Plateau(2,3,1,0)
        self.assertEqual(plateau.maxX, 2)
        self.assertEqual(plateau.maxY, 3)
        self.assertEqual(plateau.minY, 0)
        self.assertEqual(plateau.minX, 1)

    def testIsMovementPossible(self):
        plateau = Plateau(5,5)
        point = Point(1,1)
        self.assertEqual(plateau.isMovementPossible(point), True)
        point = Point(-1, 0)
        self.assertEqual(plateau.isMovementPossible(point), False)
        point = Point(0, -1)
        self.assertEqual(plateau.isMovementPossible(point), False)
        point = Point(6,7)
        self.assertEqual(plateau.isMovementPossible(point), False)

class TestRover(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(5,5)
        direction = MOVEMENT_VECTORS["N"]
        position = Point(0,0)
        marsRover = MarsRover(position,direction,plateau)
        self.assertEqual(Point(0,0), marsRover.position)
        self.assertEqual(Point(0,1), marsRover.direction)
        self.assertEqual(plateau, marsRover.surface)
    def testTurnRight(self):
        plateau = Plateau(5,5)
        direction = MOVEMENT_VECTORS["N"]
        position = Point(0,0)
        marsRover = MarsRover(position,direction,plateau)
        marsRover.turnRight()
        self.assertEqual(Point(1,0), marsRover.direction)
        marsRover.turnRight()
        self.assertEqual(Point(0,-1), marsRover.direction)
    def testTurnRight(self):
        plateau = Plateau(5,5)
        direction = MOVEMENT_VECTORS["N"]
        position = Point(0,0)
        marsRover = MarsRover(position,direction,plateau)
        marsRover.turnLeft()
        self.assertEqual(Point(-1,-0), marsRover.direction)
        marsRover.turnLeft()
        self.assertEqual(Point(0,-1), marsRover.direction)
    def testMove(self):
        plateau = Plateau(5,5)
        direction = MOVEMENT_VECTORS["N"]
        position = Point(0,0)
        marsRover = MarsRover(position,direction,plateau)
        marsRover.move()
        self.assertEqual(Point(0,1), marsRover.position)
        marsRover.move()
        self.assertEqual(Point(0,2), marsRover.position)

class TestInput(unittest.TestCase):
    def testParser(self):
        input = "5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"
        output = "1 3 N\n5 1 E\n"
        self.assertEqual(parse(input), output)
