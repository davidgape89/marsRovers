class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

class Plateau:
    def __init__(self, maxX, maxY, minX = 0, minY = 0):
        self.maxX = maxX
        self.minX = minX
        self.maxY = maxY
        self.minY = minY

    def isMovementPossible(self, point):
        return self.minX <= point.x <= self.maxX and self.minY <= point.y <= self.maxY

MOVEMENT_VECTORS = {
    "N": Point(0,1),
    "S": Point(0,-1),
    "E": Point(1,0),
    "W": Point(-1,0)
}

class MarsRover:
    def __init__(self, position, direction, surface):
        self.position = position
        self.direction = direction
        self.surface = surface

    def __str__(self):
        directionString = ""
        for key in MOVEMENT_VECTORS.keys():
            if MOVEMENT_VECTORS[key] == self.direction:
                directionString = key
        return str(self.position.x) + ' ' + str(self.position.y) + ' ' + directionString

    def turnRight(self):
        self.direction = Point(self.direction.y, -self.direction.x)

    def turnLeft(self):
        self.direction = Point(-self.direction.y, self.direction.x)

    def move(self):
        if self.surface.isMovementPossible(self.position + self.direction):
            self.position = self.position + self.direction

def parse(input):
    output = ''
    lines = input.split('\n')
    plateauStr = lines[0]
    lines = lines[1:]
    plateau = Plateau(int(plateauStr[0]),int(plateauStr[2]))
    i=0
    while(i<len(lines)):
        position = Point(int(lines[i][0]),int(lines[i][2]))
        direction = MOVEMENT_VECTORS[lines[i][4]]
        marsRover = MarsRover(position, direction, plateau)
        for instruction in lines[i+1]:
            if instruction == 'M':
                marsRover.move()
            if instruction == 'R':
                marsRover.turnRight()
            if instruction == 'L':
                marsRover.turnLeft()
        output += str(marsRover) + '\n'
        i += 2
    return output
        



