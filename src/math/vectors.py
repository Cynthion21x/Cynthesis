import math

# Vector value with helper functions
class Vector:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    # Returns magnitude of vector
    def distance(self):

        x = self.x
        y = self.y
        
        return math.sqrt((x * x) + (y * y))
    
    # Return angle between sides
    def angle(self):

        x = self.x
        y = self.y

        if (x == 0):

            return math.pi

        return math.atan(y/x)
    
    # Vector set to values from 0-1
    def normalize(self):

        return FromBearing(self.angle(), 1)

    # Return value as tuple
    def value(self):

        return (self.x, self.y)
    
# Multiply vector by number
def mult(vector1, const):

    return Vector(vector1.x * const, vector1.y * const)

# Add two vectors together
def add(vector1, vector2):
        
    x = vector1.x + vector2.x
    y = vector1.y + vector2.y

    return Vector(x, y)

# Sub two vectors
def sub(vector1, vector2):
        
    x = vector1.x - vector2.x
    y = vector1.y - vector2.y

    return Vector(x, y)

# Generator Functions
def FromBearing(angle, magnitude):

    horizontalComp = math.cos(angle) * magnitude
    verticalComp = math.sin(angle) * magnitude

    return Vector(horizontalComp, verticalComp)

def FromTuple(tup):

    return Vector(tup[0], tup[1])

# Useful constants

def Zero():

    return Vector(0, 0)

