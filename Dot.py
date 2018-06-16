import math
class Dot:

    def __init__(self,newX,newY,newR,newZ):
        """
            Creates new dot being a point
        :param newX: the new x coordinate  of the dot
        :param newY: the new y coordiante of the dot
        :param newR:
        :param newZ:
        """
        self.x=newX
        self.y=newY
        self.r=newR
        self.zOrder=newZ

    def contains(self, pointX, pointY):
        """
            This function checks if the point provided is in the dot in the class
        :param pointX: The x coord of the point to be checked
        :param pointY:  The y coord of the point to be checked
        :return: true if the point is there and false if not
        """
        return self.r > math.sqrt(math.pow(pointX-self.x,2)+ math.pow(pointY-self.y,2))

    def hasChildren(self):
        return False

    def getLeft(self):
        return self.x-self.r

    def getRight(self):
        return 2*self.r

    def getTop(self):
        return self.y-self.r

    def getBottom(self):
        return 2*self.r